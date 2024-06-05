import streamlit as st
from streamlit_extras import add_vertical_space as avs 
from streamlit_extras.switch_page_button import switch_page 
from streamlit.components.v1 import html

######################################################################################################################
# title #
######################################################################################################################
st.set_page_config(
    page_title="Suicide Ideation",
    page_icon="🆘",
    layout="wide",
)

st.title("Suicide Ideation")
st.markdown("Suicidal ideation, also known as suicidal thoughts, refers to people’s plans to commit suicide. ")

st.sidebar.markdown("## More About Suicide")
st.sidebar.link_button("Suicide", "https://www.who.int/news-room/fact-sheets/detail/suicide")
st.sidebar.link_button("World Suicide Prevention Day", "https://www.who.int/campaigns/world-suicide-prevention-day")
st.sidebar.markdown("---")
st.sidebar.markdown("## Do you need help?")
st.sidebar.link_button("Helplines", "https://findahelpline.com/countries/my/topics/suicidal-thoughts")

html1 = f"""
    <style>
        .container {{
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-around;
            padding: 1em 0;
            position: relative;
            font-size: 16px;
            border-radius: 0.5em;
            border: 1px solid #ff7a12
            background-color: #ffffff;
        }}

        span.num {{
            color: #ff7a12;
            display: grid;
            place-items: center;
            font-family: "Source Sans Pro", sans-serif;
            font-weight: 600;
            font-size: 3em;
        }}
    </style>


   <div class="container">
        <span class="num" data-val="700000">000</span>
    </div> 
    
    <script>
        let valueDisplays = document.querySelectorAll(".num");
        let interval = 2000;
        valueDisplays.forEach((valueDisplay) => {{
            let startValue = 0;
            let endValue = parseInt(valueDisplay.getAttribute("data-val"));
            let duration = Math.floor(interval / endValue);
            let counter = setInterval(function () {{

                if (startValue < 10000) {{
                    startValue += 100;
                }}

                if (startValue < 100000) {{
                    startValue += 1000;
                }}

                if (startValue >= 100000) {{
                    startValue += 10000;
                }}
      

                if (startValue >= endValue) {{
                    clearInterval(counter);
                }}

                valueDisplay.textContent = startValue + '+';


            }}, duration);
        }});
        
    </script>"""


html(html1, height = 70)
text1 = f"""
<h2 style='
    text-align: center; 
    font-family:"Source Sans Pro", 
    sans-serif; 
    font-weight: 400; 
    font-size: 2em;'>
    People <span style='color: #f8a811;'>DIE</span> due to suicide every year </h2>
"""
st.markdown(text1, unsafe_allow_html=True)
   
   
avs.add_vertical_space(2) 


rise="https://ourworldindata.org/grapher/number-of-deaths-from-suicide-ghe?country=~MYS"

cases="https://www.thestar.com.my/news/nation/2022/09/28/kj-increase-in-suicides-and-mental-health-issues-troubling-prompt-action-needed"

links= f"""
    <style>
     .a:link, visited {{
       color: #ff7a12;
       background-color: transparent;
       text-decoration: none;
     }}
     .a: hover{{
        color: #f8a811;
     }}
    </style>
    
    <p>Suicide ideation, is a global concern, claiming over 700,000 lives annually and ranking as the 4th 
    leading cause of death among 15-29 years old adults. Malaysia has seen a 
    <a href={rise}>rise </a>in suicides, with notable cases reported in <a href={cases}>2021</a>.</p>
    """
st.markdown(links,unsafe_allow_html=True)

avs.add_vertical_space(1) 
st.markdown(f""" Nowadays, individuals tend to share their thoughts and emotions on social media platforms. By collecting texts 
            from social media and training a prediction model with them, a suicide ideation prediction system can be developed.
             The system can be used to predict whether the text indicates suicidal or non-suicidal tendencies.
            """)

col1, col2, col3 = st.columns(3)
with col1:
    edapage = st.button("Explore the texts", use_container_width=True)
    if edapage:
        switch_page("eda")    
with col2:
    predictpage = st.button("Let's predict your text", use_container_width=True)
    if predictpage:
        switch_page("prediction")    
with col3:
    modelpage = st.button("Look into how's the prediction system works", use_container_width=True)
    if modelpage:
        switch_page("system")    

avs.add_vertical_space(1)

st.subheader("Symptoms of suicidal ideation")
st.markdown("Suicidal ideation shows up with changes in speech, thinking and behaviour.") 
# col1, col2, col3 = st.columns(3, gap='large')
tab1, tab2, tab3 = st.tabs(["Speech","Thinking", "Behavior"])
with tab1:
    with st.container(border=True):
        # st.subheader("Speech")
        st.markdown("The person might talk about:")
        st.markdown("- their feelings of guilt or shame")
        st.markdown("- being a burden to others")
        st.markdown("- death")
with tab2:
    with st.container(border=True):
        # st.subheader("Thinking")
        st.markdown("The person may feel:")
        st.markdown("- unbearable emotional pain")
        st.markdown("- extremely anxious and sad, full of rage, or agitated")
        st.markdown("- trapped, hopeless, empty, or that there is no reason to live")
        st.markdown("- severe fluctuations in mood or mood swings")
with tab3:
    with st.container(border=True):
        # st.subheader("Behaviour")
        st.markdown("The person may:")
        st.markdown("- withdraw from friends or family")
        st.markdown("- sleep or eat more or less")
        st.markdown("- take dangerous risks")
        st.markdown("- give away important possessions or money")
        st.markdown("- use alcohol or drugs more frequently")


           


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
            <div class = 'regular'>To anyone out there who’s hurting — it’s not a sign of weakness to ask for help. It’s a sign of strength.</div>
        </div>
        <p style="text-align:center;">- <span style="font-style: italic">Barack Obama</span></p>
    </div>

"""

st.markdown(quote, unsafe_allow_html=True)

