import streamlit as st

def app():
    tab1, tab2, tab3 = st.tabs(["📈 Project Flow ","📈 Advantages","📈 Business Model"])

    with tab1:
         c1, c2, c3 = st.columns((1, 5, 1))       
    with c1:
        st.write("")
    with c2: 
        st.image('ppg3.jpg',   use_column_width='never',)     
    with c3:
        st.write("")
        
    with tab2:
        c1, c2, c3 = st.columns((1, 5, 1))       
    with c1:
        st.write("")
    with c2: 
        st.image('advantages of digital twin.jpg',   use_column_width='never',)     
    with c3:
        st.write("")
        
        
    with tab3:
         c1, c2, c3 = st.columns((1, 5, 1))       
    with c1:
        st.write("")
    with c2: 
        st.image('Flow Business.jpg',   use_column_width='never',)     
    with c3:
        st.write("")
        


        
    