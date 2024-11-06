# LoanWise: Loan Eligibility Prediction App

LoanWise is a streamlined web app that predicts an applicant's loan eligibility based on provided financial and personal details. The app leverages machine learning to analyze multiple parameters, ensuring accurate and reliable loan eligibility assessments.

![LoanWise-Logo](https://github.com/user-attachments/assets/89cdc472-6a10-4918-b972-c04cfc149e58)


## Features:-
- User-Friendly Interface: Designed for ease of use with clear instructions and tooltips.
- Data-Driven Predictions: Uses machine learning to evaluate loan eligibility accurately.
- Streamlined Process: Supports various input fields like Applicant Income, Loan Amount, and more.
- Accessible Contact Options: Quick links to connect via LinkedIn and WhatsApp for assistance.


## Technologies Used
*Python
*Streamlit for web app framework
*scikit-learn and joblib for model training and persistence
*NumPy and Pandas for data manipulation
*CSS and HTML for styling

## Getting Started
- Prerequisites
- Ensure you have the following installed:

Python 3.11+
Required Python packages (see requirements.txt)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/loanwise.git
Navigate to the project directory:

bash
Copy code
cd loanwise
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Running the Application
To launch the app locally:

bash
Copy code
streamlit run app.py


Usage
Input Applicant Information:
Enter fields such as Gender, Married Status, Income, and Loan Amount.
Submit for Prediction:
Click on "Check Your Loan Status" to receive the prediction.
View Prediction Output:
Displays whether the applicant is eligible or not, with a detailed message.
Screenshot Examples
Main Interface


Loan Eligibility Prediction Output


Model and Prediction Details
The machine learning model (logistic regression) was trained on [dataset details] with a high accuracy score.
The model is loaded using joblib, ensuring consistent performance in the cloud or local environments.

Contact Information
For any inquiries or support, feel free to connect:
LinkedIn: Your LinkedIn Profile
WhatsApp: +Your-Number

License
This project is licensed under the MIT License.
