from defines import *

def make_audio_get(user_id, offset, count, token):
    url = "https://api.vk.com/method/audio.get?owner_id={0}"\
          "&offset={1}&count={2}&access_token={3}&v={4}".format(
           user_id, offset, count, token, VERSION_API)
    return url


def make_auth_url():
    url = "https://oauth.vk.com/authorize?client_id={0}&display={1}"\
          "&redirect_uri={2}&scope={3}&responce_type={4}&v={5}".format(
          CLIENT_ID, DISPLAY_TYPE, REDIRECT_URI, SCOPES, RESPONSE_TYPE,
          VERSION_API)
    return url


def make_token_url(code):
    url = "https://oauth.vk.com/access_token?client_id={0}"\
          "&client_secret={1}&redirect_uri={2}&code={3}".format(
          CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, code)
    return url
