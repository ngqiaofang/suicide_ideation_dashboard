import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="EDA",
    page_icon="📊",
    layout="wide",
)

st.title("Exploratory Data Analysis")
# st.markdown("This page contains the information of EDA.")
st.text("It might take some times (few minutes) to load.")
######################################################################################################################
# EDA #
######################################################################################################################
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
from wordcloud import STOPWORDS

#################
# Dataset #
################

df = pd.read_csv('pages/Suicide_Detection.csv.gzip', compression="gzip")
df.columns =['no', 'text', 'class']
df['no'] = df.index

##########################
# non-suicide wordcloud #
##########################

df1 = df.loc[df['class']=="non-suicide"]

# text1 = " ".join(i for i in df1.text.str.lower())
# text1 = ''.join(i for i in text1 if ord(i) < 128)
# stopwords = set(STOPWORDS)
# wordcloud1 = WordCloud(stopwords=stopwords, background_color="white").generate(text1)

######################
# suicide wordcloud #
######################

df2 = df.loc[df['class']=="suicide"]

# text2 = " ".join(i for i in df2.text.str.lower())
# text2 = ''.join(i for i in text2 if ord(i) < 128)
# stopwords = set(STOPWORDS)
# wordcloud2 = WordCloud(stopwords=stopwords, background_color="white").generate(text2)

st.markdown("Wordclouds of non-suicide and suicide text.")
tab1, tab2 = st.tabs(["Non-suicide", "Suicide"])
with tab1:
    # fig1 = plt.figure()
    # plt.imshow(wordcloud1, interpolation='bilinear')
    # plt.title("Wordcloud of non-suicide")
    # plt.axis("off")
    # st.pyplot(fig1)
    st.image('./wordcloud1.png')
with tab2:
    # fig2 = plt.figure()
    # plt.imshow(wordcloud2, interpolation='bilinear')
    # plt.title("Wordcloud of suicide")
    # plt.axis("off")
    # st.pyplot(fig2)
    st.image('./wordcloud1.png')


##########################
# emoji non-suicide #
##########################
import emoji
from collections import Counter

emoji1 = "".join(x for i in df1.text for x in i if emoji.is_emoji(x) )
Counter(emoji1).most_common(10)
emojies1 = [Counter(emoji1).most_common(10)[i][0] for i in range(10)]
frequency1 = [Counter(emoji1).most_common(10)[i][1] for i in range(10)]

import plotly.express as px

fig1 = px.bar(x=emojies1, y =frequency1, title = "Top 10 emojies used in non-suicide",
              labels={'x': "Emojies", 'y': " "})
total1 = sum(Counter(emoji1).values())

##########################
# emoji suicide #
##########################

emoji2 = "".join(x for i in df2.text for x in i if emoji.is_emoji(x) )
Counter(emoji2).most_common(10)
emojies2 = [Counter(emoji2).most_common(10)[i][0] for i in range(10)]
frequency2 = [Counter(emoji2).most_common(10)[i][1] for i in range(10)]

fig2 = px.bar(x=emojies2, y =frequency2, title = "Top 10 emojies used in suicide",
              labels={'x': 'Emojies', 'y': ' '})
total2 = sum(Counter(emoji2).values())

st.markdown("Top 10 emojies used in non-suicide and suicide text.")
tab1, tab2 = st.tabs(["Non-suicide", "Suicide"])
with tab1:
    st.plotly_chart(fig1, use_container_width=True)
    st.write("Total of ", total1, "emojies are used in non-suicide")
with tab2:
    st.plotly_chart(fig2, use_container_width=True)
    st.write("Total of ", total2, "emojies are used in suicide")
    

######################
# class distribution #
######################

data = {'non-suicide':5054, 'suicide':4946}
classes = list(data.keys())
number = list(data.values())


st.markdown("Distribution of Classes")
fig3 = px.bar(x=classes, y =number, title = "Class Ditribution of Sampling Dataset",
              labels={'x': " ", 'y': " "})
# fg = iplot([trace])
st.plotly_chart(fig3, use_container_width=True)
