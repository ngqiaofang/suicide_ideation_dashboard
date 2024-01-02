import streamlit as st
import pandas as pd
from io import StringIO
from streamlit_extras import add_vertical_space as avs
from streamlit_extras.row import row
from streamlit_extras.switch_page_button import switch_page 
import joblib
import re
import string
import nltk
import emoji
import advertools as adv
import demoji
from collections import Counter
from nltk.stem import WordNetLemmatizer

st.set_page_config(
    page_title="Suicide Ideation Prediction",
    page_icon="💡",
    layout="wide",
)

st.title("Suicide Ideation Prediction")

st.sidebar.markdown("## More About Suicide")
st.sidebar.link_button("Suicide", "https://www.who.int/news-room/fact-sheets/detail/suicide")
st.sidebar.link_button("World Suicide Prevention Day", "https://www.who.int/campaigns/world-suicide-prevention-day")
st.sidebar.markdown("---")
st.sidebar.markdown("## Do you need help?")
st.sidebar.link_button("Helplines", "https://findahelpline.com/countries/my/topics/suicidal-thoughts")


quote = f"""
    <style>
    .regular {{
        position: relative;
        padding-top:20px;
        padding-bottom: 50px;
        text-align: center;
        text-size-adjust: auto;
        align-self: center;

        &::before {{
            content: "“";
            position: relative;
            font-weight: bold;
            font-size: 3em;
            color: #f8a811;
            top: -20px;
            left: -15px;
            font-family: Georgia, Times, serif;
        }}
        &::after {{
            content: "”";
            position: relative;
            font-weight: bold;
            font-size: 3em;
            color: #f8a811;
            bottom: -70px;
            right: -15px;
            font-family: Georgia, Times, serif;
        }}
    }}

    </style>
    <div>
        <div>
            <div class = 'regular'>There is some good in this world, and it’s worth fighting for.</div>
        </div>
        <p style="text-align:center;">- <span style="font-style: italic">J.R.R. Tolkien</span></p>
    </div>

"""


######################################################################################################################
# model #
######################################################################################################################

###### model & vectorizer import ##########
model = joblib.load('./svm_compressed.pkl')
vectorizer = joblib.load('./vectorizer_tfidf.pkl')

st.subheader('Let\'s try to predict your text:')

####################### user input ######################

st.markdown("Choose the input method you prefer:")
rows = row(2, vertical_align="center")
but1 = rows.button("Text", use_container_width=True)
but2 = rows.button("File", use_container_width=True)
# inputType = st.radio("",["Text", "File"], horizontal=True)

if but2:
    inputType = 'File'
else:
    inputType = 'Text'

avs.add_vertical_space(1) 

if inputType == 'File':
    submitted = st.file_uploader("Upload a .txt file. This might take some times to load the result.", type=("txt"))
    if submitted:
        stringio=StringIO(submitted.getvalue().decode('utf-8'))
        text=stringio.read()
else:
    with st.form("myform"):
        text = st.text_input("Enter text and click submit. This might take some times to load the result.", "")
        submitted = st.form_submit_button("Submit")

######################## model
avs.add_vertical_space(2) 
if not submitted:
    modelpage = st.button("Look into how's the prediction system works", use_container_width=True)
    if modelpage:
        switch_page("system")

####### preprocess text ##########

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')

wordnet_lemmatizer = WordNetLemmatizer()

def preprocessing_text(text):
    text = re.sub(r'http\S+', '', text) 
    text = "".join([i for i in text if i not in string.punctuation])
    text = text.replace("’", "")
    text = " ".join(text.split())
    text = text.lower()

    tokens = nltk.word_tokenize(text)
    stopwords = nltk.corpus.stopwords.words('english')
    tokens = [i for i in tokens if i not in stopwords]
    tokens = [wordnet_lemmatizer.lemmatize(i) for i in tokens]
    text = ' '.join(map(str,tokens))

    return text


####### feature extraction ################

def mostfrequencyemoji(emojies):
    if emojies == []:
        final = ''
    else:
        final = Counter(emojies)
        final = max(final, key=final.get)

    return final



emojidf = adv.emoji_df

def emoji_extraction(text):
    emojis = [x for x in text if emoji.is_emoji(x)]
    emojies_count = emoji.emoji_count(text)
    # unique_emojies_count = emoji.emoji_count(text, unique=True)
    mostfreqemoji = mostfrequencyemoji(emojis)
    emojilabel = emojidf.index[emojidf['emoji'] == mostfreqemoji].tolist()
    if len(emojilabel) < 1:
        emojilabel = 0
    else:
        emojilabel = emojilabel[0] + 1

    # df = {'emojies_count': emojies_count,
    # 'unique_emojies_count': unique_emojies_count,
    # 'most_freq_emoji': emojilabel}

    df = {'emojies_count': emojies_count,
    'most_freq_emoji': emojilabel}

    return df


def text_vectorization(text, df1):
    text = [demoji.replace_with_desc(text, " ")]
    unigram = vectorizer.transform(text)
    unigram = pd.DataFrame.sparse.from_spmatrix(unigram)
    unigram = unigram.iloc[-1:]
    unigram['emojies_count'] = df1['emojies_count']
    # unigram['unique_emojies_count'] = df1['unique_emojies_count']
    unigram['most_freq_emoji'] = df1['most_freq_emoji']
    
    return unigram

def features_extraction(text):
    df1 = emoji_extraction(text)
    unigram = text_vectorization(text, df1)
    return unigram

######################################################################################################################
# implement model + result
######################################################################################################################

if submitted:
    text = preprocessing_text(text)
    features = features_extraction(text)
    X = features.iloc[:, :].values
    y_pred = model.predict(X)
    if y_pred == 0:
        st.balloons()
        st.subheader("Congratulations! Your text is classified as non-suicide text!")
        modelpage = st.button("Look into how's the prediction system works", use_container_width=True)
        if modelpage:
            switch_page("system")
    else:
        st.subheader("Your text is classified as suicide text.")      
        st.markdown(quote, unsafe_allow_html=True)
        col1, col2, col3 = st.columns([2,3,2])
        with col2:
            st.link_button("Find a helpline here", "https://findahelpline.com/countries/my/topics/suicidal-thoughts", use_container_width=True)
            avs.add_vertical_space(1)
            modelpage = st.button("Look into how's the prediction system works", use_container_width=True)
            if modelpage:
                switch_page("system")   
