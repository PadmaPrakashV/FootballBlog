from flask import Flask,render_template

app = Flask(__name__)

players = [
            {'name':'Cristiano Ronaldo','age':33,'position':'Attacker','country':'Portugal'},
            {'name':'Lionel Messi','age':32,'position':'Attacker','country':'Argentina'},
            {'name':'Wayne Rooney','age':35,'position':'Attacker','country':'England'}
]

@app.route("/")
@app.route("/home")
def home():
    title = "Home"
    return render_template('home.html',title=title,players=players)

@app.route("/statistics/<player>")
def statistics(player):
    return render_template('stats.html',player=player)

if(__name__ == "__main__"):
    app.run(debug="True")