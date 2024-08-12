employee_file = open('employees.txt', 'r') #r = read, w = write(change the file), a = append(add new information but not change), r+ = resading and writing
print(employee_file.readable())
print(employee_file.readline())
print(employee_file.readline())
print(employee_file.readlines()[1])
for employee in employee_file.readlines():
    print(employee)
employee_file.close()