from flask import Flask, request
from flask import redirect, render_template
import requests
from url_maker import *


app = Flask(__name__)


@app.route("/")
def home():
    return redirect("/tracks")


@app.route("/callback")
def auth_callback():
    error = request.args.get("error")
    if error:
        return error

    code = request.args.get("code")
    url = make_token_url(code)
    ret = requests.get(url).json()
    if "error" in ret:
        return ret["error"]

    user_id = str(ret["user_id"])
    token = ret["access_token"]
    # id:token
    user_info_storage[user_id] = token

    redirect_to_tracks = redirect("/tracks")
    response = app.make_response(redirect_to_tracks)
    response.set_cookie("user_id", value=user_id, max_age=MAX_AGE)
    return response


@app.route("/tracks", methods=["GET"])
def tracks():
    user_id = request.cookies.get("user_id")
    if not user_id in user_info_storage:
        url = make_auth_url()
        return redirect(url)
    
    token = user_info_storage[user_id]
    url = make_audio_get(user_id, 0, MAX_TRACKS_COUNT, token)
    ret = requests.get(url).json()
    if "error" in ret:
        return ret["error"]

    tracks=ret["response"]["items"]
    with open("tracks.lst", "w+") as f:
        for track in tracks:
            f.write("{0}###{1}\n".format(track["artist"]+"_"+track["title"], track["url"]))

    return "Info about tracks saved into 'tracks.lst'"


if __name__ == "__main__":
    user_info_storage = {}
    app.run(port=APP_PORT, debug=True)
