
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import main

app = Flask(__name__)

@app.route("/sms", methods=['POST', 'GET'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    body = request.values.get('Body')
    print ("Body: " + body)
    answer = main.main(body)
    print ("Answer: " + answer)
    # Start our response
    resp = MessagingResponse()
    # Add a message
    resp.message(answer)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
