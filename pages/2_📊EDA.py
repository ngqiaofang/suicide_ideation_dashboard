import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from streamlit_extras import add_vertical_space as avs
from streamlit_extras.switch_page_button import switch_page 

st.set_page_config(
    page_title="EDA",
    page_icon="📊",
    layout="wide",
)

st.title("Exploratory Data Analysis")

st.sidebar.markdown("## More About Suicide")
st.sidebar.link_button("Suicide", "https://www.who.int/news-room/fact-sheets/detail/suicide")
st.sidebar.link_button("World Suicide Prevention Day", "https://www.who.int/campaigns/world-suicide-prevention-day")
st.sidebar.markdown("---")
st.sidebar.markdown("## Do you need help?")
st.sidebar.link_button("Helplines", "https://findahelpline.com/countries/my/topics/suicidal-thoughts")


avs.add_vertical_space(2) 

######################################################################################################################
# EDA #
######################################################################################################################

#################
# Dataset #
################

df = pd.read_csv('pages/Suicide_Detection.csv.gzip', compression="gzip")
df.columns =['no', 'text', 'class']
df['no'] = df.index

df1 = df.loc[df['class']=="suicide"]
df2 = df.loc[df['class']=="non-suicide"]



#######################
# Wordcloud
#########################

st.subheader("Word Clouds of Suicide and Non-suicide Texts")
tab1, tab2 = st.tabs(["Suicide", "Non-suicide"])

######################
# suicide wordcloud #
######################

with tab1:

    st.image('./wordcloud_suicide.png', caption="Suicide Texts", use_column_width='auto')
    with st.expander("See Explanation"):
        st.write(f"""In suicide texts, keywords like "know", "want", "feel", "life" and "think" stand out prominently. 
                 This suggest a consistent thematic focus on understanding, personal desires, emotional expression, 
                 life's challenges, and introspective thinking. Additionally, negative words related to suicide, 
                 such as "die", "kill", "depression" and "help" can be found in the word cloud, indicating a more distressing tone.
                 """)
        st.write(f"""The identifiable linguistic patterns in suicide texts may provide valuable insights for 
                 the development of tools aimed at early detection for individuals expressing suicidal thoughts.""")
     

##########################
# non-suicide wordcloud #
##########################
                
with tab2:

    st.image('./wordcloud_non-suicide.png', caption="Non-suicide Texts", use_column_width='auto')
    with st.expander("See Explanation"):
        st.write(f"""Compared to suicide texts, there isn't a clear set of specific words that stand out prominently 
                 in non-suicide texts, indicating a random distribution of words. This suggests a diverse range of topics 
                 and expressions without consistent linguistic markers. Additionally, a typing pattern is observed where 
                 individuals tend to continuously repeat the same words, like "cheese cheese", "filler filler", "fuck fuck" 
                 and "sus sus". 
                 """)

avs.add_vertical_space(2) 
st.divider()
################################################################################################
# emoji
########################################################
st.subheader("Emojis Used in Suicide and Non-suicide Texts")


##########################
# emoji suicide #
##########################

emojis1 = np.load('./emoji_suicide.npy').tolist()
frequency1 = np.load('./frequency_suicide.npy').tolist()

fig1 = px.bar(x=emojis1, y =frequency1[:-1], title = "Top 10 emojis used in suicide texts",
              labels={'x': 'Emojis', 'y': 'Count'})
fig1.update_xaxes(showgrid=False)
fig1.update_yaxes(showgrid=False)
fig1.update_traces(marker_color='#f8a811')
total1 = frequency1[-1]

totalstr1 = f"""
<p>Total of <span style="color:#ff7a12; font-weight: bold">{total1}</span> emojis used in suicide texts.</p>
"""

##########################
# emoji non-suicide #
##########################


emojis2 = np.load('./emoji_non-suicide.npy').tolist()
frequency2 = np.load('./frequency_non-suicide.npy').tolist()

