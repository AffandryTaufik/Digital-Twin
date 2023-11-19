import pandas as pd
import pandas_profiling
import streamlit as st
import numpy as np
from streamlit_pandas_profiling import st_profile_report

def app():
        header = st.container()
        with header:
            st.markdown("<h2 style='text-align: center; color: black;'>Data Profile</h1>", unsafe_allow_html=True)

        df = pd.read_csv("targetandvariabledata.csv")
        pr = df.profile_report()

        st_profile_report(pr)