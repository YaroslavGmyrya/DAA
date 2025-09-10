from flask import Flask
import signal
import sys

print("Start server")


def handle_stop(signum, frame):
    print("Stop server")
    sys.exit(0)

app = Flask(__name__)

@app.route("/")
def hello():
    return """
        <div style="text-align:center; padding-top:250px;">
            <img src="https://media.tenor.com/IB9ol7welioAAAAM/dance-vibing.gif">
        </div>
        """

signal.signal(signal.SIGINT, handle_stop)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
