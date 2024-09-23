from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database connection configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",        # Replace with your MariaDB username
    password="your_password",  # Replace with your MariaDB password
    database="Urbanseva"  # The name of your database
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/retailer_login', methods=['GET', 'POST'])
def retailer_login():
    if request.method == 'POST':
        # Get form data and authenticate user here using database query
        username = request.form['username']
        password = request.form['password']

        cursor = db.cursor(dictionary=True)
        query = "SELECT * FROM retailer_registration WHERE mobile_no=%s AND password=%s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        if result:
            return redirect(url_for('service_entry'))
        else:
            return "Invalid credentials!"
    return render_template('retailer_login.html')

@app.route('/service_entry', methods=['GET', 'POST'])
def service_entry():
    if request.method == 'POST':
        service_name = request.form['service_name']
        service_details = request.form['service_details']
        service_address = request.form['service_address']
        price = request.form['price']

        cursor = db.cursor()
        query = "INSERT INTO services (retailer_id, service_name, service_details, service_address, price) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (1, service_name, service_details, service_address, price))  # Replace '1' with actual retailer ID
        db.commit()

        return redirect(url_for('index'))
    return render_template('service_entry.html')

if __name__ == '__main__':
    app.run(debug=True)
