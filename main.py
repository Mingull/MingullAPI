from flask import Flask, request, render_template
from MCServerAPI.serverstatus import ServerStatus

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/server', methods=["GET", "POST"])
def show_server():
    if 'ip' in request.args:
        ip = request.args.get("ip")
        Server = ServerStatus(ip).returnServerData()
        return Server, {'Content-Type': 'application/json'}
    else:
        return "Error: No IP field provided. Please specify an IP."


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


app.run(host="0.0.0.0", port=8080)