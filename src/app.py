from flask import Flask, render_template, request, redirect, url_for, flash,make_response,jsonify
from db import insert_asistencia, insert_report,get_reports,get_reports_from, get_asistencia_evento, get_asistencia_carnet
from flask_cors import CORS
import os
import time

app = Flask(__name__)
CORS(app)

@app.route(r'/report', methods=['POST','GET'])
def report():
    if request.method == 'POST':
        content = request.get_json()
        carnet = content['carnet']
        nombre = content['nombre']
        curso = content['curso']
        mensaje = content['mensaje']
        servidor = os.environ['SEVER_NAME']

        rows_inserted = insert_report(
            carnet,
            nombre,
            curso,
            mensaje,
            servidor
        )
        response = make_response(
        jsonify({"rows_inserted": rows_inserted}),200,)
        response.headers["Content-Type"] = "application/json"
        return response
    elif request.method == 'GET':
        body = get_reports()
        response = make_response(
        jsonify({"items": body, "servidor" : os.environ['SEVER_NAME']}),200,)
        response.headers["Content-Type"] = "application/json"
        return response

@app.route(r'/report/<id>', methods=['GET'])
def reports(id):
    if request.method == 'GET':
        body = get_reports_from(id)
        response = make_response(
        jsonify({"items": body, "servidor" : os.environ['SEVER_NAME']}),200,)
        response.headers["Content-Type"] = "application/json"
        return response        

@app.route(r'/asistencia', methods=['POST'])
def asistencia():
    content = request.get_json()
    carnet = content['carnet']
    nombre = content['nombre']
    evento = content['evento']
    id_evento = content['id_evento']
    imagen = content['imagen']
    fecha_hora = time.strftime("%x") + " " + time.strftime("%X")
    servidor = os.environ['SEVER_NAME']

    rows_inserted = insert_asistencia(
        carnet,
        nombre,
        evento,
        id_evento,
        imagen,
        fecha_hora,
        servidor
    )
    response = make_response(
    jsonify({"rows_inserted": rows_inserted}),200,)
    response.headers["Content-Type"] = "application/json"
    return response

@app.route(r'/evento/<id>', methods=['GET'])
def asistencia_evento(id):
    if request.method == 'GET':
        body = get_asistencia_evento(id)
        response = make_response(
        jsonify({"items": body}),200,)
        response.headers["Content-Type"] = "application/json"
        return response    

@app.route(r'/carnet/<id>', methods=['GET'])
def asistencia_carnet(id):
    if request.method == 'GET':
        body = get_asistencia_carnet(id)
        response = make_response(
        jsonify({"items": body}),200,)
        response.headers["Content-Type"] = "application/json"
        return response   

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3500, debug=False)        