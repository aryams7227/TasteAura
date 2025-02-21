from flask import Flask,render_template,request
app=Flask(__name__)
import mysql.connector
connection = mysql.connector.connect(host='localhost',user='root',password='admin',database='ict')
mycursor = connection.cursor()
user_dict={'Anjo':'Joy','Bijohn':'Shiju','Arya':'Ms','Jain Mariya':'Jimmy','Jain':'Jaison'}
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/user',methods=['POST'])
def user():
    username=request.form["username"]
    pwd=request.form["password"]
    if username not in user_dict:
        return render_template('login.html',msg="Invalid Username")
    elif user_dict[username]!=pwd:
        return render_template('login.html',msg="Invalid Password")
    else:
        return render_template('user.html',msg=username+" "+pwd)
    
    
@app.route('/add',methods=['POST'])
def add():
    return render_template('add.html')
@app.route('/addrest',methods=['GET','POST'])
def read():
    if request.method=='POST':
        name=request.form.get('name')
        address=request.form.get('address')
        district=request.form.get('district')
        time=request.form.get('time')
        number=request.form.get('number')
        img=request.form.get('img')
        park=request.form.get('park')
        dine=request.form.get('dine')
        food=request.form.get('food')
        if district=="Thrissur":
            query="insert into thrissur values (%s,%s,%s,%s,%s,%s,%s,%s)"
            data=(name,address,time,number,park,dine,food,img)
            mycursor.execute(query,data)
            connection.commit()
            return render_template('user.html')
        elif district=="Ernakulam":
            query="insert into ekm values (%s,%s,%s,%s,%s,%s,%s,%s)"
            data=(name,address,time,number,park,dine,food,img)
            mycursor.execute(query,data)
            connection.commit()
            return render_template('user.html')
        elif district=="Palakkad":
            query="insert into palakkad values (%s,%s,%s,%s,%s,%s,%s,%s)"
            data=(name,address,time,number,park,dine,food,img)
            mycursor.execute(query,data)
            connection.commit()
            return render_template('user.html')
        

    
@app.route('/view',methods=['POST'])
def view():
    return render_template('view.html')


@app.route('/delete',methods=['POST'])
def delete():
    return render_template('delete.html')
@app.route('/deldst',methods=['POST'])
def deldst():
    global deldt
    if request.method=='POST':
        deldt=request.form.get('district')
        if deldt=='Thrissur':
            mycursor.execute('select * from thrissur')
            dt=mycursor.fetchall()
            return render_template('delete.html',dt=dt)
        elif deldt=='Ernakulam':
            mycursor.execute('select * from ekm')
            dt=mycursor.fetchall()
            return render_template('delete.html',dt=dt)
        elif deldt=='Palakkad':
            mycursor.execute('select * from palakkad')
            dt=mycursor.fetchall()
            return render_template('delete.html',dt=dt)
@app.route('/delrest',methods=['POST'])
def delrest():
    if request.method=='POST':
        name=request.form.get('name')
        if deldt=='Thrissur':
            query="delete from thrissur where name=%s"
            data=(name,)
            mycursor.execute(query,data)
            connection.commit()
            return render_template('user.html')
        elif deldt=='Ernakulam':
            query="delete from ekm where name=%s"
            data=(name,)
            mycursor.execute(query,data)
            connection.commit()
            return render_template('user.html')
        elif dst=='Palakkad':
            query="delete from palakkad where name=%s"
            data=(name,)
            mycursor.execute(query,data)
            connection.commit()
            return render_template('user.html')



@app.route('/thrissur')
def tcr():
    mycursor.execute('select * from thrissur')
    tcr_data=mycursor.fetchall()
    return render_template('thrissur.html',tcr_data=tcr_data)
@app.route('/tpark',methods=['POST'])
def parktcr():
    mycursor.execute("select * from thrissur where parking='yes'")
    tcr_data=mycursor.fetchall()
    return render_template('thrissur.html',tcr_data=tcr_data)
