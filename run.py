import os
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

def write_to_doc(file, data):
    with open(file, "a") as file:
        file.writelines(data)


@app.route("/", methods=["GET","POST"])
def index():
    if request.method=="POST":
        write_to_doc("data/usernames.txt", request.form["username"] + "\n")
        return redirect(request.form["username"])
    return render_template("index.html")

@app.route("/<username>") 
def user(username):
    return render_template("game.html", username=username)

@app.route("/<username>/scores")
def scores(username):
    print(username)
    return render_template("scores.html", username=username)

@app.route("/<username>/message")
def message(username):
    message = "Hello"
    return render_template("message.html", username=username, message=message)



if __name__ == "__main__":
    app.run(host=os.getenv("IP"),port=os.getenv("PORT"), debug=True)


