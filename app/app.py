from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from app.constumer_support_crew import ConstumerSupportCrew

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    body = request.values.get('Body', None)
    crew = ConstumerSupportCrew(body)
    response = crew.run()

    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message(response)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)