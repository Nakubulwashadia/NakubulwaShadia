#qn 1: University management system
class Person:
    def __init__(self, name, national_id, email):
        self.name = name
        self.national_id = national_id
        self.email = email

    def display(self):
        print(f"Name: {self.name}, ID: {self.national_id}, Email: {self.email}")


class Student(Person):
    def __init__(self, name, national_id, email, reg_no, program):
        super().__init__(name, national_id, email)
        self.reg_no = reg_no
        self.program = program

    def display(self):
        super().display()
        print(f"Reg No: {self.reg_no}, Program: {self.program}")


class Staff(Person):
    def __init__(self, name, national_id, email, emp_no, department):
        super().__init__(name, national_id, email)
        self.emp_no = emp_no
        self.department = department

    def display(self):
        super().display()
        print(f"Employee No: {self.emp_no}, Department: {self.department}")


# Multiple inheritance
class TeachingAssistant(Student, Staff):
    def __init__(self, name, national_id, email, reg_no, program, emp_no, department):
        Student.__init__(self, name, national_id, email, reg_no, program)
        Staff.__init__(self, name, national_id, email, emp_no, department)

    def display(self):
        print("\n--- Teaching Assistant ---")
        Student.display(self)
        print(f"Employee No: {self.emp_no}, Department: {self.department}")


# Test
ta = TeachingAssistant("Alice", "12345", "alice@mail.com",
                      "REG001", "CS", "EMP01", "IT")
ta.display()


#qn 2: Smart City Transport System
class Vehicle:
    def __init__(self, reg_no, manufacturer, speed):
        self.reg_no = reg_no
        self.manufacturer = manufacturer
        self.speed = speed

    def start(self):
        print(f"{self.reg_no} started")

    def stop(self):
        print(f"{self.reg_no} stopped")


class Bus(Vehicle):
    def __init__(self, reg_no, manufacturer, speed, route, capacity):
        super().__init__(reg_no, manufacturer, speed)
        self.route = route
        self.capacity = capacity


class ElectricVehicle:
    def __init__(self, battery, status):
        self.battery = battery
        self.status = status

    def charge(self):
        print("Charging...")


class ElectricBus(Bus, ElectricVehicle):
    def __init__(self, reg_no, manufacturer, speed, route, capacity, battery, status):
        Bus.__init__(self, reg_no, manufacturer, speed, route, capacity)
        ElectricVehicle.__init__(self, battery, status)


# Test
eb = ElectricBus("UAA123", "Toyota", 80, "Route 5", 50, 90, "Not Charging")
eb.start()
eb.charge()


#qn 3: Hospital Information System
class Employee:
    def __init__(self, emp_id, name, contact):
        self.emp_id = emp_id
        self.name = name
        self.contact = contact

    def display(self):
        print(self.emp_id, self.name, self.contact)


class Doctor(Employee):
    def __init__(self, emp_id, name, contact, specialization, fee):
        super().__init__(emp_id, name, contact)
        self.specialization = specialization
        self.fee = fee


class Researcher(Employee):
    def __init__(self, emp_id, name, contact, research_area, publications):
        super().__init__(emp_id, name, contact)
        self.research_area = research_area
        self.publications = publications


class DoctorResearcher(Doctor, Researcher):
    def __init__(self, emp_id, name, contact, specialization, fee, research_area, publications):
        Doctor.__init__(self, emp_id, name, contact, specialization, fee)
        Researcher.__init__(self, emp_id, name, contact, research_area, publications)

    def display(self):
        super().display()
        print(self.specialization, self.research_area)


#qn 4: E-Commerce Platform
class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price


class Discountable:
    def __init__(self, discount):
        self.discount = discount

    def apply_discount(self, price):
        return price - (price * self.discount / 100)


class Taxable:
    def __init__(self, tax):
        self.tax = tax

    def apply_tax(self, price):
        return price + (price * self.tax / 100)


class FinalProduct(Product, Discountable, Taxable):
    def __init__(self, pid, name, price, discount, tax):
        Product.__init__(self, pid, name, price)
        Discountable.__init__(self, discount)
        Taxable.__init__(self, tax)

    def final_price(self):
        price = self.apply_discount(self.price)
        return self.apply_tax(price)


# Test
p = FinalProduct(1, "Laptop", 1000, 10, 18)
print("Final Price:", p.final_price())


#qn 5: Online Learning Platform
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def login(self):
        print(f"{self.username} logged in")


class Student(User):
    def enroll(self):
        print("Enrolled in course")

    def view_grades(self):
        print("Viewing grades")


class Instructor(User):
    def create_course(self):
        print("Course created")

    def grade(self):
        print("Grading assignment")


class StudentInstructor(Student, Instructor):
    pass


# Test
u = StudentInstructor("john", "john@mail.com")
u.login()
u.enroll()
u.create_course()


#FINAL EXAM: Internship Portal
class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def login(self):
        print(f"{self.name} logged in")

    def logout(self):
        print(f"{self.name} logged out")

    def display_profile(self):
        print(self.user_id, self.name, self.email)


class Student(User):
    def __init__(self, user_id, name, email, reg_no, course):
        super().__init__(user_id, name, email)
        self.reg_no = reg_no
        self.course = course

    def display_profile(self):
        super().display_profile()
        print(self.reg_no, self.course)


class Supervisor(User):
    def __init__(self, user_id, name, email, company, emp_id):
        super().__init__(user_id, name, email)
        self.company = company
        self.emp_id = emp_id

    def display_profile(self):
        super().display_profile()
        print(self.company, self.emp_id)


class StudentRepresentative(Student, Supervisor):
    def __init__(self, user_id, name, email, reg_no, course, company, emp_id):
        Student.__init__(self, user_id, name, email, reg_no, course)
        Supervisor.__init__(self, user_id, name, email, company, emp_id)

    def display_profile(self):
        print("\n--- Student Representative ---")
        Student.display_profile(self)
        print(self.company, self.emp_id)


# Test
sr = StudentRepresentative("U01", "Alice", "alice@mail.com",
                           "REG100", "CS", "Google", "EMP22")

sr.login()
sr.display_profile()
print(StudentRepresentative.mro())