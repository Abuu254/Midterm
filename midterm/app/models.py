"""Database models"""
from sqlalchemy import ForeignKey
from app import db

class Object(db.Model):
    """object"""
    __tablename__ = 'objects'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String)
    accession_no = db.Column(db.String)
    date = db.Column(db.String)


class Place(db.Model):
    """place"""
    __tablename__ = 'places'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String)
    part_of = db.Column(db.String)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    url = db.Column(db.String)

class Agent(db.Model):
    """agent"""
    __tablename__ = 'agents'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    begin_date = db.Column(db.String)
    end_date = db.Column(db.String)
    begin_place_id = db.Column(db.Integer, ForeignKey('places.id'))
    end_place_id = db.Column(db.Integer, ForeignKey('places.id'))


class Department(db.Model):
    """department"""
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class Classifier(db.Model):
    """classifier"""
    __tablename__ = 'classifiers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class Reference(db.Model):
    """reference"""
    __tablename__ = 'references'
    id = db.Column(db.Integer, primary_key=True)
    obj_id = db.Column(db.Integer, ForeignKey('objects.id'))
    type = db.Column(db.String)
    content = db.Column(db.String)

class Nationality(db.Model):
    """nationality"""
    __tablename__ = 'nationalities'
    id = db.Column(db.Integer, primary_key=True)
    descriptor = db.Column(db.String)

class Production(db.Model):
    """production"""
    __tablename__ = 'productions'
    obj_id = db.Column(db.Integer, ForeignKey('objects.id'), primary_key=True)
    agt_id = db.Column(db.Integer, ForeignKey('agents.id'), primary_key=True)
    part = db.Column(db.String)

class ObjectsClassifier(db.Model):
    """objectsclassifier"""
    __tablename__ = 'objects_classifiers'
    obj_id = db.Column(db.Integer, ForeignKey('objects.id'), primary_key=True)
    cls_id = db.Column(db.Integer, ForeignKey('classifiers.id'), primary_key=True)

class ObjectsDepartment(db.Model):
    """objectsdepartment"""
    __tablename__ = 'objects_departments'
    obj_id = db.Column(db.Integer, ForeignKey('objects.id'), primary_key=True)
    dep_id = db.Column(db.Integer, ForeignKey('departments.id'), primary_key=True)

class ObjectsPlace(db.Model):
    """objectsplace"""
    __tablename__ = 'objects_places'
    obj_id = db.Column(db.Integer, ForeignKey('objects.id'), primary_key=True)
    pl_id = db.Column(db.Integer, ForeignKey('places.id'), primary_key=True)

class AgentsNationality(db.Model):
    """agentsnationlity"""
    __tablename__ = 'agents_nationalities'
    agt_id = db.Column(db.Integer, ForeignKey('agents.id'), primary_key=True)
    nat_id = db.Column(db.Integer, ForeignKey('nationalities.id'), primary_key=True)
