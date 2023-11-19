import streamlit as st 
from PIL import Image
# from streamlit_elements import elements, mui
# from streamlit_elements import sync
# from streamlit_elements import lazy

def app():
        #st.title("""""")
        st.markdown("")
        st.markdown("<h1 style='text-align: center; color: black;'>What is Digital Twin ?</h1>", unsafe_allow_html=True)
        st.markdown("")
        st.markdown("<h5 style='text-align: justify; color: black;'>In many daily cases, safe and optimum operating condition is the most favorable concern for Chemical Process Engineers and operators of Chemical Plant and Refinery Operations. A process engineer and an operator should know while operating a Chemical Plant or Refiner should know which parameters can change target product yield and find best operating condition to get maximum production capacity.</h1>", unsafe_allow_html=True)

        st.markdown("<h5 style='text-align: justify; color: black;'>But, Parameter changes in plant is so dynamic, and getting optimum operating condition in dynamic condition is the most challenging thing for Process Engineers and operators. Conduct experimental or trial and errors and trying to getting best operating condition during plant opration by adjusting  is strongly avoided.  Unexpected parameters changes can reduce the target product yield and production capacity. In some cases, some parameter changes can lead to unplanned shutdown can lead to fatal effect of a Chemical Plant or Refinery like blow-up or fire incident. Hence, ensure any parameters in plant at safe and optimum operating condition is not only for achieve safe operting condition but also the best way to achieve the maximum profit. </h1>", unsafe_allow_html=True)

        c1, c2, c3 = st.columns((1, 3, 1))       
        with c1:
                st.write("")
        with c2: 
                st.image('ppg.jpg', )     
        with c3:
                st.write("")
        
        st.markdown("<h6 style='text-align: center; color: black;'>Propylene Glycol Process. </h1>", unsafe_allow_html=True)
                
        st.markdown("<h5 style='text-align: justify; color: black;'>A digital twin is a virtual representation of an object, is updated from real-time data, machine learning and reasoning to help decision making, or in simple virtual model designed to accurately reflect a physical object. By creating Digital Twin Model, which can be imitated/mirroring Chemical Plant and Refinery process, the effect of parameter changes to target product yield and production capacity can figured out. And number of experimental trial and error can be conducted and unexpected scenarios that can be avoided without giving any harm to the real process. </h1>", unsafe_allow_html=True)

        st.markdown("<h5 style='text-align: justify; color: black;'>Futhermore, by connecting realtime parameters data to trained Digital Twin Model, the model not only could predict target product yield and production capacity, but also giving best recommendation  operating condition in realtime to Process Engineers and operators. So they can adjust the parameters to achive optimum target product yield and production capacity.  </h1>", unsafe_allow_html=True)

