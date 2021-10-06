from flask import Flask, request, jsonify
from random import randint

app = Flask(__name__)


def return_random(i=randint(0, 1000000000)):
    return i

def return_random2():
    return randint(0, 1000000000)

@app.route("/", methods=["GET"])
def check():
    ans = return_random()
    ans2 = return_random2()
    print(ans)
    print(ans2)
    return jsonify([ans, ans2])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555)