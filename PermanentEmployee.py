from employee import Employee

class PermanentEmployee(Employee):                           #Creating a subclass PermanentEmployee which inherits the Employee class
    def __init__(self,name,emp_id,job_role,email_id,phn_no,basic_salary,allowance):
        super().__init__(name,emp_id,job_role,email_id,phn_no,basic_salary)
        self.allowance=allowance
 
    def calculate_salary(self):                              #Calculating the salary of the permanent employee by adding 20% of allowance to the basic salary
        self.basic_salary=self.basic_salary+(20/100)*self.allowance           
        print(f" Salary of permanent employee is:{self.basic_salary}")