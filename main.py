import streamlit as st

from streamlit_option_menu import option_menu

import about, overview, home, realtimedemo, staticprediction, howto, business
st.set_page_config(
    page_title="Digital-Twin",layout="wide"
)

class Multiapp:
    
    def __int__(self):
        self.apps = []
    def add_app(self,title,function):
        self.app.append({
            "title"     : title,
            "function"  : function
        })

    def run() :

        app = option_menu(None, 
                        ['Home','Business Overview','Data Overview','How to','Real-Time Optimization','Static Prediction','about'], 
            icons=['house-fill','bi-buildings-fill','database','question-diamond-fill','pc-display-horizontal','display','person-circle'], 
            menu_icon="cast", default_index=0, orientation="horizontal")
    
        
        if app == "Home":
            home.app()
        if app == "Business Overview":
            business.app()  
        if app == "Data Overview":
            overview.app()    
        if app == "Real-Time Optimization":
            realtimedemo.app()
        if app == "How to":
            howto.app()         
        if app == 'Static Prediction':
            staticprediction.show_predict_page()
        if app == 'about':
            about.app()    
             
    run() 