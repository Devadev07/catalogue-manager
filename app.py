from flask import Flask, request, jsonify, render_template
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Database connection
def get_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='8055',  
        database='companydb'
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/catalogues', methods=['POST'])
def add_catalogue():
    data = request.get_json()
    name = data.get('name')
    start = data.get('start_date')
    end = data.get('end_date')

    print("Received:", name, start, end)  

    db = None
    cursor = None
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO catalogue (catalogue_name, start_date, end_date, is_deleted) VALUES (%s, %s, %s, 0)",
            (name, start, end)
        )
        db.commit()
        return jsonify({"status": "success"}), 201
    except Exception as e:
        print("❌ Error:", e)  
        return jsonify({"status": "error", "message": str(e)}), 500
    finally:
        if cursor: cursor.close()
        if db: db.close()



@app.route('/getCatalogues', methods=['GET'])
def get_catalogues():
    db = None
    cursor = None
    try:
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM catalogue WHERE is_deleted = 0 ORDER BY catalogue_id DESC")
        result = cursor.fetchall()
        return jsonify(result)
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})
    finally:
        if cursor: cursor.close()
        if db: db.close()

@app.route('/deleteCatalogue', methods=['POST'])
def delete_catalogue():
    data = request.get_json()
    catalogue_id = data.get('id')  

    db = None
    cursor = None
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('UPDATE catalogue SET is_deleted = 1 WHERE catalogue_id = %s', (catalogue_id,))
        db.commit()
        return jsonify({"status": "success"}), 200
    except Exception as e:
        print("❌ Error deleting:", e)
        return jsonify({"status": "error", "message": str(e)}), 500
    finally:
        if cursor: cursor.close()
        if db: db.close()


if __name__ == '__main__':
    app.run(debug=True)
