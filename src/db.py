import mysql.connector

mydb = mysql.connector.connect(
  host="db",
  user="root",
  password="1234",
  database="redes2"
)

def insert_report(carnet,nombre,curso,mensaje,servidor):
    try:
        cur = mydb.cursor()
        cur.execute('''INSERT INTO reporte(
                carnet,
                nombre,
                curso,
                mensaje,
                servidor)
            VALUES(%s, %s, %s, %s,%s)''',
            (carnet,nombre,curso,mensaje,servidor))
        mydb.commit()
        return cur.rowcount
    except:
        return 0

def get_reports():
    mydb.commit()
    cur = mydb.cursor()
    cur.execute('''SELECT carnet,
                        nombre,
                        curso,
                        mensaje,
                        servidor,
                        id 
                FROM reporte ''')
    reports = cur.fetchall()
    respuesta = []
    for report in reports:
        respuesta.append({
            "carnet" : report[0],
            "nombre" : report[1],
            "curso" : report[2],
            "mensaje" : report[3],
            "servidor" : report[4],
            "id" : report[-1]
        })
    return respuesta

def get_reports_from(id):
    mydb.commit()
    cur = mydb.cursor()
    cur.execute('''SELECT carnet,
                        nombre,
                        curso,
                        mensaje,
                        servidor,
                        id 
                FROM reporte
                WHERE id = %s ''',(id,))
    reports = cur.fetchall()
    respuesta = []
    for report in reports:
        respuesta.append({
            "carnet" : report[0],
            "nombre" : report[1],
            "curso" : report[2],
            "mensaje" : report[3],
            "servidor" : report[4],
            "id" : report[-1]
        })
    return respuesta    

def insert_asistencia(carnet,nombre,evento,id_evento,imagen,fecha_hora,servidor):
    try:
        cur = mydb.cursor()
        cur.execute('''INSERT INTO asistencia(
                carnet,
                nombre,
                evento,
                id_evento,
                imagen,
                fecha_hora,
                servidor)
            VALUES(%s, %s, %s, %s, %s, %s, %s)''',
            (carnet,nombre,evento,id_evento,imagen,fecha_hora,servidor))
        mydb.commit()
        return cur.rowcount
    except:
        return 0

def get_asistencia_evento(id_evento):
    mydb.commit()
    cur = mydb.cursor()
    cur.execute('''SELECT carnet,
                        nombre,
                        evento,
                        imagen,
                        fecha_hora,
                        servidor
                FROM asistencia
                WHERE id_evento = %s ''',(id_evento,))
    reports = cur.fetchall()
    respuesta = []
    for report in reports:
        respuesta.append({
            "carnet" : report[0],
            "nombre" : report[1],
            "evento" : report[2],
            "imagen" : report[3],
            "fecha_hora": report[4],
            "servidor" : report[5]
        })
    return respuesta 

def get_asistencia_carnet(carnet):
    mydb.commit()
    cur = mydb.cursor()
    cur.execute('''SELECT carnet,
                        nombre,
                        evento,
                        imagen,
                        fecha_hora,
                        servidor
                FROM asistencia
                WHERE carnet = %s ''',(carnet,))
    reports = cur.fetchall()
    respuesta = []
    for report in reports:
        respuesta.append({
            "nombre" : report[1],
            "evento" : report[2],
            "imagen" : report[3],
            "fecha_hora": report[4],
            "servidor" : report[5]
        })
    return respuesta 

print(get_reports_from("1"))