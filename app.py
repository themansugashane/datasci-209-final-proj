from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  # Introduction page

@app.route("/task_1")
def task_1():
    return render_template("task_1.html")

@app.route("/task_2")
def task_2():
    return render_template("task_2.html")

@app.route("/task_3")
def task_3():
    return render_template("task_3.html")

@app.route("/task_4")
def task_4():
    return render_template("task_4.html")

if __name__ == "__main__":
    app.run(debug=True)
