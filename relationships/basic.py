from models import db, Puppy, Owner, Toy

# Create 2 Puppies
rufus = Puppy('Rufus')
fido = Puppy('Fido')


# Add puppies to DB
db.session.add_all([rufus, fido])
db.session.commit()


#Check the output
print(Puppy.query.all())


rufus = Puppy.query.filter_by(name = 'Rufus').first() # all() will give the list of all puppies udner the name Rufus

# Create owner for Rufus

jose = Owner('Jose', rufus.id)


# Give Rufus some toys
toy1 = Toy('Chew Toy', rufus.id)
toy2 = Toy('Ball', rufus.id)

# Add the owner and toys to DB
db.session.add_all([jose, toy1, toy2])
db.session.commit()

print(Puppy.query.filter_by(name = 'Rufus').first())