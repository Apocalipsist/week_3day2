class Employee:
    raise_amount = 1.05
    
    def __init__(self, first_name, last_name, position, salary):
        self.first = first_name
        self.last = last_name
        self.title = position
        self.salary = salary
        self.email = first_name + " " + last_name + "@taurusdigital.org"
        
    def change_last_name(self, new_last_name):
        self.last_name = new_last_name.title()
        self.email = self.first_name.lower() + '.' + new_last_name.lower()+'@taurusdigital.org'
        
        
    def apply_raise(self):
        self.salary *= self.raise_amount #self.salary = self.salary
        print(f'Congrats {self.full_name()}, You have recieved a raise your new amount is{self.salary}')
        
        
class Sales(Employee):
    
    def __init__(self, first_name, last_name, position, salary, phone):
        super().__init__(first_name, last_name, position, salary,)
        self.phone = phone
        
        
    def get_full_name(self):
        return f"{self.first.title()} {self.last.title()}"
        
    def send_email(self):
        return f"Dear {self}, Thank you for your interest in our product. Please let me know if you have any questions. My email is {self.email} or my phone number is {self.phone}. Thanks, {Employee.get_full_name}"
        
class Development(Employee):
    
    def __init__(self, first_name, last_name, position, salary):
        super().__init__(first_name, last_name, position, salary)
        
        
    def work(self):
        return f"{self.get_full_name()}is writing code"
    
    

emp1 = Sales("Apocalipsis", "Torres", "Sales", 50000, "208-933-7721")
emp2 = Sales("Apri", "O'Neil", "Sales", 50000, "208-933-7721")


print(emp1.__dict__)

        
        


        
        
        
        
        