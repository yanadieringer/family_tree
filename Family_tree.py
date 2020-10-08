class Member():

        """
        Comments from Gil (10/08)
        While it is very convenient to have the object ask the user for input at the moment of creation, it also limits
        the reusability of the class.  For example, this class could not be used for an application that reads family members
        from a database or receives them from a web UI or API.
        This ties to the single responsibility principle.  The Member class is mean to encapsulate everything and only things
        related to a member. Having functionality that prompts are user makes it know about the user interface, which is not
        one of its responsibilities.
        """
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
            


