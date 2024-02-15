import streamlit as st
import pandas as pd
from io import BytesIO


st.title("Exclusion")

sheet = st.text_input("Type the sheet name:")
if sheet is not None:
    st.write("sheet name is: ", sheet)



df = st.file_uploader("Choose a file to upload:", type=["xlsx"])
if df is not None:
    df1 = pd.read_excel(df, sheet_name=sheet, header=None)
    st.write(df1)



    #Operation
    # Select rows where value in column1 is not in column2
    filtered_df = df1[~df1[0].isin(df1[1])]


    filtered_df = filtered_df.drop(filtered_df.columns[1:], axis=1)

    # Print the result
    st.write(len(filtered_df), "Entries")    

    st.write(filtered_df)



    csv_string = filtered_df.to_csv(index=False, header=None)
    csv_bytes = csv_string.encode()


    st.download_button(
        label="Download data",
        data=csv_bytes,
        file_name="data.csv",
        mime="text/csv"
    )