fig2 = px.bar(x=emojis2, y =frequency2[:-1], title = "Top 10 emojis used in non-suicide texts",
              labels={'x': "Emojis", 'y': "Count"}, color_discrete_sequence =['#f8a811']*len(emojis2))
fig2.update_xaxes(showgrid=False)
fig2.update_yaxes(showgrid=False)
total2 = frequency2[-1]

totalstr2 = f"""
<p>Total of <span style="color:#ff7a12; font-weight: bold">{total2}</span> emojis used in non-suicide texts.</p>
"""

tab1, tab2 = st.tabs(["Suicide", "Non-suicide"])
with tab1:
    st.plotly_chart(fig1, use_container_width=True)
    st.write(totalstr1, unsafe_allow_html=True)
    avs.add_vertical_space(1) 
    with st.expander("See Explanation"):
        st.write(f"""Emojis in suicide texts mostly consist of facial expressions, evoking emotions like sadness 
                 and disappointment. Negative emotions are prominently represented through emojis like the loud 
                 crying face 😭, the disappointed face 😞, and the broken heart 💔', emphasizing themes 
                 of sadness, disappointment, and emotional pain. Only a minority of positive emojis is present 
                 within the top 10 used emojis and the total count of emojis is much less than in non-suicide texts. 
                 """)



with tab2:
    st.plotly_chart(fig2, use_container_width=True)
    st.write(totalstr2, unsafe_allow_html=True)
    avs.add_vertical_space(1) 
    with st.expander("See Explanation"):
        st.write(f"""The most frequently used emojis in non-suicide texts express various feeling, from joy 
                 to sadness and also include object-related symbols such as the pool 8 ball 🎱. Emojis like 
                 the laughter emoji 😂 shows fun and playfulness, while the crying face emoji 😭 reflects sadness, 
                 contributing to the diverse emotional landscape. Only a few of negative emojis is present within 
                 the top 10 used emojis and there are lots of emojis used compared to suicide texts. 
                 """)

avs.add_vertical_space(2) 
st.divider()
################################################################################################
# sentiment
########################################################
st.subheader("Sentiment Distribution in Suicide and Non-suicide Texts")


fig1 = px.bar(x=["Negative", "Neutral", "Positive"], y =[73872, 20730, 21435], title = "Sentiment labels distribution in suicide text",
              labels={'x': 'Sentiment Label', 'y': 'Count'}, color_discrete_sequence =['#f8a811']*3)
fig1.update_xaxes(showgrid=False)
fig1.update_yaxes(showgrid=False)


fig2 = px.bar(x=["Negative", "Neutral", "Positive"], y =[26369, 49047, 40621], title = "Sentiment labels distribution in non-suicide text",
              labels={'x': 'Sentiment Label', 'y': 'Count'}, color_discrete_sequence =['#f8a811']*3)
fig2.update_xaxes(showgrid=False)
fig2.update_yaxes(showgrid=False)


tab1, tab2 = st.tabs(["Suicide", "Non-suicide"])
with tab1:
    st.plotly_chart(fig1, use_container_width=True)
    avs.add_vertical_space(1) 
    with st.expander("See Explanation"):
        st.write(f"""Most of the suicidal text is labeled as negative. This suggests that 
                 the main emotional tone in suicidal texts is negative.
                 """)

with tab2:
    st.plotly_chart(fig2, use_container_width=True)
    avs.add_vertical_space(1) 
    with st.expander("See Explanation"):
        st.write(f"""Most of the non-suicidal texts are labeled as positive or neutral, with only a few categorized as negative. 
                 This suggests that the main emotional tone in non-suicidal texts is positive or neutral.
                 """)

avs.add_vertical_space(2)
col1, col2, col3 = st.columns([1,3,1])
with col2:
    predictpage = st.button("Let's try to predict your text", use_container_width=True)
    if predictpage:
        switch_page("prediction")
