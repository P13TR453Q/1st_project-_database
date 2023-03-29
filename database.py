import pickle

class Dana():
  def __init__(self,name,parameter):
    self.name=name
    self.parameter=parameter
    self.parameter2=0
    
try:
  with open('baza.txt','rb') as x:
    Data_List = pickle.load(x)
except:
  Data_List=[]

while True:
  menu = input("Select option:")
  
  if menu == "1":
    Data_List.append(Dana(input("Name: "),input("Parameter: ")))
#Adding data
  elif menu == "2":
    a = len(Data_List)
    print(f"Threre are {a} elements in this database")
    for pack in Data_List:
      print(f'{pack.name} - {pack.parameter} ')
 #Data List   
  
  elif menu == "3":
    y = input("Select an element: ")
    if y in Data_List:
      Data_List.remove(y)
    else:
      print(f"error - theres no element named {y}")
#Deleting Data
  else:
    with open('baza.txt', 'wb') as z:
      pickle.dump(Data_List, z)
    break