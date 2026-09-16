from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_order():
    # This receives the order data from BigCommerce
    data = request.json
    print("Received order:", data)
    return "Order received!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
