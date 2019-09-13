from flask import Flask, render_template,request
import mysql.connector
app=Flask(__name__)
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="mydb"
)
mycururso=mydb.cursor()
@app.route("/")
def home():
    
    return render_template("Home.html",)
 
#  SignIN
@app.route("/singin",methods=['POST','GET'])
def singin():
    if request.method=="POST":
        Uname=request.form.get("uname")
        Upass=request.form.get("pswd")
        print("====================================")
        print(Uname)
        print(Upass)
        print("====================================")
        if Uname =='admin':
            if Upass=='admin':     
                return render_template("adminpanal.html")
        mycururso.execute("select * from users where name =%s",(Uname,))
        endresult=mycururso.fetchone()
        for endresult in endresult:
            print(endresult)
        if endresult != None:
            if Upass == endresult:
                print("LOGIN DONE")
                result=Uname
                return render_template("home.html",results=result)
            else:
                print("Login In NOT Succesful") 
        
         
    
    return render_template("singIn.html")

# Regestration
@app.route("/regestration",methods=["GET","POST"])
def regestration():
    
 
    if request.method=="POST":
        name=request.form.get("name")
        email=request.form.get("email")
        address=request.form.get("address")
        password=request.form.get("password")
        confirm=request.form.get("confirm")
        role="user"
        val=(name,email,address,password,role)
        if password!=confirm:
            return ("PASSWORD 1 And Password 2 MUST be the SAME")
        
        if password==confirm:
            
            mycururso.execute("insert into users (name,email,address,password,role) values (%s,%s,%s,%s,%s)",val)
            mydb.commit()
            return render_template('home.html',results=name)
    return render_template("Regestrtion.html")

@app.route("/admin",methods=['POST','GET'])
def admin():
    if request.method=='GET':
        return render_template('errorPage.html',results="You HAD TO SING IN FIRST IN SingIn Page")
    if request.method=="POST":
        return render_template("{{url_for('admin')}}") 
    return render_template("adminpanal.html")     

    #Error Page
@app.route("/error",methods=['POST','GET'])
def error():   
    return render_template("errorPage.html")
     
     
     
@app.route("/viewusers",methods=['POST','GET'])
def viewusers():
    mycururso.execute("select * from users")
    userresult=mycururso.fetchall()
    
        
    return render_template("viewusers.html",r=userresult) 

@app.route("/edituser",methods=['POST','GET'])
def edituser():
    if request.method=='POST':
        userId=request.form.get("id")
        usename=request.form.get("name_newval")
        useemail=request.form.get("email_newval")
        useaddress=request.form.get("address_newval")
        userole=request.form.get("role_newval")
        usepass=request.form.get("password_newval")
        
        if userId !=None:
            if usename !=None:
                sql_query='Update users set name  = %s where id = %s'
                val=(usename,userId)
                mycururso.execute(sql_query,val)
                mydb.commit()
            elif useemail != None:
                sql_query='Update users set email  = %s where id = %s'
                val=(useemail,userId)
                mycururso.execute(sql_query,val)
                mydb.commit()
            elif useaddress != None:
                sql_query='Update users set address  = %s where id = %s'
                val=(useaddress,userId)
                mycururso.execute(sql_query,val)
                mydb.commit()    
            elif userole != None:
                sql_query='Update users set role  = %s where id = %s'
                val=(userole,userId)
                mycururso.execute(sql_query,val)
                mydb.commit()
            elif usepass != None:
                sql_query='Update users set password  = %s where id = %s'
                val=(usepass,userId)
                mycururso.execute(sql_query,val)
                mydb.commit()       
                     
                
                
                
        
        
         
    return render_template("edituser.html")


# PRODUCTS
@app.route("/products",methods=['GET','POST'])
def products():
    mycururso.execute("select * from product")
    productResult=mycururso.fetchall()
    mydb.commit()
    return render_template('product.html',pr=productResult)



# Add Product
@app.route('/addproduct',methods=['GET','POST'])
def addprouduct():
    # if request.method=='GET':
    #     return render_template('errorPage.html',results="Only Admin Can Add Prouducts")
    if request.method=='POST':
        prouductName=request.form.get('pname')
        prouductdescription=request.form.get('description')
        imagelink=request.form.get('Imgname')
        sql="insert into product(product_name,description,imglink) values (%s,%s,%s)"
        val=(prouductName,prouductdescription,imagelink)
        mycururso.execute(sql,val)
        print("INSERTES DONE")
        mydb.commit()
        
 
    return render_template('addprouduct.html')

@app.route('/deletepage',methods=['GET','POST'])
def deletepage():
    
    if request.method=='POST':
        userdeletedname=request.form.get('delname')
        productdeletedid=request.form.get('prodname')
        if userdeletedname !=None:
            deletequery="DELETE FROM users WHERE users.name= %s "
            deleteval=(userdeletedname,)
            mycururso.execute(deletequery,deleteval)
            mydb.commit()
        if productdeletedid !=None:
            deletequery="DELETE FROM product WHERE product.product_id= %s "
            deleteval=(productdeletedid,)
            mycururso.execute(deletequery,deleteval)
            mydb.commit()
            
    return render_template("deletepage.html")
