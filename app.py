from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyCodes
from models import Conversion

app = Flask(__name__)
app.config['SECRET_KEY'] = 'so-secret-you-dun-even-kno'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
access_key = "edc4e90589e946f0939bab7513592994"

toolbar = DebugToolbarExtension(app)
currency_code = CurrencyCodes()

@app.route("/")
def index():
    """Redirect to forex conversion form"""

    return redirect('/forex_form')

@app.route("/forex_form")
def load_form():
    """Load Form"""
    return render_template('forex.html')

@app.route("/submit_form", methods=['POST'])
def handle_form_submit():
    """handle currency conversion request via form submit"""
    conversion = Conversion(request.form['convert_from'].upper(), request.form['convert_to'].upper(), request.form['amount'])

    if conversion.verify_cur()[0] == False:
        flash(f"{conversion.verify_cur()[1]}")
        return render_template('forex.html')
    
    if conversion.verify_amt() == False:
        flash("Amount must be a numerical value.")
        return render_template('forex.html')

    return render_template('result.html', result = conversion.convert_currency())
