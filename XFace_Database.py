import sqlite3
from datetime import datetime, timedelta
import os

current_directory = os.getcwd()  # Get current directory
db_path = 'DB/database.db'
userRegPhoto_directory = os.path.join(current_directory, db_path)# ユーザー登録で画像を一時保存するディレクトリ

def create_tables():
    conn = sqlite3.connect(userRegPhoto_directory)
    c = conn.cursor()

    c.execute('''CREATE TABLE userinfo
                 (UserID INTEGER PRIMARY KEY,
                  UserName TEXT NOT NULL,
                  Password TEXT NOT NULL,
                  DepartmentID INTEGER NOT NULL,
                  AdminFlag INTEGER NOT NULL,
                  FacePhoto BLOB)''')

    c.execute('''CREATE TABLE AttendanceRecord
                 (UserID INTEGER NOT NULL,
                  YearMonth INTEGER NOT NULL,
                  Date INTEGER NOT NULL,
                  WorkStartTime TEXT,
                  WorkEndTime TEXT,
                  WorkingTime REAL,
                  Memo TEXT,
                  FOREIGN KEY(UserID) REFERENCES userinfo(UserID))''')

    c.execute('''CREATE TABLE AccessRecord
                 (UserID INTEGER NOT NULL,
                  YearMonth INTEGER NOT NULL,
                  Date INTEGER NOT NULL,
                  EnteringTime TEXT,
                  FOREIGN KEY(UserID) REFERENCES userinfo(UserID))''')

    c.execute('''CREATE TABLE DepartmentMaster
                 (DepartmentID INTEGER PRIMARY KEY,
                  DepartmentName TEXT NOT NULL,
                  WorkStartTime TEXT NOT NULL,
                  WorkEndTime TEXT NOT NULL,
                  RestTime INTEGER NOT NULL,
                  OverTime INTEGER NOT NULL)''')

    c.execute('''CREATE TABLE QRinfo
                 (QRID INTEGER PRIMARY KEY,
                  QRName TEXT NOT NULL,
                  StartTime TEXT NOT NULL,
                  EndTime TEXT NOT NULL,
                  Password TEXT NOT NULL,
                  CreatedBy TEXT NOT NULL,
                  CreationDate TEXT NOT NULL)''')

    conn.commit()
    conn.close()


def insert_data():
    conn = sqlite3.connect(userRegPhoto_directory)
    c = conn.cursor()


    users_data = [
        ('100000', 'adminuser', '123456', '0', 1, '')
    ]

    images_folder = 'XFace_User_List/images'
    for i, user in enumerate(users_data):
        try:
            with open(os.path.join(images_folder, f"{user[1]}.png"), 'rb') as file:
                users_data[i] = user[:-1] + (file.read(),)
        except FileNotFoundError:
            continue

    c.executemany('INSERT INTO userinfo (UserID, UserName, Password, DepartmentID, AdminFlag, FacePhoto) VALUES (?, ?, ?, ?, ?, ?)', users_data)
    conn.commit()

    conn.close()

def insert_department_data():
    conn = sqlite3.connect(userRegPhoto_directory)
    c = conn.cursor()

    departments_data = [
        (0, 'No_department', '09:00', '18:00', 1, 0)
    ]

    c.executemany('INSERT INTO DepartmentMaster (DepartmentID, DepartmentName, WorkStartTime, WorkEndTime, RestTime, OverTime) VALUES (?, ?, ?, ?, ?, ?)', departments_data)
    conn.commit()
    conn.close()

create_tables()
insert_data()
insert_department_data()
