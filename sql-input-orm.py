from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for "Programmer" table
class User(base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    location = Column(String)
    favorite_food = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# Adding a record
print("Please enter your details")
fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
email = input("Enter your email: ")
location = input("Enter your location: ")
ffood = input("What is your favorite food?: ")
confirmation = input(f"Add {fname} {lname}, {email}, {location}, {ffood} (y/n): \n")


if confirmation == "y":
    # Creating a new User record
    new_user=fname + "_" + lname
    new_user = User(
        first_name=fname,
        last_name=lname,
        email=email,
        location=location,
        favorite_food=ffood
    )
    session.add(new_user)
    session.commit()
    print("User added successfully!")
else:
    print("User not added")


# query the database to find all programmers
users = session.query(User)
for data in users:
    print(
        data.id,
        data.first_name + " " + data.last_name,
        data.email,
        data.location,
        data.favorite_food,
        sep=" | "
    )


print()
print("Favorite Foods :)")
for i in range(1, data.id +1):
    data = session.query(User).filter_by(id=i).first()
    print(data.favorite_food)

