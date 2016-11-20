import os
from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
    print request
    print request.__dict__
    body = request.values.get("Body", None)
    resp = twilio.twiml.Response()
    resp.message("Hello, {}".format(body))
    return str(resp)


@app.route("/mms", methods=['GET', 'POST'])
def hello_monkey_mms():
    """Respond to incoming calls with a simple text message."""
    print request
    print request.__dict__
    resp = twilio.twiml.Response()
    with resp.message("Hello") as m:
        m.media("https://demo.twilio.com/owl.png")
    return str(resp)

if __name__ == "__main__":
     app.debug = True
     port = int(os.environ.get("PORT", 33507))
     app.run(host='0.0.0.0', port=port)
