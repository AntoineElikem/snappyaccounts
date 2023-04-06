from flask import Flask


application = Flask(__name__)
app = application

######################################################################
# GET INDEX
######################################################################
@app.route("/")
def index():
    """Root URL response"""
    return (
        "Hello World! This is the root URL. "
    )