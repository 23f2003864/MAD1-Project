from app import app
from flask import render_template,redirect,url_for,session,flash,request
from controllers.models import *
@app.route("/index",methods = ["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/")
def init():
    return render_template("login.html")

@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email').lower()
        passwrd = request.form.get('psswrd')

        user = User.query.filter_by(email= email).first()


        if user and user.password == passwrd:
            session['user']=user.username
            session['role']=user.role.role_name
            
            flash('Login Succesful!','success')
            if session['role'] == 'user':
                return redirect(url_for('user'))
            
            return redirect(url_for('admin'))
        else:
            flash("User not Found ! Plz register to login","danger")
    return render_template("login.html")

@app.route("/usermenu")
def usermenu():
    return render_template("usermenu.html")

@app.route("/user")
def user():
    return render_template("user.html")

@app.route("/dashboard")
def admin_dashboard():
    return render_template("admin_dashboard.html")

@app.route("/admin")
def admin():
    return render_template("adminbase.html")

@app.route("/lotspace")
def lotspace():
    return render_template("lotspace.html")



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        usrnm = request.form.get('usrnm')
        eml = request.form.get('eml')
        psswrd = request.form.get('psswrd')

        # Optional: Check for existing user
        existing_user = User.query.filter_by(username=usrnm).first()
        if existing_user:
            flash('Username already exists. Try another one.')
            return redirect(url_for('register'))
        
        # Create new user
        new_user = User(username=usrnm, email=eml, password=psswrd, role_id = 2 )
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! Please login.')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route("/createlot",methods = ["GET","POST"])
def createlot():
    if request.method == "POST":
        prmlocationname = request.form.get("prime_location_name")
        pph = request.form.get("price_per_hour")
        address = request.form.get("address")
        pin = request.form.get("pincode")
        max_num = int(request.form.get("max_num_of_spots")) # intentionally added int() function because it is causing trouble when creating spots

        

        #crt new lot
        new_lot = ParkingLot(prime_location_name=prmlocationname,price_per_hour=pph,address=address,pincode=pin,Max_num_of_spots=max_num )
        db.session.add(new_lot)
        db.session.commit()
        for i in range(1,int(max_num)+1):
            spot = Parking_spot(lot_id=new_lot.id,spot_number= i , status = "Active")
            db.session.add(spot)
            db.session.commit()
        flash('Lot created successfully')
        return redirect(url_for('index'))
    return render_template("createlot.html")

@app.route("/lot_profile/<int:lot_id>",methods = ["GET","POST"])
def lotmaster(lot_id):
    lot = ParkingLot.query.get_or_404(lot_id)
    if request.method=="POST":
        #Following steps will allow us to retrieve the dta frm the form
        lot.prime_location_name = request.form['prime_location_name']
        lot.price_per_hour = int(request.form['price_per_hour'])
        lot.address = request.form['address']
        lot.pincode = request.form['pincode']
        lot.Max_num_of_spots = int(request.form['max_num_of_spots'])
        #By the fllwng we'll add the data to database
        db.session.commit()
        flash('Lot Updated Successfully')
        return redirect(url_for('index'))
    return render_template("lot_profile.html",lot=lot)

@app.route("/delete_lot/<int:lot_id>",methods = ["GET","POST"])
def dlt_lot(lot_id):
    lot=ParkingLot.query.get_or_404(lot_id)
    if request.method=="POST":
        Parking_spot.query.filter_by(lot_id=lot_id).delete()        
        db.session.delete(lot)
        db.session.commit()
        flash('Lot Deleted Successfully','warning')
    return redirect(url_for('index'))

@app.route("/confirm_delete_lot/<int:lot_id>",methods = [ "GET","POST"])
def cnfrmdlt(lot_id):
    lot=ParkingLot.query.get_or_404(lot_id)
    lid=lot.id
    return render_template("confirmdlt.html",lot=lot,lid=lid)