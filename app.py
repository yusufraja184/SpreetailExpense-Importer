import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Spreetail Expense Importer",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Spreetail Expense Importer")

uploaded_file = st.file_uploader(
    "Upload Expense CSV",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.header("Dataset Overview")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    st.subheader("Dataset Preview")
    st.dataframe(df)

    st.subheader("Missing Values")

    missing_values = pd.DataFrame({
        "Column": df.columns,
        "Missing Count": df.isnull().sum().values
    })

    st.dataframe(missing_values)

    st.subheader("Anomaly Report")

    anomalies = []

    for index, row in df[df["paid_by"].isnull()].iterrows():
        anomalies.append(
            f"ERROR | Row {index+1} | Missing paid_by | {row['description']}"
        )

    for index, row in df[df["currency"].isnull()].iterrows():
        anomalies.append(
            f"WARNING | Row {index+1} | Missing currency | {row['description']}"
        )

    for index, row in df[df["split_type"].isnull()].iterrows():
        anomalies.append(
            f"WARNING | Row {index+1} | Missing split_type | {row['description']}"
        )

    if anomalies:
        for anomaly in anomalies:
            st.warning(anomaly)
    else:
        st.success("No anomalies detected")

    st.subheader("Import Report")

    report_text = "\n".join(anomalies)

    st.download_button(
        label="Download Import Report",
        data=report_text,
        file_name="import_report.txt",
        mime="text/plain"
    )