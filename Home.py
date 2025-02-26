#Import necessary libraries
import streamlit as st


st.set_page_config(
    page_title = "Home",
    page_icon = "🌉",
    # layout = "wide"
)

# Sidebar navigation header
with st.sidebar:
    st.header("🔍 Navigate the App")
    st.write("Use the links above to explore:")
    st.markdown("""
    - **Sentiments About TD**: Explore sentiments about TD Bank on the web.
    - **About Bena**: A bit about me!
    """)

# Centered Title using HTML and Markdown
st.markdown(
    """
    <h2 style = "text-align: center; color: #54b946;">TD</h2>
    """,
    unsafe_allow_html = True,
)

col1, col2, col3 = st.columns(3)
with col2:
    st.image("figures/TDLogo.png", caption="TD Logo")


# Subtitle with styling
st.markdown(
    """
    <h4 style = "text-align: center; color: #54b946; font-family: Arial, sans-serif;">
    Showcase for TD Bank!
    </h4>
    """,
    unsafe_allow_html = True,
)

# Insert an image
#st.sidebar.image("Figures/houses_sidebar.jpeg", caption="California Houses")

st.write("My name is Bena Smith. I am a data scientist with an M.S. in statistics. I was so excited about TD after applying, I built this website to showcase a few \
        of my strengths. I performed sentiment analysis on webpages mentioning TD Bank spreadsheets and performed time series analysis on the number of searches.\
        I hope you enjoy my analysis!")



st.sidebar.info("Select a task above to proceed.")

# Interactive introduction with expander
with st.expander("**What can you do with this app?**", expanded=True):
    st.write("""
    😃 **Explore how users feel about TD**: Leveraging sentiment analysis on webpages mentioning TD Bank, we can view the overall opinions of users about this app. Using the OpenAI API, we can find popular phrases in these webpages to see what users like about TD and what can be improved.
    
    🌷 **About Bena**: I give a short synopsis of my interests and link my portfolio.    
    """)


# Add a footer
st.markdown(
    """
    <hr>
    <p style = "text-align: center; color: #777; font-size: 14px; font-family: Arial, sans-serif;">
    Made with ❤️ by Bena Smith.
    </p>
    """,
    unsafe_allow_html = True,
)
