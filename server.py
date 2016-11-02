from flask import Flask, session, render_template, request, redirect
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route("/")
def randomize():
    num = random.randrange(0,101)
    if "rando" in session:
        pass
    else:
        session["rando"] = num
    print num
    return render_template("index.html")

@app.route("/button", methods=["POST"])
def guess():
    actual = session["rando"]
    number = request.form["number"]
    if (int(number) > int(actual)):
        return render_template("too_high.html")
    elif (int(number) < int(actual)):
        return render_template("too_low.html")
    elif(int(number) == int(actual)):
        return render_template("you_win.html", number=number)

@app.route("/playAgain", methods=["POST"])
def play_again():
    session.pop("rando")
    return redirect("/")

app.run(debug=True)
