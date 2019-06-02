from flask import Flask
from redis import StrictRedis

app = Flask(__name__)

# rd = StrictRedis(host='redis', port=6379, db=0)
# r.set("counter", 0)

@app.route("/")
def hello():
    return "Hello World!"

# @app.route("/counter")
# def counter():
#     value = r.get("counter")
#     rd.incr("counter")
#     return "current value: {}".format(value)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