@app.route('/tdine',methods=['POST'])
def dinetcr():
    mycursor.execute("select * from thrissur where dine_in='yes'")
    tcr_data=mycursor.fetchall()
    return render_template('thrissur.html',tcr_data=tcr_data)
@app.route('/tveg',methods=['POST'])
def vegtcr():
    mycursor.execute("select * from thrissur where veg_nonveg='veg'")
    tcr_data=mycursor.fetchall()
    return render_template('thrissur.html',tcr_data=tcr_data)
@app.route('/tnonveg',methods=['POST'])
def nonvegtcr():
    mycursor.execute("select * from thrissur where veg_nonveg='non veg'")
    tcr_data=mycursor.fetchall()
    return render_template('thrissur.html',tcr_data=tcr_data)
@app.route('/tboth',methods=['POST'])
def bothtcr():
    mycursor.execute("select * from thrissur where veg_nonveg='both'")
    tcr_data=mycursor.fetchall()
    return render_template('thrissur.html',tcr_data=tcr_data)


@app.route('/ekm')
def ekm():
    mycursor.execute('select * from ekm')
    ekm_data=mycursor.fetchall()
    return render_template('ekm.html',ekm_data=ekm_data)
@app.route('/epark',methods=['POST'])
def parkekm():
    mycursor.execute("select * from ekm where parking='yes'")
    ekm_data=mycursor.fetchall()
    return render_template('ekm.html',ekm_data=ekm_data)
@app.route('/edine',methods=['POST'])
def dineekm():
    mycursor.execute("select * from ekm where dine_in='yes'")
    ekm_data=mycursor.fetchall()
    return render_template('ekm.html',ekm_data=ekm_data)
@app.route('/eveg',methods=['POST'])
def vegekm():
    mycursor.execute("select * from ekm where veg_nonveg='veg'")
    ekm_data=mycursor.fetchall()
    return render_template('ekm.html',ekm_data=ekm_data)
@app.route('/enonveg',methods=['POST'])
def nonvegekm():
    mycursor.execute("select * from ekm where veg_nonveg='non veg'")
    ekm_data=mycursor.fetchall()
    return render_template('ekm.html',ekm_data=ekm_data)
@app.route('/eboth',methods=['POST'])
def bothekm():
    mycursor.execute("select * from ekm where veg_nonveg='both'")
    ekm_data=mycursor.fetchall()
    return render_template('ekm.html',ekm_data=ekm_data)


@app.route('/palakkad')
def plk():
    mycursor.execute('select * from palakkad')
    plk_data=mycursor.fetchall()
    return render_template('palakkad.html',plk_data=plk_data)
@app.route('/ppark',methods=['POST'])
def parkplk():
    mycursor.execute("select * from palakkad where parking='yes'")
    plk_data=mycursor.fetchall()
    return render_template('palakkad.html',plk_data=plk_data)
@app.route('/pdine',methods=['POST'])
def dineplk():
    mycursor.execute("select * from palakkad where dine_in='yes'")
    plk_data=mycursor.fetchall()
    return render_template('palakkad.html',plk_data=plk_data)
@app.route('/pveg',methods=['POST'])
def vegplk():
    mycursor.execute("select * from palakkad where veg_nonveg='veg'")
    plk_data=mycursor.fetchall()
    return render_template('palakkad.html',plk_data=plk_data)
@app.route('/pnonveg',methods=['POST'])
def nonvegplk():
    mycursor.execute("select * from palakkad where veg_nonveg='non veg'")
    plk_data=mycursor.fetchall()
    return render_template('palakkad.html',plk_data=plk_data)
@app.route('/pboth',methods=['POST'])
def bothplk():
    mycursor.execute("select * from palakkad where veg_nonveg='both'")
    plk_data=mycursor.fetchall()
    return render_template('palakkad.html',plk_data=plk_data)


if __name__=='__main__':
    app.run(debug=True)