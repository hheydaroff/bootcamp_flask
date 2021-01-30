from basic import db, Puppy


# Create the database
db.create_all()

# Define some Puppy objects
sam = Puppy('Sammy', 3)
frank = Puppy('Frankie', 4)

# Add all puppy objects to the database as a table
db.session.add_all([sam, frank]) # we could also do db.session.add(sam/ or frank)

# Execute the previously defined commands on saqlalchemy
db.session.commit()

#Check the generated unique ids
print(sam.id)
print(frank.id)


