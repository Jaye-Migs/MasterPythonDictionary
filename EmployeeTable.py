#Python List
Employee1 = {
  "ID" : 1,
  "Name" : "John Doe",
  "Department" : "Sales",
  "Age" : 30,
  "Email" : "john.doe@company.com"
}
Employee2 = {
  "ID" : 2,
  "Name" : "Jane Smith",
  "Department" : "Human Resources",
  "Age" : 25,
  "Email" : "jane.smith@company.com"
}
Employee3 = {
  "ID" : 3,
  "Name" : "Mark Johnson",
  "Department" : "IT",
  "Age" : 40,
  "Email" : "mark.johnson@company.com"
}
Employee4 = {
  "ID" : 4,
  "Name" : "Lisa Wong",
  "Department" : "Markering",
  "Age" : 28,
  "Email" : "lisa.wong@company.com"
}
Employee5 = {
  "ID" : 5,
  "Name" : "Paul McDonald",
  "Department" : "Finance",
  "Age" : 35,
  "Email" : "paul.mcdonald@company.com"
}
Employees = [Employee1, Employee2, Employee3, Employee4, Employee5]
for Employee in Employees:
    print(f"ID: {Employee.get('ID')}, Name: {Employee.get('Name')}, Department: {Employee.get('Department')}, Age: {Employee.get('Age')}, Email: {Employee.get('Email')}")