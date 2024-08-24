from flask import Flask, render_template, request, redirect, url_for, flash
import pyodbc
from flask_pymongo import PyMongo
import logging
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
app = Flask(__name__)
# Thay thế <db_password> bằng mật khẩu thực tế của bạn
app.config["MONGO_URI"] = "mongodb+srv://tuan:tuan@students.kptlr.mongodb.net/students?retryWrites=true&w=majority"
mongo = PyMongo(app)

@app.route('/')
def index():
    # Truy vấn dữ liệu từ bộ sưu tập 'students' trong cơ sở dữ liệu 'students'
    students = mongo.db.students.find()
    return render_template('index.html', students=students)


if __name__ == '__main__':
    app.run(debug=True)
