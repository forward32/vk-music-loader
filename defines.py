"""
Other
"""
APP_PORT = 65010
CLIENT_ID = 5053271
CLIENT_SECRET = "T9qLBd3i7G7mnOORWW8k"
# for using on localhost
REDIRECT_URI = "http://localhost:{0}/callback".format(APP_PORT)
# for using with ngrok tunnel
#REDIRECT_URI = "http://3631c9bf.ngrok.com/callback"
DISPLAY_TYPE = "page"
SCOPES = "audio,offline"
VERSION_API = 5.37
RESPONSE_TYPE = "token"
MAX_AGE = 2592000
MAX_TRACKS_COUNT = 6000

"""
Url's
"""
BASE_URL = "http://localhost:{0}".format(APP_PORT)
