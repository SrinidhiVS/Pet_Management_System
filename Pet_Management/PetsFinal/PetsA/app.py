from flask import Flask, flash, request, redirect, url_for, send_from_directory, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import select
from sqlalchemy import text
from flask import request
import json


app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:DBMS5678@localhost/Pettest"
app.config["SQLALCHEMY_TRACK_NOTIFICATIONS"] = False

db = SQLAlchemy(app)

with app.app_context():
    db.reflect()
    tables = db.metadata.tables
    print(tables.keys())


@app.route("/")
def hello():
    return "hello"

@app.route("/get-petinfo/<type>")
def pet_table(type):
    table = tables["pet"]
    query = text(f"SELECT * FROM PET WHERE TYPE='{type}'")
    
    with db.engine.connect() as connection:
        result = connection.execute(query)
        rows = result.fetchall()
    data = []

    for row in rows:
        data.append(list(row))

    return {"data" : data}

@app.route("/get-count/<type>")
def get_count(type):
    query = text(f"SELECT COUNT(PET_ID) FROM PET WHERE TYPE='{type}'")
    
    with db.engine.connect() as connection:
        result = connection.execute(query)
        rows = result.fetchall()
    data = []

    for row in rows:
        data.append(list(row))

    return {"data" : data}



#Get Commands 
@app.route("/get-records")
def medical_records():
    table = tables["medical_records"]
    query = select(*[column for column in table.columns])
    with db.engine.connect() as connection:
        result = connection.execute(query)
        rows = result.fetchall()
    data = []
    for row in rows:
        data.append(list(row))
    return {"data" : data}

@app.route("/get-adopter")
def adopter():
    table = tables["adopter"]
    query = select(*[column for column in table.columns])
    with db.engine.connect() as connection:
        result = connection.execute(query)
        rows = result.fetchall()
    data = []
    for row in rows:
        data.append(list(row))
    return {"data" : data}

@app.route("/get-employee")
def employee():
    table = tables["employee"]
    query = select(*[column for column in table.columns])
    with db.engine.connect() as connection:
        result = connection.execute(query)
        rows = result.fetchall()
    data = []
    for row in rows:
        data.append(list(row))
    return {"data" : data}

@app.route("/get-feedback")
def feedback():
    table = tables["feedback"]
    query = select(*[column for column in table.columns])
    with db.engine.connect() as connection:
        result = connection.execute(query)
        rows = result.fetchall()
    data = []
    for row in rows:
        data.append(list(row))
    return {"data" : data}


@app.route("/get-all-tables")
def get_all():
    data = {}
    for key in tables.keys():
        query = text(f"select * from {key}")
        with db.engine.connect() as conn:
            result = conn.execute(query)
            rows = result.fetchall()

        data_arr = []
        for row in rows:
            data_arr.append(list(row))
        data[key] = data_arr

    return data


#Delete Commands
@app.route("/pet-table/<int:pet_id>", methods=["POST"])
def delete_pet(pet_id):
    query = text(f"DELETE FROM PET WHERE PET_ID = {pet_id}")
    print(query)
    with db.engine.connect() as connection:
        connection.execute(query)
        connection.commit()
        
    return f"Pet with ID {pet_id} has been deleted successfully."


@app.route("/medical-records-table/<int:pet_id>", methods=["POST"])
def delete_record(pet_id):
    query = text(f"DELETE FROM MEDICAL_RECORDS WHERE MEDICAL_RECORDS.PET_ID = {pet_id}")
    print(query)
    with db.engine.connect() as connection:
        connection.execute(query)
        connection.commit()

    return f"Pet with ID {pet_id} has been deleted successfully."


@app.route("/type-table/<int:type_id>", methods=["POST"])
def delete_type(type_id):
    query = text(f"DELETE FROM TYPE WHERE TYPE_ID = {type_id}")
    print(query)
    with db.engine.connect() as connection:
        connection.execute(query)
        connection.commit()

    return f"Deleted {type_id}"

@app.route("/shelter-table/<int:shelter_id>", methods=["POST"])
def delete_shelter(shelter_id):
    query = text(f"DELETE FROM SHELTER WHERE SHELTER_ID = {shelter_id}")
    print(query)
    with db.engine.connect() as connection:
        connection.execute(query)
        connection.commit()

    return f"Deleted {shelter_id}"

@app.route("/employee-table/<int:employee_id>", methods=["POST"])
def delete_employee(employee_id):
    query = text(f"DELETE FROM employee WHERE employee_id = {employee_id}")
    print(query)
    with db.engine.connect() as connection:
        connection.execute(query)
        connection.commit()

    return f"Deleted {employee_id}"

@app.route("/adopter-table/<int:adopter_id>", methods=["POST"])
def delete_adopter(adopter_id):
    query = text(f"DELETE FROM adopter WHERE adopter_id = {adopter_id}")
    print(query)
    with db.engine.connect() as connection:
        connection.execute(query)
        connection.commit()

    return f"Deleted {adopter_id}"



#INSERT OPERATION
@app.route("/insert-all", methods = ["POST"])
def insert_all():
    if request.method == "POST":
        data = json.loads(request.data)
        print(data)


    queries = [
        f"INSERT INTO PET VALUES({data['pet_id']}, '{data['pet_name']}', '{data['pet_type']}', '{data['pet_breed']}', {data['pet_age']}, 'F', '{data['pet_status']}')",
        f"INSERT INTO MEDICAL_RECORDS VALUES({data['pet_id']}, {data['vaccination_id']}, '{data['vaccination_status']}', '{data['next_due_date']}', '{data['disease_history']}', '{data['current_diseases']}')",
        f"INSERT INTO ADOPTER VALUES({data['adopter_id']}, {data['pet_id']}, '{data['adopter_name']}', {data['amount']}, {data['contact']})",
        f"INSERT INTO EMPLOYEE VALUES ({data['employee_id']}, '{data['name']}', 'F', {data['salary']}, '9999999')",
    ]


    
    with db.engine.connect() as connection:
        for query in queries:
            print(query)
            try:
                connection.execute(text(query))
                connection.commit()
            except:
                pass
            
        
        
        
    return {"Sucess": True}


app.run(port=5000, debug=True)