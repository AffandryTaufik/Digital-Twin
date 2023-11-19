import streamlit as st 
import pickle   
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from streamlit_elements import elements, mui, html
from streamlit_extras.metric_cards import style_metric_cards 

def load_model():
    model_regr_multirf=pickle.load(open('model_regr_multirf.pkl','rb'))
    return model_regr_multirf
model_regr_multirf = load_model() 

def show_predict_page():
    st.markdown("<h1 style='text-align: center; color: black;'>Static Prediction of the Propylene Glycol Reactor Output</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: black;'> Please input the Reactant Flow below to predict the Flow of Liquid Product, Propylene Glycol Concentration and Flow of Product Gas</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns((1, 1.3, 1))
    
    with col1:
        ReactorLiqPercentLevel = st.number_input("Liquid Percent Level in Reactor [50 - 80 %]", key = "ReactorLiqPercentLevel")
        ReactorProdsTemp = st.number_input("Reactor Temperature [35 - 70 degC]", key = "ReactorProdsTemp")
        ReactorVesselPressure = st.number_input("Reactor Internal Pressure [127 - 131 kPa]", key = "ReactorVesselPressure")
        WaterFeedLiqVolFlow = st.number_input("Water Volume Flow to Reactor [0.5 - 5 m3/h]", key = "WaterFeedLiqVolFlow")
        PropOxideLiqVolFlow = st.number_input("Propylene Oxide Volume Flow to Reactor [0.5 - 3 m3/h]", key = "PropOxideLiqVolFlow")
        MakeUpGasFlow = st.number_input("Nitrogen Flow to Reactor [2 - 2.5 m3/h]", key = "MakeUpGasFlow")
        
        scaler=StandardScaler()
        Target_Value        = [ReactorLiqPercentLevel, ReactorProdsTemp, ReactorVesselPressure, WaterFeedLiqVolFlow, PropOxideLiqVolFlow, MakeUpGasFlow]
    
        Scaled_Target_Value = np.array(Target_Value).reshape(1,-1)
        
        ok=st.button("Calculate Reactor Output")
    
    with col2 :
            st.image('gambarreaktor.jpg',  )    
             
    with col3 :
        if ok:
        #Scaling target value
        #X_test_val = np.array(Scaled_Target_Value)
            
            #Prediction using reg_multirf
            y_multirf_val = model_regr_multirf.predict(Scaled_Target_Value)
            
            test_val_prediction = np.array_split(y_multirf_val[0],3)  #str( )[1:-1]
            
            #Propylene Glycol Prediction
            Propylene_Glycol_Predict = str(test_val_prediction[0]*100)[1:-1]
            #st.subheader(f" The predicted Concentration of Propylene Glycol in Liquid Product is {Propylene_Glycol_Predict} mol/mol")
            
            #Vapor Flow Prediction
            Vapor_Flow_Predict = str(test_val_prediction[1])[1:-1]
            #st.subheader(f" The predicted flow of Vapor product is {Vapor_Flow_Predict} m3/h")
            
            #Liquid Product Flow Prediction
            Liquid_Product_Flow_Predict = str(test_val_prediction[2])[1:-1]
            #st.subheader(f" The predicted flow of Liquid product is {Liquid_Product_Flow_Predict} m3/h")     
            
            pgconc= test_val_prediction[0]*100  
            flowvapor = test_val_prediction[1]
            flowliquid = test_val_prediction[2]
            
            if MakeUpGasFlow == 0 :
                st.metric(label="Flow Nitrogen is Zero, Vapor from reaction neglected", value=0)
            elif MakeUpGasFlow > 0 :
                st.metric(label="The predicted flow of Vapor product in m3/h", value=Vapor_Flow_Predict)

            if WaterFeedLiqVolFlow == 0 and PropOxideLiqVolFlow == 0 :
                st.metric(label="One or two liquid stream is Zero, Concentration is not valid", value=0)
            elif WaterFeedLiqVolFlow > 0 and PropOxideLiqVolFlow > 0 :
                st.metric(label="The Concentration of Prop-Glycol in Liquid Product in x100 mol/mol", value=Propylene_Glycol_Predict)
                
            if WaterFeedLiqVolFlow == 0 and PropOxideLiqVolFlow == 0 :
                st.metric(label="One or two liquid stream is Zero", value=0)
            elif WaterFeedLiqVolFlow > 0 and PropOxideLiqVolFlow > 0 :
                st.metric(label="The predicted flow of Liquid product in m3/h", value=Liquid_Product_Flow_Predict)

            style_metric_cards()


            if  pgconc >= 0.7 :
                st.info('Concentration already on Specification, above 0.7 mol/mol', icon="ℹ️",)
            elif pgconc < 0.7 :
                st.warning('Concentration below Specification, minimum 0.7 mol/mol', icon="⚠️")

            
            if  flowvapor <= 2.7  :
                st.info('Flow Vapor is within acceptable limits', icon="ℹ️",)
            elif flowvapor > 2.7 :
                st.warning('Flow Vapor is too High', icon="⚠️")

                
            
            if  flowliquid <= 15 :
                st.info('Flow Liquid is within acceptable limits', icon="ℹ️",)
            elif flowliquid > 15 :
                st.warning('Flow Liquid is too High', icon="⚠️")

