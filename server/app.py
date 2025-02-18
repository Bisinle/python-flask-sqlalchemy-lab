#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)



# --------------------routes---------------

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.filter_by(id =id).first()
    if not animal:
        response_body = f'''<h1>Animal not found </h1> '''
        return make_response(response_body,404)
    else:
        response_body =  f'''
        
            <ul>id: {animal.id}</ul>
            <ul>Name: {animal.name}</ul>
            <ul>Species: {animal.species}</ul>     
            <ul>Zookeeper: {animal.zookeeper.name}</ul>     
            <ul>Enclosure: {animal.enclosure.environment}</ul>     
        
        
            '''     
  
        return make_response(response_body,200)

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.filter_by(id =id).first()
    if not Zookeeper:
        response_body = f'''<h1>zookeeper not found </h1> '''
        return make_response(response_body,404)
  
        
    response_body =  f'''
        
            <ul>id: {zookeeper.id}</ul>
            <ul>Name: {zookeeper.name}</ul>
            <ul>Birthday: {zookeeper.birthday}</ul>     
                     
            '''    
    animals = [animal for animal in zookeeper.animals]
    for animal in animals:
        response_body += f'''<ul>Animal: {animal.name}</ul>'''
        
  
    return make_response(response_body,200) 
        
  





@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.filter_by(id =id).first()
    if not enclosure:
        response_body = f'''<h1>zookeeper not found </h1> '''
        return make_response(response_body,404)
          
    response_body =  f'''
        
            <ul>id: {enclosure.id}</ul>
            <ul>Environment: {enclosure.environment}</ul>
            <ul>Open to Visitors: {enclosure.open_to_visitors}</ul>     
                     
            '''    
    animals = [animal for animal in enclosure.animals]
    for animal in animals:
        response_body += f'''<ul>Animal: {animal.name}</ul>'''
        
  
    return make_response(response_body,200) 




if __name__ == '__main__':
    app.run(port=5555, debug=True)
