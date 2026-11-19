
from abc import ABC,abstractmethod                          #Importing ABC and abstractmethod from abc module to create abstract class and abstract method

class Employee(ABC):                                        #Inheriting ABC class to create abstract class Employee
    def __init__(self,name,emp_id,job_role,email_id,phn_no,basic_salary):            #Initializing the attributes of the Employee class
        self.name=name
        self.emp_id=emp_id
        self.job_role=job_role
        self.email_id=email_id
        self.phn_no=phn_no
        self.__basic_salary=basic_salary

    @abstractmethod                                       #Creating an abstract method calculate_salary which will be implemented in the subclasses
    def calculate_salary(self):
        pass

    def display_details(self):                             #A method to display the details of the employee
        print(f" The name of the employee is:{self.name}\n The employee id:{self.emp_id}\n The job role of the employee is:{self.job_role}\n The email id:{self.email_id}\n The phone number:{self.phn_no}\n The basic salary:{self.__basic_salary}")

    @property                                               #Creating a property decorator to access the private attribute __basic_salary
    def basic_salary(self):
        return self.__basic_salary

    @basic_salary.setter                                     #Creating a setter method to set the value of the private attribute __basic_salary
    def basic_salary(self,value):
        self.__basic_salary=value






           
          