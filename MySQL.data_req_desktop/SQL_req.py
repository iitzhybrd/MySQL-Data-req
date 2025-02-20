from flask import Flask, request, jsonify
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

db_config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "Afxentis2000!",
    "database": "testsql",
    "port": 3306,
}

@app.route("/submit_data", methods=["POST"])
def submit_data():
    try:
        conn = mysql.connector.connect(**db_config)

        if conn.is_connected():
            cursor = conn.cursor()

            data = request.get_json()
            username = data["username"]
            password = data["password"]

            insert_query = "INSERT INTO user_table (username, password, create_time) VALUES (%s, %s, CURRENT_TIMESTAMP)"
            data_to_insert = (username, password)

            cursor.execute(insert_query, data_to_insert)
            conn.commit()

            return jsonify({"message": "Data inserted and saved successfully."})

    except mysql.connector.Error as e:
        return jsonify({"message": f"Error connecting to MySQL: {e}"})
    except Exception as e:
        return jsonify({"message": f"An error occurred: {e}"})
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

@app.route("/get_data", methods=["GET"])
def get_data():
    try:
        conn = mysql.connector.connect(**db_config)

        if conn.is_connected():
            cursor = conn.cursor(dictionary=True)

            cursor.execute("SELECT username, password, create_time FROM user_table")

            rows = cursor.fetchall()

            return jsonify(rows)

    except mysql.connector.Error as e:
        return jsonify({"message": f"Error connecting to MySQL: {e}"})
    except Exception as e:
        return jsonify({"message": f"An error occurred: {e}"})
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    app.run()