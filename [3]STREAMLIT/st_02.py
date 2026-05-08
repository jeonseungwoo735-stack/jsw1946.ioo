# 소스코드가 입력된 순서대로
# 

import streamlit as st

st.header('st.button')
st.write('버튼을 눌렀을 때, 특정 행동을 하도록 할 수 있습니다.')
st.write('버튼을 눌렀을 때, 특정 행동을 하도록 할 수 있습니다.')
st.write('버튼을 눌렀을 때, 특정 행동을 하도록 할 수 있습니다.')
st.write('버튼을 눌렀을 때, 특정 행동을 하도록 할 수 있습니다.')
st.write(3)

import pandas as pd


if st.button("나를 눌러주세요!"):
    st.write("why hello there")
else:
    st.write("Goodbye")