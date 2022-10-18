from tkinter import*
root = Tk()

root.geometry("600x600")
root.title("Adding Citizens")

class Citizen:
    def __init__(self, name, age, dob, id_number):
        self.citizen_name = name
        self.citizen_age = age
        self.citizen_dob = dob
        self.citizen_id = id_number
    
    def add_citizen(self):
        print("Name: " + self.citizen_name)
        print("Age: " + str(self.citizen_age))
        print("Date of Birth: " + self.citizen_dob)
        print("Citizen Id: " + self.citizen_id)
        print("Citizen Added")
        
citizen1 = Citizen("Peter",18,"October 9 2012","0198")
citizen1.add_citizen()

citizen2 = Citizen("Sophie",20,"October 9 2010","0199")
citizen2.add_citizen()