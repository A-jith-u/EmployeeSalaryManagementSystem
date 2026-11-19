#***********************************************
#**************EMPLOYEE SALARY MANAGEMENT********
#************************************************

from ContractEmployee import ContractEmployee     #Importing the ContractEmployee class
from PermanentEmployee import PermanentEmployee     #Importing the PermanentEmployee class


print("**********EMPLOYEE SALARY MANAGEMENT SYSTEM**********")

permanent_employee=PermanentEmployee('Ajay',101,'Software Engineer','ajaywork@gmail.com','6238572794',50000,2000)      #Creating an object of the PermanentEmployee class and passing the required arguments to the constructor
contract_employee=ContractEmployee('Vijay',110,'Software Designer','vijaywork@gmail.com','9747626238',40000,1000)      #Creating an object of the ContractEmployee class and passing the required arguments to the constructor


permanent_employee.display_details()                  #Displaying the details of the permanent employee by calling the display_details method of the PermanentEmployee class
permanent_employee.calculate_salary()                 #Calculating the salary of the permanent employee by calling the calculate_salary method of the PermanentEmployee class

print("______________________________________________")
contract_employee.display_details()                   #Displaying the details of the contract employee by calling the display_details method of the ContractEmployee class
contract_employee.calculate_salary()                  #Calculating the salary of the contract employee by calling the calculate_salary method of the ContractEmployee class


print("\n")
