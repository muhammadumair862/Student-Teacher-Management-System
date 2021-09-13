from flask import Flask,render_template,request,redirect,session
import sqlite3
from flask_admin import Admin                       # use to make admin interface
from flask_sqlalchemy import SQLAlchemy             # use for database
from flask_admin.contrib.sqla import ModelView      # use to create table in admin interface


# create instance to make flask app
app=Flask(__name__)

app.secret_key="hello"
admin=Admin(app)

# %%%%%%% Database Configuration %%%%%%%%
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.sqlite3'
db=SQLAlchemy(app)


# %%%%%%% Main Application %%%%%%%%
@app.route('/', methods=['POST','GET'])
def home():
    if request.method=='POST':
        type_id = request.form['id']
        name = request.form['name']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        address = request.form['address']
        phone = request.form['phone_number']
        course = request.form['course']

        usertype = request.form['option']  # check user teacher or student
        print(type_id, name, email, username, password, address, phone, course)
        print(usertype)
        try:
            with sqlite3.connect("users.sqlite3") as con:
                cur = con.cursor()

                if usertype=='student':
                    cur.execute("INSERT INTO students (student_id,name,email,username,password,address,phone_number,course) VALUES(?, ?,?,?,?, ?,?, ?)",(type_id,name,email,username,password,address,phone,course))
                else:
                    cur.execute("INSERT INTO teachers (teacher_id,name,email,username,password,address,phone_number,course) VALUES(?, ?,?,?,?,?, ?, ?)",(type_id,name,email,username,password,address,phone,course))
                con.commit()

                msg= "<h2>Record successfully added!!!</h2><br><a href='/'>Back</a>"
        except:
            con.rollback()
            con.close()
            msg= "<h2>username already exist</h2>"
        finally:
            return msg
            con.close()
    else:
        return render_template('home.html')            # render_tempalte to display html page


# %%%%%%  login function for student & teacher  %%%%%%%
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']

        usertype = request.form['option']  # check user teacher or student
        try:
            with sqlite3.connect("users.sqlite3") as con:
                if usertype=="student":
                    data=con.execute("select *from students where (username='{}' and password='{}')".format(username,password))
                    row=data.fetchall()

                    if len(row)==1:
                        session["username"]=username
                        return render_template('Assignment.html')
                        con.close()
                    else:
                        return redirect('/login')
                        con.close()
                else:
                    data = con.execute("select *from teachers where (username='{}' and password='{}')".format(username, password))
                    row = data.fetchall()
                    print(len(row))
                    if len(row) == 1:
                        session["username"]=username
                        return redirect('/viewassignment')
                        con.close()
                    else:
                        return redirect('/login')
                        con.close()

        except:
            return "Unknown Error!!!"
    else:
        return render_template('login.html')


# %%%%%%  Function to upload assignment by student %%%%%%%
@app.route('/upload', methods=['POST','GET'])
def upload():
    if request.method=='POST':
        with sqlite3.connect("users.sqlite3") as con:
            assignemt=request.form['assignment']
            con.execute("UPDATE students SET assignment = '{}' WHERE username='{}'".format(assignemt,session["username"]))
            con.commit()
            return "<h2>assignment uploaded!!!</h2><br><a href='/'>Back</a>"
            con.close()

    else:
        return render_template('Assignment.html')


# %%%%%%  Function to view assignment by teacher %%%%%%%
@app.route('/viewassignment')
def viewassignment():
    assignments=[]
    with sqlite3.connect("users.sqlite3") as con:
        data=con.execute("select course from teachers WHERE username='{}'".format(session["username"]))
        course = data.fetchall()
        data=con.execute("select course,student_id,name,assignment from students")
        d1 = data.fetchall()

        for i in d1:
            if i[0]==course[0][0] and (i[3] is not None):
                assignments.append(str('Student Name:'+i[2]+'\n'+'Student ID:'+i[1]+'\nStudent Assignment\n\n'+i[3]))
        # print(assignments)

    return render_template("viewassignment.html",content=assignments)


# %%%%%%  Login for admin  %%%%%%%
@app.route('/adminlogin', methods=['POST', 'GET'])
def adminlogin():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        try:
            with sqlite3.connect("users.sqlite3") as con:
                data = con.execute("select *from admin_account where (username='{}' and password='{}')".format(username, password))
                row = data.fetchall()
                if len(row) == 1:
                    return redirect('/admin/')
        except:
            return "<h2>Unknown Error</h2><br><a href='/'>Back</a>"

    else:
        return render_template("adminlogin.html")


# Database Models or Tables declaration (for student,teacher & admin)
class students(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    student_id=db.Column(db.String(50))
    name=db.Column(db.String(100))
    email=db.Column(db.String(100))
    username=db.Column(db.String(100),unique=True)
    password=db.Column(db.String(100))
    address=db.Column(db.String(100))
    phone_number=db.Column(db.String(100))
    course=db.Column(db.String(100))
    assignment=db.Column(db.String(100000))
    def __init__(self,student_id,name,email,username,password,address,phone_number,course,assignment):
        self.id=id
        self.student_id=student_id
        self.name=name
        self.email=email
        self.username=username
        self.password=password
        self.address=address
        self.phone_number=phone_number
        self.course=course
        self.assignment=assignment

class teachers(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    teacher_id=db.Column(db.String(50))
    name=db.Column(db.String(100))
    email=db.Column(db.String(100))
    username=db.Column(db.String(100),unique=True)
    password=db.Column(db.String(100))
    address=db.Column(db.String(100))
    phone_number=db.Column(db.String(100))
    course=db.Column(db.String(100))
    def __init__(self,teacher_id,id,name,email,username,password,address,phone_number,course):
        self.id=id
        self.teacher_id=teacher_id
        self.name=name
        self.email=email
        self.username=username
        self.password=password
        self.address=address
        self.phone_number=phone_number
        self.course=course

class admin_account(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50))
    password=db.Column(db.String(100))

    def __init__(self, id,username, password):
        self.id = id
        self.username = username
        self.password = password


# %%%%%% method to create view for database models/tables in admin view
admin.add_view(ModelView(students,db.session))
admin.add_view(ModelView(teachers,db.session))
admin.add_view(ModelView(admin_account,db.session))


# %%%%%%%   to run application  %%%%%%%%
if __name__=="__main__":
    db.create_all()          # create tables if not created
    app.run(debug=True)