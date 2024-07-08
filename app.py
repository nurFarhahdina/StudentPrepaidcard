from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'prepaidCard'

def get_db_connection():
    conn = sqlite3.connect('prepaid_cards.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_balance', methods=['POST'])
def check_balance():
    student_id = request.form['student_id']


    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT s.StudentName, pc.CardNo, pc.Balance
        FROM Students 
        INNER JOIN PrepaidCard pc ON s.StudentID = pc.StudentID
        WHERE s.StudentID = ?
    ''', (student_id,))
    result = cursor.fetchone()
    conn.close()

    if result:
        student_name = result['StudentName']
        card_no = result['CardNo']
        balance = result['Balance']
        formatted_balance = f"RM {balance:.2f}"

if __name__ == '__main__':
    app.run(debug=True)