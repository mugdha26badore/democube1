class employee:
    def __init__(self):
        self.firstname = ""
        self.lastname = ""

    def get_firstname(self):
        return self.firstname
    def get_lastname(self):
        return self.lastname
    def set_firstname(self, f):
        self.firstname = f
    def set_lastname(self, l):
        self.lastname = l
    
    def get_fullname(self):
        a = self.firstname[0].upper() + self.firstname[1:].lower()
        b = self.lastname[0].upper() + self.lastname[1:].lower()
        return f"My name is {a} {b}"
    
def main():
    emp = employee()
    emp.set_firstname(input("Enter first name: "))
    emp.set_lastname(input("Enter last name: "))
    print(emp.get_fullname())
    
if __name__ == "__main__":
    main()