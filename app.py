## Flask Front End app for adminde-tc project.
## Pybabylon Project.
## Coded by: Mauricio Alcala (@maualkla)
## Date: May 2023.
## More info at @intmau in twitter or in http://maualkla.com
## Description: Web app to serve adminde-tc project.
## flask run --host=0.0.0.0 --port=3000

## Imports
## Imports
from flask import Flask, jsonify, request, render_template, redirect, make_response
import os, requests


## Initialize Flask App
app = Flask(__name__)


## @TO_BE_DELETED 
# sample helloworld
@app.route('/postman', methods=['POST'])
def postman():
    url = request.json['url']
    method = request.json['method']
    key1 = request.json['key1']
    val1 = request.json['val1']
    key2 = request.json['key2']
    val2 = request.json['val2']
    key3 = request.json['key3']
    val3 = request.json['val3']

    data = {
        key1: val1,
        key2: val2,
        key3: val3
        }
    print(data)
    headers = {'Content-type': 'application/json'}
    print("validando")
    if method == 'post':
        print("go to post")
        response = requests.post(url, json=data, headers=headers)
    else: 
        print("go to get")
        response = requests.get(url, headers=headers)
    
    print(response.json())
    return response.json()


## @TO_BE_DELETED 
# sample helloworld
@app.route('/helloworld')
def hello_world():
    import requests

    url = 'http://localhost:3000/login?u=jp@adminde.com&p=aG9sYTEyMw=='
    headers = {'Content-type': 'application/json'}

    response = requests.get(url, headers=headers)
    ##print(response.json())
    
    ##print(response.json())
    return response.json()

## @TO_BE_DELETED
# Landing page
@app.route('/')
def landing():
    return render_template('index.html')

@app.route('/index')
def index():
    local_ip = request.remote_addr

    response = make_response(redirect('/status'))
    response.set_cookie('local_ip', local_ip)
    return response

## Login page
@app.route('/login')
def login():
    return render_template('login.html')

## Login process
@app.route('/s_login')
def s_login():
    _u = request.cookies.get('_u')
    _p = request.cookies.get('_p')
    return 'User = '+_u+'; Password: '+_p

## @TO_BE_DELETED
# Sample service
@app.route('/service', methods=['GET'])
def service():
    data = request.get_json()
    if data:
        return jsonify({
            "status": "connected",
            "code": 200
        })
    else:
        return jsonify({
            "status": "Error",
            "code": 500
        })
    
## API Status
@app.route('/status')
def status():
    _local_ip = request.remote_addr
    local_ip = request.cookies.get('local_ip')
    return "Running fine - IP: "+local_ip

if __name__ == '__main__':
    app.run(debug=True)
