from flask import Flask, render_template, request, jsonify
import requests
import argparse


app = Flask(__name__, template_folder='./Templates')


@app.route('/ping', methods=['GET'])
def ping():
    return "PONG VERSION 1", 200


@app.route('/', methods=['POST', 'GET'])
def calculate():
    budget = ''
    income = ''
    if request.method == 'POST' and 'checking' in request.form and 'housing' in request.form and 'savings' in request.form and 'transportation' in request.form and 'bills' in request.form and 'food' in request.form and 'misc' in request.form:
        c = 0 if len(request.form.get('checking')) == 0 else float(request.form.get('checking'))
        h = 0 if len(request.form.get('housing')) == 0 else float(request.form.get('housing'))
        s = 0 if len(request.form.get('savings')) == 0 else float(request.form.get('savings'))
        t = 0 if len(request.form.get('transportation')) == 0 else float(request.form.get('transportation'))
        b = 0 if len(request.form.get('bills')) == 0 else float(request.form.get('bills'))
        f = 0 if len(request.form.get('food')) == 0 else float(request.form.get('food'))
        m = 0 if len(request.form.get('misc')) == 0 else float(request.form.get('misc'))
        budget = c-(h+s+t+b+f+m)
        income = c
    return render_template('index.html', budget=budget, income=income)


@app.route('/about/')
def about():
    return '<h3>This is a Flask web application intended to work cohesively with a CI/CD pipeline.</h3>'


app.run(debug=False, host='0.0.0.0', port=5000)
