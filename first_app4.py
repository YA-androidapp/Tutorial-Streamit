import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

# option = st.selectbox(
#     'Which number do you like best?',
#      df['first column'])
# 'You selected: ', option

option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['first column'])
'You selected:', option
