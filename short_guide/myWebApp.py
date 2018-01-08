from flask import Flask, render_template

# setup Flask app
app = Flask(__name__)


# Ensure responses aren't cached on your browser.
# Useful to see the changes you have made to your front end.
# You can delete this block once the project is finished.
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# When someone accesses "/" returns the index.html file in the teamplate folder
@app.route("/")
def home():
    return render_template("index.html")


# Run the program
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3126, threaded=True, debug=False)
