from flask import Flask, request, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# Webhook test for main bot
@app.route('/webhook/main', methods=['POST'])
def main_webhook():
    data = request.get_json()
    app.logger.info(f"Received main bot update: {data}")
    return "OK", 200

# Webhook test for reception bot
@app.route('/webhook/admin', methods=['POST'])
def admin_webhook():
    data = request.get_json()
    app.logger.info(f"Received reception bot update: {data}")
    return "OK", 200

@app.route('/')
def home():
    return "✅ BOT Test Running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
