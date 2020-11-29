from database import *


def get_purposes():
	purposes = Purpose.query.all()
	return purposes

def get_purpose_id(purpose_name: str):
	return Purpose.query.filter_by(name=purpose_name).first().idx

def add_appointment(appointment: Appointment):
	db.session.add(appointment)
	db.session.commit()

def count_predecessors(idx: int):
	appointment=Appointment.query.get(idx)
	appointments=Appointment.query.filter_by(purpose_idx=appointment.purpose_idx).all()
	predecessors = list(filter(lambda x: x.idx<appointment.idx, appointments))
	return len(predecessors)

def remove(idx:int):
	appointment = Appointment.query.get(idx)
	db.session.delete(appointment)
	db.session.commit()