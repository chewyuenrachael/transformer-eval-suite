# dashboard.py

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Transformer Eval Suite", layout="wide")

st.title("🧠 Transformer Evaluation Suite")
st.markdown("Compare transformer models across metrics, prompts, and generations.")

# Load Data
CSV_PATH = "results/summarization-comparison/results.csv"
df = pd.read_csv(CSV_PATH)

# Sidebar filters
st.sidebar.header("🔍 Filter Options")

models = df["Model"].unique()
selected_models = st.sidebar.multiselect("Select Models", models, default=models)

prompts = sorted(df["Prompt"].unique())
selected_prompts = st.sidebar.multiselect("Select Prompt Variants", prompts, default=prompts)

metrics = ["BLEU", "ROUGE-1", "ROUGE-L", "Cosine Sim"]
selected_metric = st.sidebar.selectbox("Select Metric to Visualize", metrics)

# Filtered data
filtered_df = df[df["Model"].isin(selected_models) & df["Prompt"].isin(selected_prompts)]

# Plot
st.subheader(f"📊 {selected_metric} by Model and Prompt")
fig = px.bar(
    filtered_df,
    x="Model",
    y=selected_metric,
    color="Prompt",
    barmode="group",
    hover_data=["Latency", "Num Tokens", "Output"],
    template="plotly_white",
    height=500
)
st.plotly_chart(fig, use_container_width=True)

# Table
st.subheader("📄 Generated Outputs Table")
st.dataframe(filtered_df[["Model", "Prompt", selected_metric, "Latency", "Num Tokens", "Output"]])

# Export
st.download_button("📥 Download Filtered CSV", filtered_df.to_csv(index=False), file_name="filtered_results.csv")
