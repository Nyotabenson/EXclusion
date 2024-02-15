import streamlit as st
import pandas as pd
from io import BytesIO


#st.title("Exclusion")
st.image("HEADER.png", caption=".", use_column_width=True)
st.subheader("Exclusion")
st.write("""Exclusion is an advanced program designed to streamline data management by effectively filtering out redundant entries
          from one column based on the information present in another column. By employing this tool, users can obtain a comprehensive and
            reliable overview of the unique values inherent in their dataset.

The functionality of Exclusion primarily revolves around a dual-column approach, wherein it meticulously identifies 
entries in column B that also exist in column A. What sets this program apart is its ability to automatically eliminate 
these redundant values, thereby leaving users with a refined set of unique data points. This streamlined dataset often contains
 valuable insights into previously overlooked or unattended values,
 enhancing the depth and accuracy of data analysis.""")

st.write("---")
st.subheader("Exclusion Program")
st.write("##")
st.write("- Utilize a dataset formatted in Excel with the extension '.xlsx'.")
st.write("- The two features should be side by side.")

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
    st.write(len(filtered_df), "Uniques Entries")    

    st.write(filtered_df)



    csv_string = filtered_df.to_csv(index=False, header=None)
    csv_bytes = csv_string.encode()


    st.download_button(
        label="Download data",
        data=csv_bytes,
        file_name="data.csv",
        mime="text/csv"
    )