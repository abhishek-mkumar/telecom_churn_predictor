from flask import Flask, render_template, request
import numpy as np
import pickle

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def predict_churn():
    result = None
    if request.method == 'POST':
        tenure = request.form.get('Tenure')
        monthly_charges = request.form.get('Monthly Charges')
        total_charges = request.form.get('Total Charges')
        gender = request.form.get('Gender')
        senior_citizen = request.form.get('Senior Citizen')
        partner = request.form.get('Partner')
        phone_service = request.form.get('Phone Service')
        multiple_lines = request.form.get('Multiple Lines')
        fiber_optic = request.form.get('Fiber Optic')
        online_security = request.form.get('Online Security')
        online_backup = request.form.get('Online Backup')
        device_protection = request.form.get('Device Protection')
        tech_support = request.form.get('Tech Support')
        tv = request.form.get('TV Streaming')
        movie = request.form.get('Movie Streaming')
        paperless_billing = request.form.get('Paperless Billing')
        internet_service = request.form.get('Internet Service')

        if request.form.get('Contract') == 'one_year':
            one_year_contract = 1
            two_year_contract = 0
        elif request.form.get('Contract') == 'two_year':
            one_year_contract = 0
            two_year_contract = 1
        else:
            one_year_contract = 0
            two_year_contract = 0

        if request.form.get('Payment Method') == 'credit_card':
            credit_card = 1
            electronic_check = 0
            mailed_check = 0
        elif request.form.get('Payment Method') == 'electronic_check':
            credit_card = 0
            electronic_check = 1
            mailed_check = 0
        elif request.form.get('Payment Method') == 'mailed_check':
            credit_card = 0
            electronic_check = 1
            mailed_check = 0
        else:
            credit_card = 0
            electronic_check = 0
            mailed_check = 0

        result = model.predict(np.array([tenure, monthly_charges, total_charges, gender, senior_citizen, partner, phone_service, multiple_lines, fiber_optic, online_security, online_backup, device_protection, tech_support, tv, movie, one_year_contract, two_year_contract, paperless_billing, credit_card, electronic_check, mailed_check, internet_service]).reshape(1, -1))

        if result == 1:
            result = "Your customer will churn"
        else:
            result = "Your customer will not churn"

    return render_template('churn_predictor.html', result=result)

@app.route("/data-overview")
def data_overview():
    return render_template('data_overview.html')

@app.route("/how-it-works")
def how_it_works():
    return render_template('how_it_works.html')

if __name__ == '__main__':
    app.run(debug=True)
