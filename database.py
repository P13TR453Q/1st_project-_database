import pickle
#pickle enables us to save and load file by using an .txt file.

#Commands list:
print("Commands: \n 1 = adds an element\n 2 = shows all elements and their parameters\n 3 = deletes an element(if there are two elements with the same name, deletes both!)\n Type anything else to save the data and close the program.")

#Our main code:
class Dana():
  def __init__(self,name,parameter):
    self.name=name
    self.parameter=parameter
    
#Saving process:    
try:
  with open('baza.txt','rb') as x:
    Data_List = pickle.load(x)
except:
  Data_List=[]

#The commands coded:
while True:
  menu = input("Select number:")

#Adding our data:
  if menu == "1":
    Data_List.append(Dana(input("Name: "),input("Parameter: ")))


#The data list view:
  elif menu == "2":
    a = len(Data_List)
    print(f"Threre are {a} elements in this database")
    for pack in Data_List:
      print(f'{pack.name} - {pack.parameter} ')
 
#Deleting data: 
  elif menu == "3":
    c = len(Data_List)
    if c == 0:
      print("You have no data in your database")
    else:
      y = input("Select an element: ")
    for pack in Data_List:
      if y == pack.name:
        Data_List.remove(pack)
        print(f"Deleted {pack.name}.")
      elif y != pack.name:
        print("there is no element named "+ y)

#Saving process:
  else:
    with open('baza.txt', 'wb') as z:
      pickle.dump(Data_List, z)
    break


#Work time ~2hours