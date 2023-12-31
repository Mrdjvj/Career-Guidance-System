import mysql.connector
from datetime import datetime,timedelta

def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="vedant2803",
        database="DBMS_miniproject",
        auth_plugin="mysql_native_password",
    )
    return connection


def past_appointments(Counsellor_ID):
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)

    query = """SELECT Appointment_ID,Student_ID,Date,Start_Time FROM Appointments where Counsellor_ID=%s"""
    cursor.execute(query, (Counsellor_ID,))
    appointments = cursor.fetchall()

    cursor.close()
    connection.close()

    return appointments
