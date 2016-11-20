import os

# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient


# Find these values at https://twilio.com/user/account
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")  # "ACXXXXXXXXXXXXXXXXX"
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")  # "YYYYYYYYYYYYYYYYYY"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to=os.environ.get("DANDYE_GOOGLE_VOICE"),
                                 from_=os.environ.get("TWILIO_PHONE_NUMBER"),
                                 body="Treasure Tampa")
