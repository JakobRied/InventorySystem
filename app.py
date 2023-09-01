from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from collections import defaultdict
from datetime import datetime
import os

basedir = os.path.abspath(os.path.dirname(__file__))    #current dir

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
db = SQLAlchemy(app)


class Item(db.Model):

    __tablename__ = 'items'
    item_name       = db.Column(db.String(200), primary_key=True)
    unreserved      = db.Column(db.Integer, default=0)
    reserved        = db.Column(db.Integer, default=0)
    ordered         = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Product %r>' % self.item_id
    
class Bike(db.Model):

    __tablename__ = 'bikes'
    bike_name           = db.Column(db.String(200), primary_key=True)
    description         = db.Column(db.String(200))
    due                 = db.Column(db.DateTime, default=datetime.utcnow)

    
class Delay(db.Model):

    __tablename__ = 'delays'
    delay_id        = db.Column(db.Integer, primary_key=True)
    hours           = db.Column(db.Integer, default=0)
    reason          = db.Column(db.String(200))
    date            = db.Column(db.DateTime, default=datetime.utcnow)
    worker_name     = db.Column(db.String(200))


db.create_all()

@app.route('/', methods=["POST", "GET"])
def index():
    items   = Item.query.order_by(Item.item_name).all()
    bikes   = Bike.query.order_by(Bike.due).all()
    delays  = Delay.query.order_by(Delay.date).all()
    return render_template("index.html", items = items, bikes = bikes, delays = delays)


@app.route('/items/', methods=["POST", "GET"])
def viewItem():
    if (request.method == "POST") and ('item_name' in request.form):
        item_name = request.form["item_name"]
        reserved, unreserved, ordered = 0,0,0
        try: 
            ordered         = request.form["ordered"]
            unreserved      = request.form["unreserved"]
            reserved        = request.form["reserved"]
        except KeyError:
            return "You did not enter a number in one of the number-fields. Please also enter ""0"" if applicable"

        new_item = Item(item_name=item_name, ordered=ordered, unreserved=unreserved, reserved=reserved)

        try:
            db.session.add(new_item)
            db.session.commit()
            return redirect("/items/")

        except:
            items   = Item.query.order_by(Item.item_name).all()
            return "There Was an issue while add a new Product"
        
    else:
        items   = Item.query.order_by(Item.item_name).all()
        return render_template("items.html", items=items)
    
@app.route("/dub-items/", methods=["POST", "GET"])
def getItemDublicate():
    item_name = request.form["item_name"]
    items = Item.query.\
        filter(Item.item_name == item_name).\
        all()
    print(items)
    if items:
        return {"output": False}
    else:
        return {"output": True}
    
@app.route("/delete-item/<item_name>")
def deleteItem(item_name):
    item_to_delete = Item.query.get_or_404(item_name)

    try:
        db.session.delete(item_to_delete)
        db.session.commit()
        return redirect("/items/")
    except:
        return "There was an issue while deleting the Item"
    

@app.route('/bikes/', methods=["POST", "GET"])
def viewBike():
    if (request.method == "POST") and ('bike_name' in request.form):
        bike_name = request.form["bike_name"]
        description = ""
        due = datetime.utcnow
        try: 
            description     = request.form["description"]
            due             = request.form["due"]
            due             = datetime.strptime(due, "%Y-%m-%d")
        except KeyError:
            return "You did not enter a Description or a due date"

        new_bike = Bike(bike_name=bike_name, description=description, due=due)

        try:
            db.session.add(new_bike)
            db.session.commit()
            return redirect("/bikes/")

        except:
            bikes   = Bike.query.order_by(Bike.due).all()
            return "There Was an issue while add a new Product"
        
    else:
        bikes   = Bike.query.order_by(Bike.due).all()
        return render_template("bikes.html", bikes=bikes)
    
@app.route("/dub-bikes/", methods=["POST", "GET"])
def getBikeDuplicates():
    bike_name = request.form["bike_name"]
    bikes = Bike.query.\
        filter(Bike.bike_name == bike_name).\
        all()
    print(bikes)
    if bikes:
        return {"output": False}
    else:
        return {"output": True}
    

@app.route("/delete-bike/<bike_name>")
def deleteBike(bike_name):
    bike_to_delete = Bike.query.get_or_404(bike_name)

    try:
        db.session.delete(bike_to_delete)
        db.session.commit()
        return redirect("/bikes/")
    except:
        return "There was an issue while deleting the Bike"
    

@app.route('/delays/', methods=["POST", "GET"])
def viewDelay():
    if (request.method == "POST"):
        reason  = request.form["reason"]
        hours   = request.form["hours"]
        date    = request.form["date"]
        worker  = request.form["worker"]

        date = datetime.strptime(date, "%Y-%m-%d")
        new_delay = Delay(reason=reason, hours=hours, date=date, worker_name=worker)

        try:
            db.session.add(new_delay)
            db.session.commit()
            return redirect("/delays/")

        except:
            delays   = Delay.query.order_by(Delay.date).all()
            return "There Was an issue while add a new Delay"
        
    else:
        delays   = Delay.query.order_by(Delay.date).all()
        return render_template("delays.html", delays=delays)
    

@app.route("/delete-delay/<delay_id>")
def deleteDelay(delay_id):
    delay_to_delete = Delay.query.get_or_404(delay_id)

    try:
        db.session.delete(delay_to_delete)
        db.session.commit()
        return redirect("/delays/")
    except:
        return "There was an issue while deleting the Delay"
    
if (__name__ == "__main__"):
    app.run(debug=True)