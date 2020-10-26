#create class
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
            

#read csv file
def read_file(file, code):
    import csv
    data = open (file, encoding = code)
    csv_data = csv.reader (data)
    all_rows = list(csv_data)
    member_list = [] 
    
    for row in all_rows[1:]:  
        member = Member()
        member.name = row[1]
        member.index = row[2]
        member.last_name = row[3]      
        member.gender = row[4]
        member.mother = row[5]
        member.father = row[6]
        member_list.append(member)
        if row[9] == "TRUE":
            root = member
            
    for index, member in enumerate(member_list):

        for each in member_list:            
            if each.mother == member_list[index].index:
                each.mother = member_list[index]


            if each.father == member_list[index].index:
                each.father = member_list[index]
    print (f"The root of the family is {root}.")
    return (root)


# print family tree

def print_family(root, indentation):
    root.left = root.mother
    root.right = root.father
 

    if root.left=="Null" or root.right =="Null":
        print ("                                              " + f"{root}")
        return
    else: 
        indentation += "           "
        
        # first recur on left child 
        print_family(root.left, indentation) 
        
        
        # then print the data of node 

        print ("  ")
        print(f"{indentation}"  + f"{root}")
        print ("  ")


        # now recur on right child 
        print_family(root.right, indentation) 
        

# find any member in the tree

def find_member (root, name):
    
    if root == "Null":
        return
    
    if root.name == name:
        member = root
        print_family(member, "")
        return member

    find_member(root.left, name)

    find_member(root.right, name)


#Test
read_file ("/Users/ef5j/git_repo/Members_Information.csv", "utf-8-sig")

print_family(root, "")
print ("_________________________________________________________________________")

find_member(root, "Ambrose")