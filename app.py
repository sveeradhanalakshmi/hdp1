import pickle
import streamlit as st
import numpy as np
pickle_in=open('hdp.pkl','rb')
clf=pickle.load(pickle_in)

def main():
    html_temp='''
    <div style="background-color:yellow;padding:13px">
    <h1 style="color:black;text-align:center;">CORONARY HEART DETECTION PREDICTION</h1>
    </div>'''

    st.markdown(html_temp,unsafe_allow_html=True)
    age=st.number_input("AGE")
    cpd=st.number_input("CIGARETTES PER DAY")
    tc=st.number_input("TOAL CHOLESTROL")
    sbp=st.number_input('SYSTOLIC')
    dbp=st.number_input('DIASTOLIC')
    bmi=st.number_input('BMI')
    hr=st.number_input('HEART RATE')
    glucose=st.number_input('glucose')
    result=''

    if st.button('PREDICT'):
        result=prediction(age,cpd,tc,sbp,dbp,bmi,hr,glucose)
        st.success('RISK IS {}'.format(result))

def prediction(age,cpd,tc,sbp,dbp,bmi,hr,glucose):
    s=clf.predict([[age,cpd,tc,sbp,dbp,bmi,hr,glucose]])
    if s==1:
        p='HIGH'
    else:
        p='LOW'
    return p

if __name__=='__main__':
    main()




