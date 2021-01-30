from basic import db, Puppy

# CREATE

my_puppy = Puppy('Rufus', 10)
db.session.add(my_puppy)
db.session.commit()


# READ

all_puppies = Puppy.query.all() # list of puppy objects in the db
print('All Puppies: ', all_puppies)

## Select by ID
puppy_one = Puppy.query.get(1)
print('Puppy One', puppy_one.name)

## Select by name
puppy_frankie = Puppy.query.filter_by(name = 'Frankie')
puppy_frankie.all()


# UPDATE

first_puppy = Puppy.query.get(1)
first_puppy.age =  10
db.session.add(first_puppy)
db.session.commit()

# DELETE
second_pup = Puppy.query.get(2)
db.session.delete(second_pup)
db.session.commit()

## Check it
all_puppies = Puppy.query.all()
print('All puppies after deleting second_pup: ', all_puppies)