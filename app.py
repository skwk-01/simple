from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

class Memo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100))

@app.route("/", methods=["GET", "POST"])
def home():
    memo = Memo.query.all()
    return render_template("index.html", memo=memo)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
