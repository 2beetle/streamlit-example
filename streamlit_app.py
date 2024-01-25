import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder

if "rerun" not in st.session_state:
    st.session_state.rerun = True
    st.rerun()

file = st.experimental_get_query_params().get('file')

# df = pd.read_csv('https://test-aliyun8203292432-beijing.oss-cn-beijing.aliyuncs.com/test/data/warehouse_genotype_snp_csv_sample-col_batch_PMBD2023080733P01%20%282%29.csv')
df = pd.read_excel(file[0])
builder = GridOptionsBuilder.from_dataframe(df)
builder.configure_pagination(paginationPageSize=20, paginationAutoPageSize=False)
go = builder.build()
with st.container():
    AgGrid(df, gridOptions=go)
