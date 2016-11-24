import os
import httplib
import json

import yaml

from flask import Flask, request, redirect
import twilio.twiml

API_KEY = "AJO8AO39"

app = Flask(__name__)

def latlon2wtw(blob):
    """
    """
    print "Entering latlon2wtw..."
    parts = blob.split("=")
    lat,lon = parts[1].split(",")
    print "lat: {}, lon: {}".format(lat,lon)
    # get three words with Lat Lon
    conn = httplib.HTTPSConnection("api.what3words.com")
    print conn
    request_url = "https://api.what3words.com/v2/reverse?coords=" + \
                 "{lat}%2C{lon}".format(lat=lat,lon=lon) + \
                 "&key={api_key}".format(api_key=API_KEY) + \
                 "&lang=en&format=json&display=full"

    print "request_url: {}".format(request_url)

    conn.request("GET", request_url)
    print conn
    res = conn.getresponse()
    print res
    data_str = res.read()
    print "data_str: {}".format(data_str)
    j = json.loads(data_str)
    print j
    words = j.get("words")
    return words

def wtw_lookup(tw="encounter.inhaled.mime"):
    wtw = yaml.safe_load(open("./wtw.yaml"))
    return wtw.get(tw)

def guess_format(blob):
    print "Starting guess_format..."
    print "blob: {}".format(blob)
    if "https://maps.google.com/maps?q=" in blob:
        print "before calling latlon2wtw..."
        words = latlon2wtw(blob)
        print "words: {}".format(words)
        return words
    # TODO: more guesses here
    return wtw_lookup(blob)


@app.route("/", methods=['GET', 'POST'])
def hello_monkey_mms():
    """Respond to incoming calls with a simple text message."""
    print request
    print request.__dict__
    #three_words = request.values.get("Body", None)
    # TODO: sanity check body; error handling
    print request.values.get("Body")
    words = guess_format(request.values.get("Body"))
    print "Words: {}".format(words)
    resp = twilio.twiml.Response()
    data = wtw_lookup(words)
    print "data: {}".format(data)
    with resp.message(data.get("sms")) as m:
        m.media(data.get("mms"))
    return str(resp)

if __name__ == "__main__":
     app.debug = True
     port = int(os.environ.get("PORT", 33507))
     app.run(host='0.0.0.0', port=port)
