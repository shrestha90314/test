import datetime as dt


class Employee:
    # Regular methods take automatically instance as a first argument
#test
    raise_amount = 1.04
    number_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = first+'.'+last+'@company.com'
        # when we define the the variable in the calss it will not change and increase the value everyt time we call the instance
        Employee.number_of_emps += 1
# Class variables are the variable that are shared among the all instance of that class.

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    def fullname(self):  # methods
        return f'{self.first} {self.last}'

    # @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    def apply_raise(self):
        # we can access raise_amount by self.raise_amount or Employee.raise_amount
        self.pay = int(self.pay * self.raise_amount)

    @classmethod  # Pass class as the first argument
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        cls(first, last, pay)

    @staticmethod  # if you dont access instance or class with in the functhon
    def is_work_day(day):
        if day.weekday == 5 or day.weekday == 6:
            return False
        return True

# subclass will inherient everythng from parant class


class Developer(Employee):

    aise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # Employee.__init__(self, first,last,pay) #work as as above
        self.prog_lang = prog_lang


class manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.full_name())


def __repr__(self):
    return f'{self.first} {self.last} {self.pay}'
#
# my_date = dt.date(2021, 8, 8)
# print(Employee.is_work_day(my_date))


emp_1 = Developer('Suman', 'Shrestha', 500000, 'Python')
print(emp_1.email)
# print(emp_1.fullname())
emp_1.fullname = 'sky Blue'
print(emp_1.email)
emp_2 = Developer('Sky', 'Blue', 200000, 'SQL')

mgr_1 = manager('sam', 'Shrestha', 500000, [emp_1])

print(emp_1.__repr__())
print(repr(emp_1))

# print(mgr_1.email)
# mgr_1.add_emp(emp_2)
# mgr_1.remove_emp(emp_1)
# print(mgr_1.print_emp())
#
# print(isinstance(Developer, manager))
# print(issubclass(manager, manager))
# print(emp_1.prog_lang)
# print(emp_2.email)
# help(Developer)
# emp_str1 = 'sam-stha-700000'
# new_emp_1 = Employee.from_string(emp_str1)
# print(Employee.number_of_emps)
# emp_1.raise_amount = 1.08
# print(Employee.raise_amount)
# print(new_emp_1.raise_amount)
# # emp_1.apply_raise()
# print(emp_2.raise_amount)
# print(emp_1.__dict__)
# print(Employee.__dict__)
# print(emp_1.email)
# print(emp_2.email)
# # when we run methods from the instance we do not have to pass the argument it take automatically.
# print(emp_1.full_name())
# # when we run it from the class we have to pass instance as an argument
# print(Employee.full_name(emp_1))
