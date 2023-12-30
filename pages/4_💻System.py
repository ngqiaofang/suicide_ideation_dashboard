import streamlit as st
import plotly.express as px
from streamlit_extras import add_vertical_space as avs 
import pandas as pd
from streamlit_extras.switch_page_button import switch_page 


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
    scikiturl = "https://scikit-learn.org/0.16/modules/generated/sklearn.linear_model.LogisticRegression.html"
    scikit= f"""    
    <p>The classification model used is <span style="font: bold; color: #f8a811">Logistic Regression</span> from
    <a href={scikiturl}>scikit-learn </a>python library.</p>
    """
    st.subheader('Logistic Regression')
    st.markdown(scikit, unsafe_allow_html=True)
    st.markdown("The paremeters are set to default except for:")
    st.markdown("- Solver: liblinear")
    st.markdown("- Max_iter: 10000")

    st.text("'liblinear' is a solver that recommended when we have high dimension dataset (recommended for solving large-scale classification problems)")
# “liblinear” (A Library for Large Linear Classification):

# It’s a linear classification that supports logistic regression and linear support vector machines.

# The solver uses a Coordinate Descent (CD) algorithm that solves optimization problems by successively performing approximate minimization along coordinate directions or coordinate hyperplanes.

# liblinear applies L1 Regularization and it’s recommended when we have high dimension dataset (recommended for solving large-scale classification problems).

    avs.add_vertical_space(2)
    st.subheader('Result of Training Model')
    # plot_confusion_matrix(model, x_test, y_test, display_labels=   class_names)
    #     st.pyplot()
    data = {
        "Metics": ["Accuracy", "F1-score", "Precision", "Recall"],
        "Values": ["0.91","0.90", "0,91", "0.91"]
    }
    df = pd.DataFrame(data)
    st.dataframe(data,hide_index=True, use_container_width=True)



    # # Imports
    # from mlxtend.plotting import plot_confusion_matrix
    # import matplotlib.pyplot as plt
    # import numpy as np

    # # Your Confusion Matrix
    # cm = np.array([[1401, 85],
    #                 [ 200, 1314]])

    # # Classes
    # classes = ['non-suicide', 'suicide']

    # figure, ax = plot_confusion_matrix(conf_mat = cm,
    #                                 class_names = classes,
    #                                 show_absolute = False,
    #                                 show_normed = True,
    #                                 colorbar = True)
    # st.pyplot(figure)


if selected == "Features":
    st.subheader('Features Selected:')
    st.markdown("- Text vectorization, including emoji-converted text, using unigram")
    st.markdown("- Count of emoji in the text")
    st.markdown("- Most frequent used emoji in the text")
    
avs.add_vertical_space(2)
col1, col2, col3 = st.columns([1,3,1])
with col2:
    predictpage = st.button("Let's try to predict your text", use_container_width=True)
    if predictpage:
        switch_page("prediction")
