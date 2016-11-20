import os

import yaml

from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

def wtw_lookup(tw="encounter.inhaled.mime"):
    wtw = yaml.safe_load(open("./wtw.yaml"))
    return wtw.get(tw)

@app.route("/sms", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
    print request
    print request.__dict__
    three_words = request.values.get("Body", None)
    resp = twilio.twiml.Response()
    resp.message(wtw_lookup(three_words))
    return str(resp)


@app.route("/", methods=['GET', 'POST'])
def hello_monkey_mms():
    """Respond to incoming calls with a simple text message."""
    print request
    print request.__dict__
    three_words = request.values.get("Body", None)
    resp = twilio.twiml.Response()
    three_words = wtw_lookup(three_words)
    resp = twilio.twiml.Response()
    with resp.message(three_words.get("sms")) as m:
        m.media(three_words.get("mms"))
    return str(resp)

if __name__ == "__main__":
     app.debug = True
     port = int(os.environ.get("PORT", 33507))
     app.run(host='0.0.0.0', port=port)
