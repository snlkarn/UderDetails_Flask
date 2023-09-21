from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///User.sqlite3'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "user"
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def __init__(self, name, email):
        self.name = name
        self.email = email

@app.route("/")
def home():
    return redirect(url_for('index'))

@app.route("/index", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        data = request.form
        name = data["name"]
        email = data["email"]

        new_data = User(name, email)
        db.session.add(new_data)
        db.session.commit()

        return redirect(url_for('index'))  # Redirect after POST

    user_data = User.query.all()
    return render_template("index.html", user_data=user_data)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='localhost', port=8080)

