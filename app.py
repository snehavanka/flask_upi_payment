from flask import Flask, render_template, request, redirect
import mysql.connector
import re

app = Flask(__name__)


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sneha@220",  
    database="payment_db"
)
cursor = db.cursor()


def gmail_exists(email):
    return bool(re.match(r"[^@]+@gmail\.com$", email))  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pay', methods=['POST'])
def pay():
    name = request.form['name']
    email = request.form['email']
    sender_upi = request.form['sender_upi_id']
    receiver_upi = "6281917774-2@axl"

    if gmail_exists(email):
        cursor.execute(
            "INSERT INTO payments (name, email, upi_id, receiver_upi_id) VALUES (%s, %s, %s, %s)",
            (name, email, sender_upi, receiver_upi)
        )
        db.commit()

        upi_url = f"upi://pay?pa={receiver_upi}&pn=ReceiverName&am=1&cu=INR"
        return render_template('payment_success.html', receiver_upi=receiver_upi, upi_url=upi_url)
    else:
        return "❌ Invalid Gmail format.", 400


if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=5000, debug=True)
