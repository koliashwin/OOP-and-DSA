# class is basically an user define datatype. it contains bluprints or prototype form which object are being created.
# object is an entity that has state and bahaviour assosiated with it

class Anime:

    # attributes
    name= ""
    MC= ""
    rating= 0

# create objects form class
obj1 = Anime()
obj1.name = "Naruto"
obj1.MC = "dattebayo"
obj1.rating = 4.7

obj2 = Anime()
obj2.name = "One Piece"
obj2.MC = "mugiwara"
obj2.rating = 4.9

# access attributes
print(f"{obj1.name} is famous for {obj1.MC} and has ratting of {obj1.rating}")
print("{} is famous for {} and has ratting of {}".format(obj2.name, obj2.MC, obj2.rating))
