# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

from secrets import Secrets

# Find these values at https://twilio.com/user/account
account_sid = Secrets().twilio_account_sid # "ACXXXXXXXXXXXXXXXXX"
auth_token = Secrets().twilio_auth_token # "YYYYYYYYYYYYYYYYYY"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to=Secrets().dandye_google_voice,
                                 from_=Secrets().twilio_phone_number,
                                 body="Treasure Tampa")
