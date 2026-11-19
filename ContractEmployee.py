from employee import Employee

class ContractEmployee(Employee):                             #Creating a subclass ContractEmployee which inherits the Employee class
    def __init__(self,name,emp_id,job_role,email_id,phn_no,basic_salary,allowance):
        super().__init__(name,emp_id,job_role,email_id,phn_no,basic_salary)
        self.allowance=allowance

    def calculate_salary(self):                              #Calculating the salary of the contract employee by adding 5% of allowance to the basic salary
        self.basic_salary=self.basic_salary+(5/100)*self.allowance
        print(f" Salary of contract employee is:{self.basic_salary}")

