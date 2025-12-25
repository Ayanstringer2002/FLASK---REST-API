from flask import Flask, request, jsonify
import mysql.connector
app = Flask(__name__)

db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='WJ28@krhps',
    database='mydatabase',
    port=3308 
    
)

## Now creating POST Route 
@app.route('/addStudent',methods=['POST'])
def add_student():
    data=request.get_json()
    name=data.get('name')
    mark=data.get('mark')
    
    cursor=db.cursor()
    sql_query="INSERT INTO students (name,mark) VALUES (%s,%s)"
    cursor.execute(sql_query,(name,mark))
    db.commit()
    return jsonify({"message":"student added successfully"}),200

## Now Creating Fetching Route
@app.route('/fetchAll', methods=['GET'])
def fetch_all():
    cursor=db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students")
    rows=cursor.fetchall()
    cursor.close()
    return jsonify(rows)

## Now Creating Fetching Route by ID
@app.route('/fetchbyid/<int:id>', methods=['GET'])
def fetchById(id):
    cursor=db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students WHERE id=%s", (id,))
    data=cursor.fetchall()
    cursor.close()
    return jsonify(data)

## Now Creating Update Route (BY Id)
@app.route('/update',methods=['PUT'])
def update_data():
    id=request.json.get('id')
    name=request.json.get('name')
    mark=request.json.get('mark')
    cursor=db.cursor()
    query="UPDATE students SET name=%s,mark=%s WHERE id=%s"
    cursor.execute(query,(name,mark,id))
    db.commit()
    cursor.close()
    return jsonify({"message": "update"}), 200




if __name__=="__main__":
    print("connecting to db...")
    app.run()
    
    