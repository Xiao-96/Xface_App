import sqlite3
import XFace_Database_Function

db_path="DB/database.db"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print("UserInfo Table:")
cursor.execute("SELECT UserID, UserName, Password, DepartmentID, AdminFlag FROM userinfo")
userinfo_data = cursor.fetchall()
for row in userinfo_data:
    print(row)

print("\nAttendanceRecord Table:")
cursor.execute("SELECT * FROM AttendanceRecord ORDER BY Date ASC")
AttendanceRecord_data = cursor.fetchall()
for row in AttendanceRecord_data:
    print(row)

print("\nAccessRecord Table:")
cursor.execute("SELECT * FROM AccessRecord")
AccessRecord_data = cursor.fetchall()
for row in AccessRecord_data:
    print(row)

print("\nDepartmentMaster Table:")
cursor.execute("SELECT * FROM DepartmentMaster")
departmentmaster_data = cursor.fetchall()
for row in departmentmaster_data:
    print(row)
    
print("\nDepartment List:")
departmentmaster_list = XFace_Database_Function.fetch_departmentname()
print(departmentmaster_list)

print("\nQRcode List:")
cursor.execute("SELECT * FROM QRinfo")
QR_data = cursor.fetchall()
for row in QR_data:
    print(row)