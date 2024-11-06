import dash
from dash import dcc, html, Input, Output
import joblib
import numpy as np

# Load the model saved as a joblib file
file = "loan_prediction_model_LR.joblib"
model = joblib.load(file)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.Div([
        html.H1("Loan Eligibility Checker"),
        
        dcc.Input(id='account-number', type='text', placeholder='Account Number'),
        dcc.Input(id='full-name', type='text', placeholder='Full Name'),

        dcc.Dropdown(id='gender',
                     options=[
                         {'label': 'Male', 'value': 'Male'},
                         {'label': 'Female', 'value': 'Female'}
                     ],
                     placeholder='Select Gender'),

        dcc.Dropdown(id='married',
                     options=[
                         {'label': 'Yes', 'value': 'Yes'},
                         {'label': 'No', 'value': 'No'}
                     ],
                     placeholder='Married?'),

        dcc.Dropdown(id='dependents',
                     options=[
                         {'label': '0', 'value': '0'},
                         {'label': '1', 'value': '1'},
                         {'label': '2', 'value': '2'},
                         {'label': '3 or more', 'value': '3+'}
                     ],
                     placeholder='Dependents'),

        dcc.Dropdown(id='education',
                     options=[
                         {'label': 'Graduate', 'value': 'Graduate'},
                         {'label': 'Not Graduate', 'value': 'Not Graduate'}
                     ],
                     placeholder='Education Level'),

        dcc.Dropdown(id='self-employed',
                     options=[
                         {'label': 'Yes', 'value': 'Yes'},
                         {'label': 'No', 'value': 'No'}
                     ],
                     placeholder='Self Employed?'),

        dcc.Input(id='applicant-income', type='number', placeholder='Applicant Income ($)'),
        dcc.Input(id='coapplicant-income', type='number', placeholder='Coapplicant Income ($)'),
        dcc.Input(id='loan-amount', type='number', placeholder='Loan Amount ($)'),
        dcc.Input(id='loan-amount-term', type='number', placeholder='Loan Amount Term (Months)'),
        
        dcc.Dropdown(id='credit-history',
                     options=[
                         {'label': '0.0', 'value': 0.0},
                         {'label': '1.0', 'value': 1.0}
                     ],
                     placeholder='Credit History'),

        dcc.Dropdown(id='property-area',
                     options=[
                         {'label': 'Urban', 'value': 'Urban'},
                         {'label': 'Rural', 'value': 'Rural'},
                         {'label': 'Semiurban', 'value': 'Semiurban'}
                     ],
                     placeholder='Property Area'),

        html.Button('Check Your Loan Status', id='submit-button', n_clicks=0),
        
        html.Div(id='output-container', children="")
    ], id="app-container")
])

# Define callback to update the output
@app.callback(
    Output('output-container', 'children'),
    Input('submit-button', 'n_clicks'),
    Input('account-number', 'value'),
    Input('full-name', 'value'),
    Input('gender', 'value'),
    Input('married', 'value'),
    Input('dependents', 'value'),
    Input('education', 'value'),
    Input('self-employed', 'value'),
    Input('applicant-income', 'value'),
    Input('coapplicant-income', 'value'),
    Input('loan-amount', 'value'),
    Input('loan-amount-term', 'value'),
    Input('credit-history', 'value'),
    Input('property-area', 'value'),
)
def update_output(n_clicks, account_number, full_name, Gender, Married, Dependents, Education, Self_Employed,
                  ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area):

    if n_clicks > 0:
        input_mapping = {
            "Gender": {"Male": 0.0, "Female": 1.0},
            "Married": {"Yes": 0.0, "No": 1.0},
            "Dependents": {"0": 0.0, "1": 1.0, "2": 2.0, "3+": 3.0},
            "Education": {"Graduate": 0.0, "Not Graduate": 1.0},
            "Self_Employed": {"Yes": 0.0, "No": 1.0},
            "Property_Area": {"Urban": 0, "Rural": 1, "Semiurban": 2}
        }

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

        # Reshape and predict
        input_data = np.array(input_data).reshape(1, -1)
        prediction = model.predict(input_data)[0]

        if prediction == 0:
            return html.Div([
                html.H3(f"Hello, {full_name}", className="result-header result-fail"),
                html.Div(f"Account Number: {account_number}", className="account-number"),
                html.H3("We’re sorry!", className="result-fail"),
                html.P("Unfortunately, you are not eligible for a loan at this time.")
            ])
        else:
            return html.Div([
                html.H3(f"Hello, {full_name}", className="result-header result-success"),
                html.Div(f"Account Number: {account_number}", className="account-number"),
                html.H3("Congratulations!!", className="result-success"),
                html.P("Based on our assessment, you meet the eligibility criteria for a loan.")
            ])
    return ""

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)


