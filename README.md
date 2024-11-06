

![LoanWise-Logo](https://github.com/user-attachments/assets/7111a41b-9977-4488-8d96-4519a99d4c7f)
# **LoanWise:** The Future of Loan Eligibility Verification
LoanWise is a streamlined web app that predicts an applicant's loan eligibility based on provided financial and personal details. The app leverages machine learning to analyze multiple parameters, ensuring accurate and reliable loan eligibility assessments.

## Features:-
- **User-Friendly Interface:** Designed for ease of use with clear instructions and tooltips.
- **Data-Driven Predictions:** Uses machine learning to evaluate loan eligibility accurately.
- **Streamlined Process:** Supports various input fields like Applicant Income, Loan Amount, and more.
- **Accessible Contact Options:** Quick links to connect via LinkedIn and WhatsApp for assistance.


## Technologies Used
- Python
- Streamlit for web app framework
- scikit-learn and joblib for model training and persistence
- NumPy and Pandas for data manipulation
- CSS and HTML for styling

## Getting Started
**Prerequisites**
Ensure you have the following installed:
- Python 3.11+
- Required Python packages (see requirements.txt)

**Installation**
1. Clone the repository:
 ```
git clone https://github.com/yourusername/loanwise.git
 ```

2. Navigate to the project directory:
```
cd LoanWise-Prediction_App
```

3. Install dependencies:
```
pip install -r requirements.txt
```


## Running the Application

**To launch the app locally:**
```
streamlit run loanwise.py
```

## Usage

1 **Input Applicant Information:**
- Enter fields such as Gender, Married Status, Income, and Loan Amount.

2. **Submit for Prediction:**
- Click on "Check Your Loan Status" to receive the prediction.

3. **View Prediction Output:**
- Displays whether the applicant is eligible or not, with a detailed message.


## Screenshot Examples

1. Main Interface
![image](https://github.com/user-attachments/assets/bd92891c-4583-4a45-8449-b896d58b60c3)

2. Loan Eligibility Prediction Output
![image](https://github.com/user-attachments/assets/e5228204-7720-4209-819b-68b4444c0995)

## Model and Prediction Details
- Model Type: The loan eligibility prediction is powered by a **Logistic Regression** model.
- Model File: The model is saved as a `.pkl` file (`loan_prediction_model_LR.pkl`) and loaded into the app at runtime using Python’s `pickle` library.
- Dataset: Trained on a loan application dataset, achieving high accuracy on test data.

## Contact Information
For any inquiries or support, feel free to connect:

- LinkedIn: https://www.linkedin.com/in/sheikh-shakil/
- WhatsApp: https://wa.me/+8801601122081

## License
This project is licensed under the **MIT License.**
