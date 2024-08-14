employee_file = open('employees.txt', 'a')
employee_file.write('\nToby - Human Resources')
employee_file.close()

employee_file = open('employees1.txt', 'w')
employee_file.write('\nKelly - Customer Service')
employee_file.close() 

employee_file = open('index.html', 'w')
employee_file.write('<p>This is HTML<\p>')
employee_file.close()