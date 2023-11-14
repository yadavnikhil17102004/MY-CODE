
class employee:
     company = "Google"

     employes = 1000
     salary = 26000 

     def __init__(self, name, branch,):
        self.name = name
        self.branch = branch
      

     def getdetails(self):
         print(f"Name :{self.name}")
         print(f"Branch assigned is :{self.branch}")
         print(f"Salary provided :{self.salary}")
         print(f"Employee capacity :{self.employes}")

class programmer(employee):
    employes = 500
    salary = 30000

rohan  = employee("Rohan", "pune")
mohit = programmer("Mohit", "mumbai")

rohan.getdetails()
mohit.getdetails()