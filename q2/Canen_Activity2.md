# Single Inheritance

class Animal:
    def __init__(self, name):
        self._name = name  

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def eat(self):
        print(self.get_name(), "is eating.")

    def sleep(self):
        print(self.get_name(), "is sleeping.")

class Dog(Animal):
    pass

dog1 = Dog("Bruno")
dog1.eat()

dog1.set_name("Buster")
print("Updated Dog Name:", dog1.get_name())
dog1.eat()

dog2 = Dog("Rocky")
dog2.sleep()


# Multilevel Inheritance

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age


class Employee(Person):
    def __init__(self, name, age, job_title, salary):
        super().__init__(name, age)
        self._job_title = job_title
        self._salary = salary

    def get_job_title(self):
        return self._job_title

    def set_job_title(self, job_title):
        self._job_title = job_title

    def get_salary(self):
        return self._salary

    def set_salary(self, salary):
        self._salary = salary


class Manager(Employee):
    def __init__(self, name, age, job_title, salary, department):
        super().__init__(name, age, job_title, salary)
        self._department = department

    def get_department(self):
        return self._department

    def set_department(self, department):
        self._department = department

    def display_details(self):
        print("--- Manager Info ---")
        print("Name:", self.get_name())
        print("Age:", self.get_age())
        print("Job:", self.get_job_title())
        print("Salary:", self.get_salary())
        print("Dept:", self.get_department())


mgr1 = Manager("Alice", 35, "Project Manager", 80000, "IT")
mgr1.display_details()

mgr1.set_salary(90000)
mgr1.set_department("Tech Ops")
print("\nAfter Promotion:")
mgr1.display_details()

mgr2 = Manager("Mark", 40, "HR Head", 75000, "Human Resources")
print("New Manager Name:", mgr2.get_name())


# Hierarchical Inheritance

class Animal:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def eat(self):
        print(self.get_name(), "is eating.")


class Dog(Animal):
    def bark(self):
        print(self.get_name(), "says Woof!")


class Cat(Animal):
    def meow(self):
        print(self.get_name(), "says Meow!")


dog1 = Dog("Bruno")
cat1 = Cat("Kitty")

dog1.eat()
dog1.bark()

cat1.eat()
cat1.meow()

cat1.set_name("Luna")
print("Updated Cat Name:", cat1.get_name())
cat1.meow()

cat2 = Cat("Milo")
cat2.meow()