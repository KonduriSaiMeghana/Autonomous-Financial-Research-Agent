import streamlit as st

from financial_agent import FinancialResearchAgent

st.set_page_config(
    page_title="AI Financial Research Agent",
    page_icon="📈",
    layout="wide"
)

st.title("📈 AI Financial Research Agent")

st.write(
    "Generate professional investment research reports using AI Agents."
)

ticker = st.text_input(
    "Company Ticker",
    placeholder="MSFT"
)

query = st.text_area(
    "Research Query",
    placeholder="Analyze Microsoft as an investment."
)

if st.button("Generate Report"):

    if ticker == "":
        st.warning("Please enter a company ticker.")
        st.stop()

    if query == "":
        query = f"Analyze {ticker} as an investment."

    agent = FinancialResearchAgent()

    with st.spinner("Researching company..."):

        report = agent.run(
            ticker.upper(),
            query
        )

    st.success("Report Generated!")

    st.markdown(report)