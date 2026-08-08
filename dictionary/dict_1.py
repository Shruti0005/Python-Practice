# Create an empty dictionary and print it.
employee = {}
print(employee)

# Add some keys and values and print dictionary
employee = dict({
    'id' : 1,
    'name' : 'Nova',
})
print(employee)

# Add new key-value and print dictionary
employee['salary'] = 20000
print(employee)

# Update the salary to 30000, then add: department : HR
employee.update({
    'salary' : 30000,
    'department' : 'HR'
})
print(employee)

# combine two dictionary 
emp_status = {
    'status' : 'single',
    'gender' : 'female'
}

employee.update(emp_status)
print(employee)

