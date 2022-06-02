class Employee:
    def message(self):
        print("this is emp class")
class Department(Employee):
    def messages(self):
        print("This depart class inherited from")
emp= Employee()
emp.message()
print("---------")
dept=Department()
dept.message()
