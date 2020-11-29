
#jeżeli jesteś 1. w kolejce to nowy komunikat
#wsparcie błędów, jeżeli spotkania nie ma, to komunikat tak samo dla usuwanych
#dodać do bazy tabelę z administratorami i najpierw ma pyta,c o hasło
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from database import *
from queries import *



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://queuingsystem:1234@localhost/queuingdb'
db.init_app(app)


@app.route("/", methods=["get"])
def index():
    purposes = list(map(lambda x: x.name, get_purposes()))
    return render_template("index.html", purposes=purposes, length=len(purposes))


@app.route("/add_client", methods=["post"])
def add_client():
    firstname = request.form["firstname"]
    lastname = request.form["lastname"]
    purpose = request.form["purpose"]
    appointment=Appointment(get_purpose_id(purpose), firstname, lastname)
    add_appointment(appointment)
    return render_template("add_client.html")

@app.route("/remove_appointment/<idx>", methods=["get"])
def remove_appointment(idx: int):
    remove(idx)
    return render_template("remove_appointment.html")

@app.route("/estimate_time/<idx>", methods=["get"])
def estimate_time(idx: int):
    predecessors_count=count_predecessors(idx)
    order=predecessors_count+1
    return render_template("estimate_time.html", order=order, time=predecessors_count*15)