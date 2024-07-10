import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/convert', methods=['GET'])
def convert_currency():
    from_currency = request.args.get('from').lower()
    to_currency = request.args.get('to').lower()

    if not from_currency or not to_currency:
        return jsonify({"error": "Please provide 'from' and 'to' currencies"}), 400

    def fetch_rates(base_url):
        try:
            response = requests.get(base_url)
            response.raise_for_status()
            data = response.json()
            if from_currency not in data:
                raise ValueError(f"Unexpected response format: {data}")
            rates = data[from_currency]
            if to_currency not in rates:
                raise ValueError(f"Invalid currency code: {to_currency}")
            return None, rates[to_currency]
        except (requests.exceptions.RequestException, ValueError) as e:
            return str(e), None

    primary_url = f"https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@1/latest/currencies/{from_currency}.json"
    error, rate = fetch_rates(primary_url)
    
    if rate is None:
        fallback_url = f"https://latest.currency-api.pages.dev/v1/currencies/{from_currency}.json"
        error, rate = fetch_rates(fallback_url)
    
    if rate is None:
        return jsonify({"error": error}), 500

    return jsonify({"rate": rate})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

