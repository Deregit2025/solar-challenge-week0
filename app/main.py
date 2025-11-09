import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(page_title="Solar Data Dashboard", layout="wide")

st.title("Solar Data EDA Dashboard")
st.write("Upload your cleaned CSV file for any country to visualize EDA results.")

# File uploader widget
uploaded_file = st.file_uploader("📤 Upload a cleaned CSV file (e.g., cleaned_data_benin.csv)", type=["csv"])

# Check if user uploaded a file
if uploaded_file is not None:
    # Read data
    df = pd.read_csv(uploaded_file)
    st.success("File successfully uploaded!")
    
    # Preview data
    st.subheader("Data Preview")
    st.dataframe(df.head())

    # Convert Timestamp column to datetime
    if "Timestamp" in df.columns:
        df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")
        df["Month"] = df["Timestamp"].dt.month_name()

    # Select plot type
    st.subheader("Plot Options")
    plot_type = st.selectbox("Choose a plot type:", ["Line Chart", "Boxplot", "Scatter Plot"])

    # Draw selected plot
    st.subheader("Visualization")

    if plot_type == "Line Chart":
        columns_to_plot = st.multiselect("Select variables to plot vs Timestamp:", 
                                         [col for col in df.columns if col not in ["Timestamp"]])
        if columns_to_plot:
            fig, ax = plt.subplots(figsize=(10, 5))
            for col in columns_to_plot:
                ax.plot(df["Timestamp"], df[col], label=col)
            ax.legend()
            ax.set_xlabel("Timestamp")
            ax.set_ylabel("Value")
            st.pyplot(fig)

    elif plot_type == "Boxplot":
        num_cols = df.select_dtypes(include="number").columns.tolist()
        col_choice = st.selectbox("Select numeric column for Boxplot:", num_cols)
        if col_choice:
            fig, ax = plt.subplots()
            sns.boxplot(data=df, y=col_choice, ax=ax)
            st.pyplot(fig)

    elif plot_type == "Scatter Plot":
        if "GHI" in df.columns and "Tamb" in df.columns:
            fig, ax = plt.subplots()
            sns.scatterplot(data=df, x="Tamb", y="GHI", hue="Month", ax=ax)
            st.pyplot(fig)
        else:
            st.warning("Columns 'Tamb' or 'GHI' not found in uploaded data.")
else:
    st.info("Please upload a cleaned CSV file to begin.")
