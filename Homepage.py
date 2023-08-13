import pandas as pd  # pip install pandas openpyxl
import streamlit as st  # pip install streamlit
from pydataset import data


st.set_page_config(page_title= " Excel Plotter")
st.title("Excel Plotter📈")
st.subheader("Feed me with your excel file")

uploaded_file = st.file_uploader("Choose a XLSX file", type="xlsx")

selected_data = st.selectbox("Select a dataset",data().dataset_id)

with st.expander("show list of dataset"):
        st.write(data())

st.subheader(f'Selected data (`{selected_data}`)')
st.write(data(selected_data))

if uploaded_file:
        st.markdown("---")
        df = pd.read_excel(uploaded_file,engine = "openpyxl")
        st.dataframe(df)


# py -m streamlit run Homepage.py