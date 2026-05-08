import streamlit as st
st.title('st.session_state')
# 1근 = 0.6kg
# 1kg = 1.667근
if 'geun' not in st.session_state:
    st.session_state['geun'] = 0.0
if 'kg' not in st.session_state:
    st.session_state['kg'] = 0.0

def geun_on_change():
    st.session_state['kg'] = st.session_state['geun'] * 0.6

def kg_on_change():
    st.session_state['geun'] = st.session_state['kg'] * 1.667

st.slider(
    "근:",
    min_value=0.0,
    max_value=100.0,
    step=0.1,
    key='geun',
    on_change=geun_on_change
)
st.slider(
    "Kg:",
    min_value=0.0,
    max_value=60.0,
    step=0.1,
    key='kg',
    on_change=kg_on_change
)


