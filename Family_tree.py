class Member():

        def __init__(self):
            self.name = None
            self.last_name = None
            self.gender = None
            self.mother = None
            self.father = None
            self.spouse = None
            self.children = None
        
    
        def __str__(self):
            mother = 0
            if type(self.mother) == str:
                mother = self.mother
            elif isinstance(self.mother, Member):
                mother = (self.mother).name
                
            father = 0
            if type(self.father) == str:
                father = self.father
            elif isinstance(self.father, Member):
                father = (self.father).name
            
            spouse = 0
            if type(self.spouse) == str:
                spouse = self.spouse
            elif isinstance(self.spouse, Member):
                spouse = (self.spouse).name
            
#         Not sure how to print out children's names for both options, when it is a string and when it is an instance of a class. 
#             children = []
#             for i in self.children:
#                 if type(i) == str:
#                     i = i
#                     children = (', '. join(str(x) for x in self.children) 
#                 if isinstance(self.children, Member):           
#                         i = str((self.children).name)
#                         children.append [i]
#                         children = (', '. join(str(x) for x in children)   

            children = 0
            if type(self.children) == str:
                children = self.children
            elif isinstance(self.children, Member):
                children = (self.children).name
                
                
            return (f"{self.name}'s record includes: \nName: {self.name} \nLast_name: {self.last_name} \nGender: {self.gender} \nMother: {mother} \nFather: {father} \nSpouse: {spouse} \nChildren: {children}") 

def get_member(name, last_name, gender, mother, father, spouse, children):
    member = Member()
    member.name = name
    member.last_name = last_name
    member.gender = gender
    member.mother = mother
    member.father = father
    member.spouse = spouse
    member.children = children
    return member 

Yana = get_member("Yana", "Dieringer", "Female", "Lubov", "Bogdan", "Ambrose", "Albert") 
Albert = get_member("Albert", "Dieringer", "Male", Yana, "Ambrose", None, None)
Margaret = get_member("Margaret", "Dieringer", "Female", "Fanie", "Albert_Sr_1", "Alan", "Ambrose")
Alan = get_member("Alan", "Dieringer", "Male", "Margaret_Sr", "Albert_Sr_2", "Margaret", "Ambrose")
Ambrose = get_member("Ambrose", "Dieringer", "Male", Margaret, Alan, Yana, Albert)

print (Yana)

print (Margaret)

