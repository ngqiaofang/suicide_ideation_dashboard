import streamlit as st
import plotly.express as px
from streamlit_extras import add_vertical_space as avs 
import pandas as pd
from streamlit_extras.switch_page_button import switch_page 
import plotly.graph_objs as go

st.set_page_config(
    page_title="About the System",
    page_icon="💻",
    layout="wide",
)

st.title("About the System")

st.sidebar.markdown("## More About Suicide")
st.sidebar.link_button("Suicide", "https://www.who.int/news-room/fact-sheets/detail/suicide")
st.sidebar.link_button("World Suicide Prevention Day", "https://www.who.int/campaigns/world-suicide-prevention-day")
st.sidebar.markdown("---")
st.sidebar.markdown("## Do you need help?")
st.sidebar.link_button("Helplines", "https://findahelpline.com/countries/my/topics/suicidal-thoughts")

######################
# class distribution #
######################

data = {'Non-suicide':5054, 'Suicide':4946}
classes = list(data.keys())
number = list(data.values())

fig = px.bar(x=classes, y =number, title = "Class Ditribution of Sampling Dataset",
            labels={'x': " ", 'y': " "})
fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False)
fig.update_traces(marker_color='#f8a811')

avs.add_vertical_space(1)

selected = st.selectbox("Choose one part of the system to focus on it:", ["Dataset", "Model", "Features"])



avs.add_vertical_space(1)

if selected == "Dataset":
    dataurl = "https://www.kaggle.com/datasets/nikhileswarkomati/suicide-watch"

    dataset= f"""    
    <p>The <a href={dataurl}>dataset </a>chosen comprises of 232,074 texts and is 
    categorized into two classes: suicide and non-suicide. It has been undersampled to 10,000 texts for training data.</p>
    """

    
    st.subheader("Distribution of Classes")

    st.markdown(dataset, unsafe_allow_html=True)

    st.plotly_chart(fig, use_container_width=True)
    st.write("The undesampled data is balanced, as both classes have nearly equal representation.")


    avs.add_vertical_space(4)

    # st.divider()
    st.subheader('Sample Texts')   

    data = {
        "Texts": ["It ends tonight.I can't do it anymore. I quit.", "Day 1: Useless facts until quarintine is over Sharks are the only fish that can blink with both eyes."],
        "Classes": ["suicide","non-suicide"]
    }
    df = pd.DataFrame(data)
    st.dataframe(data,hide_index=True, use_container_width=True)



if selected == "Model":
    scikiturl = "https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC"
    scikit= f"""    
    <p>The calssification model used is <span style="font: bold; color: #f8a811">Support Vector Machine(SVM)</span> from
    <a href={scikiturl}>scikit-learn </a>python library.</p>
    """
    st.subheader('SVM')
    st.markdown(scikit, unsafe_allow_html=True)

    avs.add_vertical_space(2)
    st.subheader('Result of Training Model')
    data = {
        "Metics": ["Accuracy", "F1-score", "Precision", "Recall"],
        "Values": ["0.92","0.91", "0.92", "0.92"]
    }
    df = pd.DataFrame(data)
    st.dataframe(data,hide_index=True, use_container_width=True)

    cm = [[1391,95], [ 160 ,1354]]
    # create the heatmap
    heatmap = go.Heatmap(z=cm, text=cm, texttemplate="%{text}",textfont={"size":15}, x=['non-suicide', 'suicide'], y=['non-suicide', 'suicide'], colorscale='Oranges')

    # create the layout
    layout = go.Layout(title='Confusion Matrix', xaxis=dict(title="Predicted Label"), yaxis=dict(title="True Label"))

    # create the figure
    fig = go.Figure(data=[heatmap], layout=layout)
    fig.layout.height = 500
    fig.layout.width = 500

    # show the figure
    st.plotly_chart(fig, use_container_width=True)


if selected == "Features":
    st.subheader('Features Selected:')
    st.markdown("- Text vectorization, including emoji-converted text, using Term Frequency - Inverse Document Frequency (TF-IDF)")
    st.markdown("- Count of emoji in the text")
    st.markdown("- Most frequent used emoji in the text")
    
avs.add_vertical_space(2)
col1, col2, col3 = st.columns([1,3,1])
with col2:
    predictpage = st.button("Let's try to predict your text", use_container_width=True)
    if predictpage:
        switch_page("prediction")
