from controllers.database import db
from datetime import datetime


class roles(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    role_name = db.Column ( db.String(80),unique= True , nullable = False)
    
#user table
class User(db.Model):  
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    role_id = db.Column(db.Integer,db.ForeignKey(roles.id),nullable = True)

    #relationship

    role = db.relationship('roles', backref ='users')
    
#parking lot 
class ParkingLot(db.Model):
    id = db.Column(db.Integer,primary_key= True)
    prime_location_name = db.Column ( db.String , nullable = False)
    price_per_hour = db.Column(db.Integer,nullable = False)
    address = db.Column(db.String, nullable = False)
    pincode = db.Column(db.String,nullable = False)
    Max_num_of_spots = db.Column ( db.Integer , nullable = False)
    
#parking sopt
class Parking_spot(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    lot_id = db.Column(db.Integer,db.ForeignKey(ParkingLot.id),nullable = True)
    spot_number = db.Column(db.String,nullable = True)
    status = db.Column(db.String(1),nullable = True)
    

#reservation_id
class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    spot_id = db.Column(db.Integer,db.ForeignKey(Parking_spot.id),nullable = True)
    user_id = db.Column(db.Integer,db.ForeignKey(User.id),nullable = True)
    parking_time = db.Column ( db.DateTime,nullable = True)
    leaving_time = db.Column ( db.DateTime , nullable = True )
    parking_cost = db.Column ( db.Integer,nullable = True)
    
class Vehicle(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey(User.id),nullable = True)
    plate_number = db.Column(db.String,nullable = True)
    Vehicle_type = db.Column( db.Enum('2-Wheeler','3-Wheeler','4-Wheeler',name='vehicle_type_enum',nullable = True))



 
