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
    takes string like "I'm here: https://maps.google.com/maps?q=28.063540,-82.364304"
    returns three words like "loyal.beehives.lock"
    """
    print "Entering latlon2wtw..."
    parts = blob.split("=")
    lat,lon = parts[1].split(",")
    lon = lon.strip()
    print "lat: {}, lon: {}".format(lat,lon)
    # get three words with Lat Lon
    conn = httplib.HTTPSConnection("api.what3words.com")
    print conn
    request_url = \
    "https://api.what3words.com/v2/reverse?coords={lat}%2C{lon}&key={api_key}&lang=en&format=json&display=full".format(
    api_key=API_KEY,
    lat=lat,
    lon=lon)
    print "request_url: {}".format(request_url)
    conn.request("GET", request_url)
    res = conn.getresponse()
    data_str = res.read()
    print "data_str: {}".format(data_str)
    j = json.loads(data_str)
    print j
    print j.keys()
    words = j.get("words")
    return words

"""
def wtw_lookup(words="encounter.inhaled.mime"):
    wtw = yaml.safe_load(open("./wtw.yaml"))
    return wtw.get(words)
"""

"""
def guess_format(blob):
    print "Starting guess_format..."
    print "blob: {}".format(blob)
    if "https://maps.google.com/maps?q=" in blob:
        print "before calling latlon2wtw..."
        words = latlon2wtw(blob)
        print "words: |{}|".format(words)
        return wtw_lookup(words.strip())
    # TODO: more guesses here
    return wtw_lookup(blob)
"""

@app.route("/", methods=['GET', 'POST'])
def google_q_string_to_three_words():
    """Respond to incoming calls with a simple text message."""
    print request
    print request.__dict__

    # TODO: sanity check body; error handling
    sms_body = request.values.get("Body")
    print "sms_body: {}".format(sms_body)

    words = latlon2wtw(sms_body)
    print "Words: {}".format(words)

    resp = twilio.twiml.Response()
    resp.message(words)
    return str(resp)

if __name__ == "__main__":
     app.debug = True
     port = int(os.environ.get("PORT", 33507))
     app.run(host='0.0.0.0', port=port)
