#streamlit run LoanWise_app.py

import streamlit as st
import requests
import pickle
from streamlit_lottie import st_lottie
import joblib
import numpy as np
from PIL import Image


#Logo as Fevicon
image = Image.open('./img/LoanWise-Icon.png')
st.set_page_config(page_title='LoanWise - Verify Eligibility with Confidence', page_icon=image)

#Header Logo and Info
logo = Image.open("img/LoanWise-Logo.png")

# Create two columns
col1, col2 = st.columns([1, 2])

# Left column: Display the logo
with col1:
    st.image(logo, caption="", width=200)

# Right column: Display the personal information, left-aligned
with col2:
    st.markdown(
        """
        <div style="text-align: right;">
            <b style="font-size: 30px"> Md. Shakil Sheikh</b>
            <p>Department of CSE, ADUST</p>
            <p>ID: 213-0001-203</p>
        </div>
        """,
        unsafe_allow_html=True
    )


st.write('---')

#st.title('LoanWise')
st.subheader('Enter Applicant Details:')

# For Animations

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()




lottie_link = "https://assets8.lottiefiles.com/packages/lf20_4wDd2K.json"
animation = load_lottie(lottie_link)
animation_contact = load_lottie("https://assets4.lottiefiles.com/packages/lf20_mwawjro9.json")





# Load the trained model
file = "loan_predition_model_LR.pkl"
with open(file, 'rb') as f:
    model = pickle.load(f)


#Logo as Header
st.logo("./img/LoanWise-Icon.png")
st.logo(
    "./img/LoanWise-Icon.png",
    size="large",
    link="http://localhost:8501/",
    icon_image="./img/LoanWise-Icon.png"
)

#Input things

account_number = st.text_input("Account Number")
full_name = st.text_input("Full Name")
Gender = st.selectbox("Gender", ["Male", "Female"])
Married = st.selectbox("Married", ["Yes", "No"])
Dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"], format_func=lambda x: x.replace("3+", "3 or more"))
Education = st.selectbox("Education", ["Graduate", "Not Graduate"])
Self_Employed = st.selectbox("Self_Employed", ["Yes", "No"])
ApplicantIncome = st.number_input("ApplicantIncome($)", min_value=0)
CoapplicantIncome = st.number_input("CoapplicantIncome($)", min_value=0.0)
LoanAmount = st.number_input("LoanAmount($)", min_value=0.0)
Loan_Amount_Term = st.number_input("Loan Amount Term(Month)", min_value=0.0)
Credit_History = st.selectbox("Credit_History*", [0.0, 1.0])
Property_Area = st.selectbox("Property_Area", ["Urban", "Rural", "Semiurban"])


# Create a dictionary to map the user-friendly input to numerical values
input_mapping = {
    "Gender": {"Male": 0.0, "Female": 1.0},
    "Married": {"Yes": 0.0, "No": 1.0},
    "Dependents": {"0": 0.0, "1": 1.0, "2": 2.0, "3 or more": 3.0},
    "Education": {"Graduate": 0.0, "Not Graduate": 1.0},
    "Self_Employed": {"Yes": 0.0, "No": 1.0},
    "Property_Area": {"Urban": 0, "Rural": 1, "Semiurban": 2}
}


# Make prediction
if st.button("Predict"):
    # Convert user inputs to numerical values using the mapping
    input_data = [
        input_mapping["Gender"][Gender],
        input_mapping["Married"][Married],
        input_mapping["Dependents"][Dependents],
        input_mapping["Education"][Education],
        input_mapping["Self_Employed"][Self_Employed],
        ApplicantIncome,
        CoapplicantIncome,
        LoanAmount,
        Loan_Amount_Term,
        Credit_History,
        input_mapping["Property_Area"][Property_Area]        
    ]

    input_data = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_data)[0]
    
    
    if prediction == 0:
        st.write(f"Hello {full_name} and account number: {account_number}")
        st.write("Loan Prediction: Rejected")
    else:
        st.write(f"Hello {full_name} and account number: {account_number}")
        st.write("Loan Prediction: Approved")
        
        
        
        
        
        
st.write('---')
st.write('')       

with st.container():
    right_column, left_column = st.columns(2)
    with right_column:

        st.write('_For any issue contact me via :_')
        st.info('[LinkedIn](https://www.linkedin.com/in/sheikh-shakil/)', icon="📩")
        st.info('[Whatsapp](https://wa.me/+8801601122081)', icon="📲")

    with left_column:
        st_lottie(animation_contact, speed=1, height=200, key="third")  
        
        
        
        
        
        
        
        
        
        
        
        
footer="""<style>
header {visibility: hidden;}

/* Light mode styles */
p {
  color: black;
}

/* Dark mode styles */
@media (prefers-color-scheme: dark) {
  p {
    color: white;
  }
}

a:link , a:visited{
color: #5C5CFF;
background-color: transparent;
text-decoration: none;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

:root {
  --footer-bg-color: #333;
}

@media (prefers-color-scheme: dark) {
  :root {
    --footer-bg-color: rgb(14, 17, 23);
  }
}

@media (prefers-color-scheme: light) {
  :root {
    --footer-bg-color: white;
  }
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: var(--footer-bg-color);
color: black;
text-align: center;
}

</style>
<div class="footer">
<p>&copy; 2024 <a href="https://www.facebook.com/sheikhshaakil"> Sheikh Shakil,</a> All Rights Reserved.</p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)