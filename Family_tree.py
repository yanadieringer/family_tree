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
            
            return (self.name)
        
        def add_child(self,member):
            if self.children == None:
                self.children = []
            self.children.append(member)



def create_member(member, file, code):
    import csv
    data = open (file, encoding = code)
    csv_data = csv.reader (data)
    data_lines = list(csv_data)

    for line in data_lines[1:]:  
        if member == line [0]: 
            member = Member()
            member.name = line[1]
            member.index = line[2]
            member.last_name = line[3]
            member.gender = line[4]
            member.mother = line[5]
            member.father = line[6]
            member.spouse = line[7]
            member.children = line[8]
    return (member)


def printInorder(member, indentation):
    member.left = member.mother
    member.right = member.father

    if member.left=="Null" or member.right =="Null":
        print ("                                      " + f"{member}")
        return
    else: 
        indentation += "        "
        # First recur on left child 
        printInorder(member.left, indentation) 

        # then print the data of node 
        print ("")
        print(indentation + f"{member}"),

        # now recur on right child 
        printInorder(member.right, indentation) 




def printPostorder(member, indentation): 
    member.left = member.mother
    member.right = member.father

    if member.left== None or member.right ==None:
        print ("                                      " + f"{member}")
        return

    else:

        indentation += "        "
        # First recur on left child 
        printPostorder(member.left, indentation) 
  
        # the recur on right child 
        printPostorder(member.right, indentation) 
  
        # now print the data of node 
        print ("")
        print(indentation + f"{member}"),

Feder = create_member("Feder", "/Users/ef5j/git_repo/Members_Information.csv", "utf-8-sig")
Lukeria = create_member("Lukeria", "/Users/ef5j/git_repo/Members_Information.csv", "utf-8-sig")
Maria = create_member("Maria", "/Users/ef5j/git_repo/Members_Information.csv", "utf-8-sig")
Grigoriy = create_member("Grigoriy", "/Users/ef5j/git_repo/Members_Information.csv", "utf-8-sig")
Lubov = create_member("Lubov", "/Users/ef5j/git_repo/Members_Information.csv", "utf-8-sig")
Bogdan = create_member("Bogdan", "/Users/ef5j/git_repo/Members_Information.csv", "utf-8-sig")
Roman = create_member("Roman", "/Users/ef5j/git_repo/Members_Information.csv", "utf-8-sig")
Yana = create_member("Yana", "/Users/ef5j/git_repo/Members_Information.csv", "utf-8-sig")
Fanie = create_member("Fanie", "/Users/ef5j/git_repo/Members_Information.csv", "utf-8-sig")
Albert1 = create_member("Albert1", "/Users/ef5j/git_repo/Members_Information.csv", "utf-8-sig")
Margaret1 = create_member("Margaret1", "/Users/ef5j/git_repo/Members_Information.csv", "utf-8-sig")
Albert2 = create_member("Albert2", "/Users/ef5j/git_repo/Members_Information.csv", "utf-8-sig")
Margaret = create_member("Margaret", "/Users/ef5j/git_repo/Members_Information.csv", "utf-8-sig")
Alan = create_member("Alan", "/Users/ef5j/git_repo/Members_Information.csv", "utf-8-sig")
Ambrose = create_member("Ambrose", "/Users/ef5j/git_repo/Members_Information.csv", "utf-8-sig")
Albert = create_member("Albert", "/Users/ef5j/git_repo/Members_Information.csv", "utf-8-sig")

Lukeria.spouse = Feder
Feder.spouse = Lukeria
Grigoriy.spouse = Maria
Maria.spouse = Grigoriy
Lubov.mother = Lukeria
Lubov.father = Feder
Bogdan.mother = Maria
Bogdan.father = Grigoriy
Bogdan.spouse = Lubov
Lubov.spouse = Bogdan
Roman.father = Bogdan
Roman.mother = Lubov
Yana.father = Bogdan
Yana.mother = Lubov
Albert1.spouse = Fanie
Fanie.spouse = Albert1
Margaret1.spouse = Albert2
Alan.mother = Margaret1
Alan.father = Albert2
Margaret.mother = Fanie
Margaret.father = Albert1
Alan.spouse = Margaret
Ambrose.mother = Margaret
Ambrose.father = Alan
Ambrose.spouse = Yana
Yana.spouse = Ambrose
Albert.mother = Yana
Albert.father = Ambrose
printInorder(Albert, " ")
