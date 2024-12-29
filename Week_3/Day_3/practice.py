#   Static Method

# class method:


class Person():
    name = "Annonymous"

    def changename(self, name):
        self.name = name  # New name attribute
        Person.name = name #Change the class attribute


        
