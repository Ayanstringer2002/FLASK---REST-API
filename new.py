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



if __name__=="__main__":
    print("connecting to db...")
    app.run()
    
    