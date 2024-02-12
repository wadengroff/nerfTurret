from client import Client
#import socket
import keyboard
from flask import Flask



run = True






# ------------------------------------------
# setting up the flask web application
# ------------------------------------------


app = Flask(__name__)


# function runs when the main webpage is run
@app.route("/")
def index():
    return "Congrats it's a web app"


# --------------------------------------------
# setting up the socket based on input
# --------------------------------------------


@app.route("/<ip>:<port>")
def socket_setup(ip, port):
    # 128.61.82.221 wired for Raspberry Pi 4b
    try:
        RASPI_PORT = int(port)
    except:
        return "invalid port"

    # attempt to connect to the socket specified by URL
    conn = Client(ip, port)
    return "tried to connect"
    


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=14549, debug=True)








