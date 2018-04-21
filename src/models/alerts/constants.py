
#URL = "https://api.mailgun.net/v3/duf-family.fr/messages"
#API_KEY = "key-fc80fb984a315d0f40f70cfc90b47793"
#FROM = "Duf <mailgun@duf-family.fr>"
import os

URL = os.environ.get('MAILGUN_URL')
API_KEY = os.environ.get('MAILGUN_API_KEY')
FROM = os.environ.get('MAILGUN_FROM')


ALERT_TIMEOUT = 10
COLLECTION = "alerts"