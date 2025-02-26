import streamlit as st
import base64


st.set_page_config(
    page_title = "Sentiment Analysis",
    page_icon = "🌉",
    layout = "wide"
)

# Sidebar navigation header
with st.sidebar:
    st.header("🔍 Navigate the App")
    st.write("Use the links above to explore:")
    st.markdown("""
    - **Sentiments About Mito**: Explore sentiments about MitoLabs on the web.
    - **AI Agent Trends**: Time series analysis of \"AI agent\" google searches.
    - **About Bena**: A bit about me!
    """)


# Code to size image with the text from ash2shukla https://discuss.streamlit.io/t/image-and-text-next-to-each-other/7627/18
st.markdown(
    """
    <style>
    .container {
        display: flex;
    }
    .logo-text {
    }
    .logo-img {
        float:right;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class="container">
        <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open("figures/Mitochondria.png", "rb").read()).decode()}">
        <h2 class="logo-text">Sentiments About Mito</h2>
    </div>
    """,
    unsafe_allow_html=True
)

st.write(f"The bar graph below shows the distribution of sentiments of webpages mentioning Mito Spreadsheets. Click on a bar to view each link.")

with open('figures/SentimentsGraph.html', 'r', encoding='utf-8') as file:
    sentiment_graph_data = file.read()


st.components.v1.html(sentiment_graph_data, height=650, width=1500)


col1, col2, col3 = st.columns([1, 1, 1])  

with col1: 
    st.markdown(f"<h3> Popular phrases in positive webpages: </h3>", unsafe_allow_html=True)

    st.markdown(
    """
    - "Automatic Python code for spreadsheet operations"
    - "Spreadsheet automation with Mito"
    - "Turn spreadsheets into Python"
    - "Rev up your Python data analysis"
    - "Generate production-ready Python"
    - "Manipulating Pandas DataFrame using Mitosheet"
    - "Add a spreadsheet directly into your activity"
    - "Build elegant data apps with Mito"
    - "Manipulate your data like spreadsheets using Mito"
    - "AI-powered spreadsheet tool"
    """
    )

with col2: 
    st.markdown(f"<h3> Popular phrases in neutral webpages: </h3>", unsafe_allow_html=True)

    st.markdown(
    """
    - "Mito AI is a game changer for Python developers."
    - "Boost your productivity with Mito Spreadsheet."
    - "Mito can help you write Python code faster and more efficiently."
    - "The Mito AI tool is revolutionizing the way we code."
    - "I highly recommend trying out Mito for Python development."
    - "Mito Spreadsheet is a must-have tool for any Python programmer."
    - "With Mito, coding in Python has never been easier."
    - "Mito makes coding in Python 10x faster."
    - "I love the simplicity and power of Mito AI."
    - "Mito is a fantastic tool for speeding up Python development."
    """
    )

with col3: 
    st.markdown(f"<h3> Popular phrases in negative webpages: </h3>", unsafe_allow_html=True)
    st.markdown("No webpages with negative sentiment")

st.write("")

with st.expander("🥳 **Conclusion**"):
    st.write("""
            There are no webpages that display negative sentiment about Mito! 🙌 This is great. Mito users seem to understand the product \
            and write that Mito allows them to turn spreadsheets into Python and build data apps. It seems like this tool is working well \
            for users.
             
            In order to find features that can be improved, we might send out surveys to get direct feedback about our product and run this analysis on those surveys. Currently \
            this analysis does not filter out promotional posts so our results may be skewed toward positive sentiments. People might also be more inclinded  \
            to provide constructive feedback anonymously. 🔮
             """)
    
st.write("")

with st.expander("🧮 **Procedure**"):
    st.write("""
    🔎 **1. Scrape the web for pages mentioning Mito Spreadsheets**: I used the googlesearch Python package to retreive URLs that appear in the Google Search: \"Mito Spreadsheets\"\
    The newspaper package was used to parse the text from these webpages
             
    😁 **2. Analyze Sentiments**: I used the vaderSentiment package to estimate the sentiment of each webpage
             
    📊 **3. Plot Sentiments**: The plot shown on this webpage uses the bokeh package
             
    📝 **4. Get popular phrases**: Using the OpenAI API, I submit a prompt with the parsed webpages and requested that the top phrases contributing to the positive/ neutral/negative\
            sentiments be returned
    """)

