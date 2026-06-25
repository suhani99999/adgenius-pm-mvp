import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="AdGenius AI", layout="wide")
st.title("🎯 AdGenius AI - Product Management Case Study")

tab1, tab2 = st.tabs(["✨ AI Copy Generator", "📊 Performance Analytics"])
with tab1:
    st.subheader("Generate Marketing Copy")
    product = st.text_input("Product Name", "EcoClean Smart Bottle")
    if st.button("Generate"):
        st.success(f"Ad Copy for {product}: 'Experience the future of hydration with {product}. Built for the modern nomad!'")

with tab2:
    st.subheader("Simulated CTR Trends")
    data = pd.DataFrame({'Year': [2022, 2024, 2026], 'Adoption': [10, 15, 45]})
    fig = px.area(data, x='Year', y='Adoption', title="Rapid SaaS Adoption Across Ad-Tech")
    st.plotly_chart(fig, use_container_width=True)
