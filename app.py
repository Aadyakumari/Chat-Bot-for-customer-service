from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get_response', methods=['GET'])
def get_response():
    user_msg = request.args.get('msg')  # get user input

    # SIMPLE RULE-BASED LOGIC
    user_msg = user_msg.lower()

    if "refund" in user_msg:
        reply = "Please provide your order ID to initiate a refund."
    elif "return" in user_msg:
        reply = "You can return the product within 7 days of delivery."
    elif "order" in user_msg:
        reply = "Can you please share your order number?"
    elif "hello" in user_msg or "hi" in user_msg:
        reply = "Hello! How can I assist you today?"
    else:
        reply = "Sorry, I didn’t understand that. Could you please rephrase?"

    return jsonify({"response": reply})

if __name__ == '__main__':
    app.run(debug=True)
