from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///details.db'
db = SQLAlchemy(app)
# MVC
class Details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return '<Details %r>' % self.id
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/form',methods=['POST','GET'])
def form():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        details = Details(name=name,email=email,phone=phone)
        db.session.add(details)
        db.session.commit()
        return render_template('form.html')
    else:
        all_posts = Details.query.order_by(Details.date_created).all()
        return render_template("form.html")
        
if __name__ == '__main__':
    app.run(debug=True)