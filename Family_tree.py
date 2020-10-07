class Member():

        def __init__(self):
            self.name = input("Enter first name: ")
            self.gender = input("Enter your gender: ")
            self.family_surname = input("Enter your family surname: ")
            self.married_surname = input("Enter your married surname: ")
            self.father_name = input("Enter your father's first name: ")
            self.father_surname = input("Enter your father's surname: ")
            self.mother_name = input("Enter your mother's name: ")
            self.mother_surname = input("Enter your mother's surname: ")


        def __str__(self):
            return (f"{self.name}'s record includes: \nName: {self.name} \nGender: {self.gender} \nFamily surname: {self.family_surname} \nMarried surname: {self.married_surname} \nFather's name: {self.father_name} \nFather's surname: {self.father_surname} \nMother's name: {self.mother_name} \nMother's surname: {self.mother_surname}")  

class Family(Member):
        def __init__(self, member):
            self.family_surname = member.family_surname
        
        def add_to_family():
            # if family_surname == "d":
            


