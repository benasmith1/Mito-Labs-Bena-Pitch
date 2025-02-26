import streamlit as st


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
    - **Sentiments About TD**: Explore sentiments about TD Bank on the web.
    - **About Bena**: A bit about me!
    """)
st.markdown("<h2>About Me</h2>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 3])  # Adjust ratio as needed

with col1:
    st.image("figures/BenaSmithHeadshot.png", width=200, caption="")

with col2:
    st.write("I am especially excited about automating and streamlining systems with data algorithms. At Gallo Winery, I created a LangChain AI agent to ask questions about Gallo’s wine sales in plain language. \
                The agent writes SQL code and queries the sales database to return an answer. I was asked to return to Gallo as a full-time Associate Data Scientist following this project.\
    ")
    st.write("During my B.S. in Statistics and Data Science with minors in Computer Science and Biology at the University of Arizona, I developed strong coding and data science skills. Seeking a deeper \
                understanding of the theory behind data modeling, I completed an M.S. in Statistics at Cal Poly. I am skilled in time series analysis, generalized linear models, and statistical consulting.")
    
    st.write("I am currently relocating to New York and am excited to put my skills to work!")

with st.expander("🗽 **Portfolio**"):
    st.markdown("<a>https://bena-smith.com/</a>", unsafe_allow_html=True)

