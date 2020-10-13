class Member():

        def __init__(self):
            self.index = None
            self.name = None
            self.last_name = None
            self.gender = None
            self.mother = None
            self.father = None
            self.spouse = None     
            self.children = []    
    
        def __str__(self): 
            
            return (f"""{self.name}'s record includes: 
            Name: {self.name} 
            Last_name: {self.last_name} 
            Gender: {self.gender} 
            Mother: {(self.mother).name} 
            Father: {(self.father).name} 
            Spouse: {(self.spouse).name} 
            Children: {self.children}""") 
        
        def add_child(self,member):
            if self.children == None:
                self.children = []
            self.children.append(member)

def create_member(index,name, last_name, gender, mother, father, spouse, children):
    member = Member()
    member.name = name
    member.last_name = last_name
    member.gender = gender
    member.mother = mother
    member.father = father
    member.spouse = spouse
    member.children = children
    return member 

members = []

def add_to_members(member):
    members.append(member)



def create_records():
    records = {} 

    for member in members:
        record = []
        if member.father == None:
            record.append(member.father)
        if member.mother == None:
            record.append(member.mother)
        else: 
            record.append(member.father.name)
            record.append(member.mother.name)  
        key = member.name
        records[key] = record 
    return (records)


def print_records(member):
    records = create_records()
    sequence_list = []
    member = member.name
    sequence_list.append(member)

    for each in records:
        index = 0
        while member != None: 
            father = records[member][0]
            mother = records[member][1]
            sequence_list.append (father)
            sequence_list.append (mother)
            index += 1
            member = sequence_list[index]

    print (sequence_list [0])
    x = 1
    y = 3
    i = 1
    for each in sequence_list:
        if each == None:
            break
        else:
            l = sequence_list[x:y]
            print (*l, sep = "   ")
            x = y
            y = (y*2)+1
            


Feder = create_member("10000001", "Fedor", "Fevralyov", "Male", None, None, None, None)
Lukeria = create_member("10000002", "Lukeria", "Fevralyov", "Female", None, None, Feder, None)
Maria = create_member("10000003", "Maria", "Grinyenkova", "Female", None, None, None, None)
Grigoriy = create_member("10000004", "Grigoriy", "Grinyenkov", "Male", None, None, Maria, None)
Lubov = create_member("10000005","Lubov","Grinyenkova", "Female", Lukeria, Feder, None, None)
Bogdan = create_member("10000006", "Bogdan", "Grinyenkov", "Male", Maria, Grigoriy, Lubov, None)
Roman = create_member("10000007","Roman", "Grinyenkov", "Male", Lubov, Bogdan, None,  None)
Yana = create_member("10000008","Yana", "Dieringer", "Female", Lubov, Bogdan, None,  None) 
Fanie = create_member("10000009","Fanie", "Khan", "Female", None, None, None,  None)
Albert_Sr_1 = create_member("10000010","Albert_Sr_1", "Khan", "Male", None, None, Fanie,  None)
Margaret_Sr = create_member("10000011","Margaret_Sr", "Dieringer", "Female", None, None, None,  None)
Albert_Sr_2 = create_member("10000012","Albert_Sr_2", "Dieringer", "Male", None, None, Margaret_Sr,  None)
Margaret = create_member("10000013","Margaret_JR", "Dieringer", "Female", Fanie, Albert_Sr_1, None, None)
Alan = create_member("10000014","Alan", "Dieringer", "Male", Margaret_Sr, Albert_Sr_2, Margaret,  None)
Ambrose = create_member("10000015","Ambrose", "Dieringer", "Male", Margaret, Alan, Yana, None)
Albert = create_member("10000016","Albert", "Dieringer", "Male", Yana, Ambrose, None, None)


add_to_members(Feder)
add_to_members(Lukeria)
add_to_members(Maria)
add_to_members(Grigoriy)
add_to_members(Lubov)
add_to_members(Bogdan)
add_to_members(Roman)
add_to_members(Yana)
add_to_members(Fanie)
add_to_members(Albert_Sr_1)
add_to_members(Margaret_Sr)
add_to_members(Albert_Sr_2)
add_to_members(Margaret)
add_to_members(Alan)
add_to_members(Ambrose)
add_to_members(Albert)



print_records(Yana)