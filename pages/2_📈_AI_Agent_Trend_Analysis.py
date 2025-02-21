import streamlit as st


st.set_page_config(
    page_title = "AI Agent Trend Analysis",
    page_icon = "🌉",
    layout = "wide"
)

# Sidebar navigation header
with st.sidebar:
    st.header("🔍 Navigate the App")
    st.write("Use the links above to explore:")
    st.markdown("""
    - **Sentiment Analysis**: Explore sentiments about MitoLabs on the web.
    - **AI Agent Trends**: Time series analysis of \"AI agent\" google searches.
    - **About Bena**: A bit about me!
    """)

company = "Mito"
keyword = "Mito Spreadsheets"

col1, col2 = st.columns([0.2, 3.8])  # Adjust ratio as needed


with col1:  
        st.image("figures/Mitochondria.png", use_column_width=True)  # Ensures the image fits within the column width


with col2:  
    st.markdown(f"<h2 style='padding-top: 0;'>AI Agent Trend Analysis</h2>", unsafe_allow_html=True)


st.write(f"The line graph below shows the trends of Google searches for \"AI Agents\" and \"Learn Python\"")
st.write("")
st.image('figures/SearchesoverTime.png', caption="", width=900)

st.write("")
st.write("It appears that searches for \"Learn Python\" have been relatively consistent over time while searches for AI Agents have increased rapidly in the last few years.")

st.write("We can use a Poisson generalized linear model to test if these visual observations are true.")

st.markdown("<h4>Procedure</h4>", unsafe_allow_html=True)
st.write("I used a Poisson GLM because we are examining count data. This model constrains outputs to be > 0 and can account for some of the visual curvature in the searches for \"AI Agents\" because a log link function is used.")
st.write("Because this is time series data, there may be leftover autocorrelation between residuals after modeling with the Poisson GLM. This means that knowing the value at one time point may give you information about the value at the next time point. \
        This violates the regression assumption of independent observations and leads to potentially inacurrate standard errors and pvalues. To account for this, I applied the Newey-West estimator which accounts for this autocorrelation when estimating standard errors.")

st.write("Our residuals are pictured below with autocorrelation functions and partial autocorrelation functions so we can examine if thisstandard error adjustment is necessary")
st.write("")
st.write("")

st.image('figures/SearchesoverTimeResiduals.png', caption="", width=850)

st.write("")
st.write("We see geometric decay in our ACFs and spikes after lag 1 in our PACFs, indicating there is autocorrelation in our residuals. So, we apply the Newey West adjustment to our model. This does not change the coefficients of our model, only the standard errors and p values")
st.write("")

st.markdown("<h4>Results</h4>", unsafe_allow_html=True)
st.write("The Poisson GLM is shown below. Observed values are marked with dots and values estimated by our model are marked as a line.")
st.write("")
st.image('figures/SearchesoverTimeModel.png', caption="", width=900)

st.write("")
st.write("")

st.write("Our model coefficients and metrics are shown below.")

st.image('figures/SearchesOverTimeModelCoefs.png', caption="", width=500)

st.write("The p value for the coefficient of week is 0. This means that there is no evidence that the search interest for \"Learn Python\" has increased from 2020 to 2025.")
st.write("Conversely, the interaction between week and \"AI Agents\" is statistically significant with a positive coefficient, providing evidence that there has been more of an increase in search interest for \"AI Agents\" than \"Learn Python\" from 2020 to 2025.")

st.markdown("<h4>Conclusion</h4>", unsafe_allow_html=True)
st.write("Mito AI is a relevant application because there has not been an increase in interest about learning Python over time, so users may use Mito AI for Python data manipulation. AI agents are also becoming more popular, showing that Mito AI is a relevant and innovative tool.")


st.markdown("<h4>Data</h4>", unsafe_allow_html=True)

st.write("Data was sourced from Google Trends https://trends.google.com/trends/explore?date=today%205-y&geo=US&q=ai%20agent,learn%20python&hl=en")
st.write("Search interest numbers represent search interest relative to the highest point on the chart for the given region and time. A value of 100 is the peak popularity for the term. A value of 50 means that the term is half as popular. A score of 0 means there was not enough data for this term.")
