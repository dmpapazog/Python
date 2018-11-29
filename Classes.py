import datetime


def main():
    
   class Employee:
       raise_amount = 1.04

       def __init__(self, first, last, pay):
           self.first = first
           self.last = last
           self.email = first + '.' + last + "@gmail.com"
           self.pay = pay

       def fullname(self):
           return "{} {}".format(self.first, self.last)

       def apply_raise(self):
           self.pay = int(self.pay * self.raise_amount)

       @classmethod
       def from_string(cls, input_string):
           first, last, pay = input_string.split('-')
           return cls(first, last, pay)

       @staticmethod
       def is_weekday(day):
           if day.weekday() == 5 or day.weekday() == 6:
               return False
           return True


   dev1 = Employee("Correy", "Schafer", 50000)
   dev2 = Employee("Test", "Employee", 60000)
   dev3 = Employee.from_string("John-Doe-70000")

   print(dev1.email)
   print(dev2.email)
   print(dev3.email)

   my_date = datetime.date(2017, 7, 10)
   print(Employee.is_weekday(my_date))

   return 1


if __name__ == "__main__":
    main()