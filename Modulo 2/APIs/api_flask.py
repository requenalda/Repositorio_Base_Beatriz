from flask import Flask,render_template
app=Flask(__name__)


@app.route("/roblox")
def home():
    return render_template('roblox.html')

@app.route("/portifolio")
def pagina2():
    return render_template('portifolio.html')




if __name__ == "__main__":
    app.run(debug=True)