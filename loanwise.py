#streamlit run loanwise.py

import streamlit as st
import requests
import pickle
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
    st.image(logo, caption="", width=220)

# Right column: Display the personal information, left-aligned
with col2:
    st.markdown(
        """
        <div style="text-align: right;">
            <b style="font-size: 28px"> MD. SHAKIL SHEIKH</b>
            <p>Department of CSE, <b>ADUST</b> <br> <b>ID: 213-0001-203</b></p>
            <b style="font-size: 22px"> Project Name:</b>
            <br>
            <p> <b>LoanWise:</b> The Future of Loan Eligibility Verification</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write('---')

#st.title('LoanWise')
st.subheader('Enter Applicant Details:')

#Logo as Header
st.logo("./img/LoanWise-Icon.png")
st.logo(
    "./img/LoanWise-Icon.png",
    size="large",
    link="http://localhost:8501/",
    icon_image="./img/LoanWise-Icon.png"
)




#Load the trained model
file = "loan_predition_model_LR.pkl"
with open(file, 'rb') as f:
    model = pickle.load(f)



#Input things
account_number = st.text_input("Enter Your Account Number")
full_name = st.text_input("Enter Your Full Name")
Gender = st.selectbox("Select Your Gender*", ["Male", "Female"])
Married = st.selectbox("Marital Status: Are You Married?*", ["Yes", "No"])
Dependents = st.selectbox("Number of Dependents (Children/Family Members)*", ["0", "1", "2", "3+"], format_func=lambda x: x.replace("3+", "3 or more"))
Education = st.selectbox("Highest Level of Education Achieved*", ["Graduate", "Not Graduate"])
Self_Employed = st.selectbox("Employment Type: Are You Self-Employed?*", ["Yes", "No"])
ApplicantIncome = st.number_input("Your Annual Income (in $)", min_value=0)
CoapplicantIncome = st.number_input("Co-applicants Annual Income (if any) (in $)", min_value=0.0)
LoanAmount = st.number_input("Requested Loan Amount ($)", min_value=0.0)
Loan_Amount_Term = st.number_input("Loan Repayment Period (Months)", min_value=0.0)
Credit_History = st.selectbox("Credit History (1 = Good, 0 = Poor)*", [0.0, 1.0])
Property_Area = st.selectbox("Choose Property Area Type*", ["Urban", "Rural", "Semiurban"])


# Create a dictionary to map the user-friendly input to numerical values
input_mapping = {
    "Gender": {"Male": 0.0, "Female": 1.0},
    "Married": {"Yes": 0.0, "No": 1.0},
    "Dependents": {"0": 0.0, "1": 1.0, "2": 2.0, "3+": 3.0},
    "Education": {"Graduate": 0.0, "Not Graduate": 1.0},
    "Self_Employed": {"Yes": 0.0, "No": 1.0},
    "Property_Area": {"Urban": 0, "Rural": 1, "Semiurban": 2}
}


# Make prediction
if st.button("Check Your Loan Status", use_container_width=True):
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
        st.subheader(f"Hello, {full_name}")
        st.write(f"Account Number: :blue-background[{account_number}]")
        st.header(":red[We’re sorry!]")
        st.write("Unfortunately, you are not eligible for a loan at this time.")
    else:
        st.subheader(f"Hello, {full_name}")
        st.write(f"Account Number: :blue-background[{account_number}]")
        st.header(":green[Congratulations!!]")
        st.write("Based on our assessment, you meet the loan eligibility criteria.")
        
        
           
st.write('---')
st.write('')     



    
    # Divide the layout into three columns
left_col, middle_col, right_col = st.columns([1, 1, 1])

# Left column: Display your photo
with left_col:
    st.image("./img/ShakilPortrait.jpg", width=120)  # Replace "your_photo.jpg" with the path to your photo
    st.write("&copy; Sheikh Shakil")  # Optional: Display your name below the photo

# Middle column: LinkedIn link
with middle_col:
    st.write("Connect with me on LinkedIn for collaboration & networking.")
    linkedin_url = "https://www.linkedin.com/in/sheikh-shakil/"  # Replace with your LinkedIn profile link
    st.markdown(f"[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)]({linkedin_url})")

# Right column: WhatsApp link
with right_col:
    st.write("Contact me on WhatsApp for any questions or assistance.")
    whatsapp_number = "+8801601122081"  # Replace with your WhatsApp number
    whatsapp_url = f"https://wa.me/+8801601122081"  # Creates a direct link to WhatsApp
    st.markdown(f"[![WhatsApp](https://img.shields.io/badge/WhatsApp-Message-green)]({whatsapp_url})")
        
 
 
 
 # Custom CSS for the footer styling
st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;  /* Light background color */
        color: #333333;  /* Text color */
        text-align: center;
        padding: 10px 0;
        font-size: 14px;
    }
    .footer a {
        color: #0072b1;  /* Link color */
        text-decoration: none;
    }
    .footer a:hover {
        text-decoration: underline;  /* Underline on hover for emphasis */
    }
    </style>
    
    <div class="footer">
        <p>&copy; 2024 <a href="https://www.facebook.com/sheikhshaakil" target="_blank">Sheikh Shakil</a>, All Rights Reserved.</p>
    </div>
    """, unsafe_allow_html=True)