import sqlite3

con = sqlite3.connect('users.sqlite3')
# # query1='CREATE TABLE students (student_id TEXT, name TEXT, email TEXT,username TEXT unique,password TEXT,address TEXT,phone_number TEXT,course TEXT,assignment TEXT)'
# query2='CREATE TABLE teachers (teacher_id TEXT, name TEXT, email TEXT,username TEXT unique,password TEXT,address TEXT,phone_number TEXT,course TEXT)'
#
# con.execute(query1)
# con.execute(query2)
# print("Table created successfully")
# con.close()

# query_insert="select *from students"
# query_insert2='select *from teachers'
query3='select *from admin_account'
data=con.execute(query3)
row=data.fetchall()
print(len(row),row)

# query_insert='insert into students (name,email,username,password,address,phone_number,course) VALUES("s", "ss@gmail.com","w1","1","k","aa","sa")'
# con.execute(query_insert)
# con.execute("insert into students (student_id,name,email,username,password,address,phone_number,course) VALUES(?, ?,?,?,?, ?,?, ?)",("45","s", "ss@gmail.com","w1","1","k","aa","sa"))
# con.execute("insert into admin_account (username,password) values('admin','admin')")
# con.commit()
con.close()







#
# @app.route('/registrationform',methods=['POST','GET'])
# def Registrationform():
#     if request.method=='POST':
#         try:
#             id=request.form['id']
#             name = request.form['name']
#             email=request.form['email']
#             username=request.form['username']
#             password=request.form['password']
#             address = request.form['address']
#             phone = request.form['phone_number']
#             course = request.form['course']
#
#             usertype=request.form['option']       # check user teacher or student
#             print(id,name,email,username,password,address,phone,course)
#             print(usertype)
#
#             with sqlite3.connect("database.db") as con:
#                 cur = con.cursor()
#                 if usertype=='student':
#                     cur.execute("INSERT INTO students (std_id,name,email,username,password,address,phone_number,course) VALUES(?, ?,?,?,?, ?,?, ?)",(id,name,email,username,password,address,phone,course))
#                 else:
#                     cur.execute("INSERT INTO teachers (t_id,name,email,username,password,address,phone_number,course) VALUES(?, ?,?,?,?,?, ?, ?)",(id,name,email,username,password,address,phone,course))
#                 con.commit()
#
#                 msg= "Record successfully added"
#         except:
#             con.rollback()
#             msg= "Error"
#         finally:
#             return msg
#             con.close()
#
#     else:
#         return redirect('/')
#
# # # checking
# # @app.route('/<name>')
# # def user(name):
# #     return f"{name}"












# from flask import Flask,render_template,request,redirect
# from flask_admin import Admin                       # use to make admin interface
# from flask_sqlalchemy import SQLAlchemy             # use for database
# from flask_admin.contrib.sqla import ModelView      # use to create table in admin interface
import sqlite3
#
# # create instance to make flask app
# app=Flask(__name__)
#
# # create admin interface to flask app
# admin=Admin(app)
#
# # %%%%%% Database creation & configuration %%%%%%
#
# # Database Configuration
# app.secret_key="hello"
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.sqlite3'
# db=SQLAlchemy(app)
#
# # con = sqlite3.connect('sqlite3')
#
#
# # Database Models or Tables declaration
# class students(db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#     student_id=db.Column(db.String(50))
#     name=db.Column(db.String(100))
#     email=db.Column(db.String(100))
#     username=db.Column(db.String(100),unique=True)
#     password=db.Column(db.String(100))
#     address=db.Column(db.String(100))
#     phone_number=db.Column(db.String(100))
#     course=db.Column(db.String(100))
#     assignment=db.Column(db.String(100000))
#     def __init__(self,student_id,name,email,username,password,address,phone_number,course,assignment):
#         self.id=id
#         self.student_id=student_id
#         self.name=name
#         self.email=email
#         self.username=username
#         self.password=password
#         self.address=address
#         self.phone_number=phone_number
#         self.course=course
#         self.assignment=assignment
#
# class teachers(db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#     teacher_id=db.Column(db.String(50))
#     name=db.Column(db.String(100))
#     email=db.Column(db.String(100))
#     username=db.Column(db.String(100),unique=True)
#     password=db.Column(db.String(100))
#     address=db.Column(db.String(100))
#     phone_number=db.Column(db.String(100))
#     course=db.Column(db.String(100))
#     def __init__(self,teacher_id,id,name,email,username,password,address,phone_number,course):
#         self.id=id
#         self.teacher_id=teacher_id
#         self.name=name
#         self.email=email
#         self.username=username
#         self.password=password
#         self.address=address
#         self.phone_number=phone_number
#         self.course=course
#
#
#
#
# # %%%%%%% Main Application %%%%%%%%
# @app.route('/', methods=['POST','GET'])
# def home():
#     if request.method=='POST':
#         type_id = request.form['id']
#         name = request.form['name']
#         email = request.form['email']
#         username = request.form['username']
#         password = request.form['password']
#         address = request.form['address']
#         phone = request.form['phone_number']
#         course = request.form['course']
#
#         usertype = request.form['option']  # check user teacher or student
#         print(type_id, name, email, username, password, address, phone, course)
#         print(usertype)
#         # try:
#             # cur = con.cursor()
#         if usertype=='student':
#             usr=students(str(type_id),str(name),str(email),str(username),str(password),str(address),str(phone),str(course),"")
#             db.session.add(usr)
#             db.session.commit()
#             # con.execute("insert into students (student_id,name,email,username,password,address,phone_number,course) VALUES(?, ?,?,?,?, ?,?, ?)",("42","s", "ss@gmail.com","2w1","1","k","aa","sa"))
#             print("d")
#         else:
#             con.execute("INSERT INTO teachers (teacher_id,name,email,username,password,address,phone_number,course) VALUES(?, ?,?,?,?,?, ?, ?)",(type_id,name,email,username,password,address,phone,course))
#         # con.commit()
#         return "<h1>User Created Successfully!!!</h2>"
#         # except:
#         #     return "User Id or username already exist!"
#     else:
#         return render_template('home.html')            # render_tempalte to display html page
#
#
#
# admin.add_view(ModelView(students,db.session))
# admin.add_view(ModelView(teachers,db.session))
#
# if __name__=="__main__":
#     db.create_all()
#     app.run(debug=True)