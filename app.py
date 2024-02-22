import streamlit as st
import joblib

st.title("food expiation prediction")

inp1=st.text_input("Oil composition present in the food")
inp2=st.text_input("salt percentage dont include percentage")
inp3=st.text_input("salt composition according to food")
inp4=st.text_input("chemical composition percentage dont include percentage symbol at last")

if st.button('Predict'):
    # st.write('Why hello there')
    model=joblib.load("model_regression")
    res=model.predict([[int(inp1),int(inp2),int(inp3),int(inp4)]])
    st.balloons()
    st.success(res)
else:
    st.write('Please Enter valid input')
