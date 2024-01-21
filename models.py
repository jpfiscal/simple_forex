from flask import Flask, request, render_template, redirect, jsonify, flash
from forex_python.converter import CurrencyCodes
import requests

access_key = "edc4e90589e946f0939bab7513592994"
currency_code = CurrencyCodes()

class Conversion:
    """Instance of a currency conversion"""
    def __init__(self, cur_from, cur_to, amount):
        """Create conversion instance"""
        self.cur_from = cur_from
        self.cur_to = cur_to
        self.amount = amount

    def verify_cur(self):
        if not self.validate_currencies(self.cur_from):
            return (False, f"{self.cur_from} is not a valid FROM currency")
        elif not self.validate_currencies(self.cur_to):
            return (False, f"{self.cur_to} is not a valid TO currency")
        else:
            return (True, None)
        
    def verify_amt(self):
        try:
            float(self.amount)
            return True
        except ValueError:
            return False

    def convert_currency(self):
        """Use forex converter API to return converted currency"""
        api_url = f"http://api.exchangerate.host/convert?access_key={access_key}&from={self.cur_from}&to={self.cur_to}&amount={self.amount}"
        response = requests.get(api_url)
        symbol = currency_code.get_symbol(self.cur_to.upper())

        if response.status_code == 200:
            data = response.json()
            print(data)
            return f"{symbol}{round(data['result'],2)}"
        else:
            return jsonify({"error": "API Request Failed"}), response.status_code

    def validate_currencies(self, cur):
        """check if a currency code is valid"""
        symbol = currency_code.get_symbol(cur)
        print(f"SYMBOL: {symbol}")
        if symbol == None:
            return False
        return True