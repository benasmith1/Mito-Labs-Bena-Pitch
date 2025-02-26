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
    - **Sentiments About TD**: Explore sentiments about TD Bank on the web.
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
        height: 55px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class="container">
        <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open("figures/TDLogo.png", "rb").read()).decode()}">
        <h2 class="logo-text">&nbsp; Sentiments About TD</h2>
    </div>
    """,
    unsafe_allow_html=True
)

st.write(f"The bar graph below shows the distribution of sentiments of webpages mentioning TD Bank. Click on a bar to view each link.")

with open('figures/SentimentsGraph.html', 'r', encoding='utf-8') as file:
    sentiment_graph_data = file.read()


st.components.v1.html(sentiment_graph_data, height=650, width=1500)


col1, col2, col3 = st.columns([1, 1, 1])  

with col1: 
    st.markdown(f"<h3> Popular phrases in positive webpages: </h3>", unsafe_allow_html=True)

    st.markdown(
    """
    - "TD Bank has great customer service."
    - "I love the convenience of TD Bank's mobile banking app."
    - "TD Bank offers competitive interest rates."
    - "I have had a positive experience with TD Bank's mortgage services."
    - "TD Bank has a user-friendly website."
    - "TD Bank's savings accounts are a great option for growing your money."
    - "I trust TD Bank with my financial needs."
    - "TD Bank's credit cards have excellent rewards programs."
    - "TD Bank provides a wide range of financial products."
    - "TD Bank is a reliable and trustworthy bank."
    """
    )

with col2: 
    st.markdown(f"<h3> Popular phrases in neutral webpages: </h3>", unsafe_allow_html=True)

    st.markdown(
    """
    - "TD Bank offers a variety of financial products and services to meet your banking needs."
    - "Customers appreciate TD Bank's user-friendly online banking platform."
    - "TD Bank has a strong presence in the community and supports local initiatives."
    - "Many customers find TD Bank's customer service to be reliable and helpful."
    - "TD Bank's mobile app is convenient and easy to use for banking on the go."
    - "TD Bank has competitive interest rates on savings accounts and CDs."
    - "Customers value TD Bank's commitment to security and fraud protection."
    - "TD Bank has a wide network of ATMs for convenient access to cash."
    - "TD Bank's mortgage and lending options are flexible and cater to individual needs."
    - "TD Bank's fees are transparent and reasonable compared to other banks."
    """
    )

with col3: 
    st.markdown(f"<h3> Popular phrases in negative webpages: </h3>", unsafe_allow_html=True)
    st.markdown("""
    - "Terrible customer service"
    - "Unprofessional staff"
    - "Hidden fees"
    - "Poor communication"
    - "High account maintenance fees"
    - "Unreliable online banking system"
    - "Long wait times"
    - "Lack of transparency"
    - "Incompetent management"
    - "Difficulty resolving issues"
    """)

st.write("")

with st.expander("🥳 **Conclusion**"):
    st.write("""
    Most webpages express positive sentiments about TD Bank and write about the convenient mobile app and website. Customers also write about the trust and security
    that TD provides. The negative articles reference hidden fees and a lack of transparency. To examine this issues more carefully, we might send out surveys to get direct 
    feedback about our product and run this analysis on those surveys. People might be more inclinded to include more detailed descriptions of potential feature fixes and hidden 
    fees anonymously. 🔮
""")
    
st.write("")

with st.expander("🧮 **Procedure**"):
    st.write("""
    🔎 **1. Scrape the web for pages mentioning TD Bank**: I used the googlesearch Python package to retreive URLs that appear in the Google Search: \"TD Bank Opinions\"\
    The newspaper package was used to parse the text from these webpages
             
    😁 **2. Analyze Sentiments**: I used the vaderSentiment package to estimate the sentiment of each webpage
             
    📊 **3. Plot Sentiments**: The plot shown on this webpage uses the bokeh package
             
    📝 **4. Get popular phrases**: Using the OpenAI API, I submit a prompt with the parsed webpages and requested that the top phrases contributing to the positive/ neutral/negative\
            sentiments be returned
    """)

st.write("")

with st.expander("🦋 **Future Use Cases**"):
    st.write("""A similar algorithm to this application may be used to create financial portfolios for clients. We can identify companies with mostly positive sentiments to include in 
            these portfolios. We can also observe certain markets in a similar way. If we are interested in how customers like a specific TD product, we may analyze that product with this procedure.""")