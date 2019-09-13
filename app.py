from flask import Flask, render_template,request
import mysql.connector
app=Flask(__name__)
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database='mydb' 
   )

mycururso=mydb.cursor()
#mycururso.execute("CREATE DATABASE mydb")#run this row
# 
# Execute This At First time
# mycururso.execute("CREATE TABLE `customer` (`id` int(11) NOT NULL,`name` varchar(255) DEFAULT NULL,`address` varchar(255) DEFAULT NULL)")
# mycururso.execute("INSERT INTO `customer` (`id`, `name`, `address`) VALUES(1, 'John', 'Highway 21');")
# mycururso.execute("CREATE TABLE `product` (`product_name` varchar(15) NOT NULL,`product_id` int(5) NOT NULL,`description` varchar(90) NOT NULL,`imglink` varchar(200) NOT NULL)")
# mycururso.execute("INSERT INTO `product` (`product_name`, `product_id`, `description`, `imglink`) VALUES('Iphone', 5, 'THis Is Iphone 11', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR88t1fMR2bpSyAzmYI-yx2t-NLrU3TuyUS_n0hvdrkVV3Cgze9'),('Macbook Pro', 6, 'This is a macbook Pro', 'https://cnet4.cbsistatic.com/img/F9suzz0c1Q7ghhQoienu2TajkIw=/868x488/2016/10/27/6cd01ecb-40cd-4615-b5f5-82993fbf9419/apple-macbook-pro-13-inch-2016-1765-026.jpg'),('MiBand', 7, 'This Is  a mi band', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSTsJlhB3eg2QzskfNa_DLGWzkuJqVWYSN_vFb5r70sCpOkFkFo'),('galaxy s10', 9, 'This Is galaxy s10', 'https://images-na.ssl-images-amazon.com/images/I/619h1rSUcKL._SX569_.jpg'),('Cannon 4000D', 10, 'This Is Canon 4000D cam', 'https://images-na.ssl-images-amazon.com/images/I/41RV3IWWADL._SX425_.jpg'),('Wireless Keybor', 11, 'This is a Wireless Keybord', 'https://target.scene7.com/is/image/Target/GUEST_25cb8b97-a9ce-4dad-a0b7-1d7142461fc1?wid=488&hei=488&fmt=pjpeg'),('Apple Airpods', 12, 'This is Airpods', 'https://images-na.ssl-images-amazon.com/images/I/41qIPi7taiL._SX385_.jpg'),('VR Box', 13, 'Enjoy With This Amazing VR Box', 'https://rukminim1.flixcart.com/image/832/832/j5lchow0/smart-glass/u/k/4/12-nexus-original-imaevs9sg9egpjzh.jpeg?q=70');")
# mycururso.execute("CREATE TABLE `users` (`id` int(11) NOT NULL,`name` varchar(50) NOT NULL,`email` varchar(30) NOT NULL,`address` varchar(30) NOT NULL,`role` varchar(10) DEFAULT NULL,`password` varchar(30) NOT NULL)")
# mycururso.execute("INSERT INTO `users` (`id`, `name`, `email`, `address`, `role`, `password`) VALUES(19, 'admin', 'admin@admin.com', 'admincity', 'admin', 'admin'),(21, 'Khaled Ahmed', 'khaled.basha144@gmail.com', 'Cairo', 'user', '123456789'),(22, 'Khaled Abd ElFatah', 'khaledabdelfatah200@gmail.com', 'Mansoura', 'user', '123456789'),(23, 'user', 'user@user.com', 'User City', 'user', '123456789');")
# mycururso.execute("ALTER TABLE `customer`ADD PRIMARY KEY (`id`);")
# mycururso.execute("ALTER TABLE `product`ADD PRIMARY KEY (`product_id`);")
# mycururso.execute("ALTER TABLE `users` ADD PRIMARY KEY (`id`);")
# mycururso.execute("ALTER TABLE `customer`MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;")
# mycururso.execute("ALTER TABLE `product`MODIFY `product_id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;")
# mycururso.execute("ALTER TABLE `users`MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;")
# 
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
