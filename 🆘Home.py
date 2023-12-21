import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

######################################################################################################################
# title #
######################################################################################################################
st.set_page_config(
    page_title="Suicide Ideation",
    page_icon="🆘",
    layout="wide",
)

st.title("Suicide Ideation")
st.markdown("Suicide ideation, or thoughts of suicide, is a global concern, claiming over 700,000 lives annually and ranking as the fourth leading cause of death among 15-29 years old adults. Malaysia has seen a rise in suicides, with notable cases reported in 2022. ")
with st.container(border=True):
    st.image('./dashboard/intro.jpg', caption='Number of suicide in Malaysia')
st.markdown('Suicidal ideation shows up with changes in behavior, speech, and thinking, often accompanied by feelings of guilt, shame, and discussions about death. Nowadays, individuals tend to share their thoughts and emotions on social media platforms. This system capitalizes on this trend by collecting posts from social media and training a prediction model with them. The system can be used to predict whether the text indicates suicidal or non-suicidal tendencies.')
######################################################################################################################
# model #
######################################################################################################################

###### model & vectorizer import ##########
import joblib
model = joblib.load('./logistic_regression_model.joblib')
vectorizer = joblib.load('./vectorizer.pkl')

st.markdown('Let\'s try to predict your text:')
text = st.text_input('Enter text and press ENTER. This might take some times to load the result.')

####### preprocess text ##########
import re
import string
import nltk
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
from nltk.stem import WordNetLemmatizer
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
from collections import Counter

def mostfrequencyemoji(emojies):
    if emojies == []:
        final = ''
    else:
        final = Counter(emojies)
        final = max(final, key=final.get)

    return final


import emoji
import advertools as adv
emojidf = adv.emoji_df

def emoji_extraction(text):
    emojis = [x for x in text if emoji.is_emoji(x)]
    emojies_count = emoji.emoji_count(text)
    unique_emojies_count = emoji.emoji_count(text, unique=True)
    mostfreqemoji = mostfrequencyemoji(emojis)
    emojilabel = emojidf.index[emojidf['emoji'] == mostfreqemoji].tolist()
    if len(emojilabel) < 1:
        emojilabel = 0
    else:
        emojilabel = emojilabel[0] + 1

    df = {'emojies_count': emojies_count,
    'unique_emojies_count': unique_emojies_count,
    'most_freq_emoji': emojilabel}

    return df

import demoji

def text_vectorization(text, df1):
    text = [demoji.replace_with_desc(text, " ")]
    unigram = vectorizer.transform(text)
    unigram = pd.DataFrame.sparse.from_spmatrix(unigram)
    unigram = unigram.iloc[-1:]
    unigram['emojies_count'] = df1['emojies_count']
    unigram['unique_emojies_count'] = df1['unique_emojies_count']
    unigram['most_freq_emoji'] = df1['most_freq_emoji']
    
    return unigram

def features_extraction(text):
    df1 = emoji_extraction(text)
    unigram = text_vectorization(text, df1)
    return unigram

######################################################################################################################
# implement model #
######################################################################################################################

if text:
    text = preprocessing_text(text)
    features = features_extraction(text)
    X = features.iloc[:, :].values
    y_pred = model.predict(X)
    if y_pred == 0:
        st.markdown("The text entered is classified as non-suicide text.")
    else:
        st.markdown("The text entered is classified as suicide text.")
