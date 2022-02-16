# opening file to read
import os

path_name = "students.txt"

if os.path.isfile(path_name):
    print("File exists")
    c = 0
    # declaring lists
    result = [ ]
    with open(path_name, 'r') as f:
        for line in f:
            if not line.strip():
                continue
            if line:
                # excluding header
                if c == 0:
                    c += 1
                else:
                    line = line.rstrip('\n')
                    fields = line.split('\t')
                    result.append([fields[0],fields[1],fields[2],fields[3],fields[4],fields[5]])
            
    f.close()
    if (len(result)==0):
        raise Exception("File did not contain any valid data")
        

else:
    raise Exception("File does not exist! IOError has occured")
 
def printMenu():
    print('\n1.Display all student records\n'
          '2.Display students whose last name begins with a certain string (case insensitive)\n'
          '3.Display all records for students whose graduating year is a certain year\n'
          '4.Display a summary report of number and percent of students in each program, for students graduating on/after a certain year\n'
          '5.Exit')
    
def print_students():
    print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format('ID','Last Name', 'First Name', 'Degree Year', 'Degree Term', 'Degree Program'))
    
    for data in result:
        if (len(data)!=0):
            ID, LastName, FirstName, DegreeYear, DegreeTerm, DegreeProgram = data
            print ("{:<15} {:<15} {:<15}{:<15} {:<15} {:<15}".format( ID, LastName, FirstName, DegreeYear, DegreeTerm, DegreeProgram))
        else:
            raise Exception("Bad or missing row in file")
        
        
def last_name():
    last=input('Enter the last name: ')
    foundRecord = False
    for data in result:
        if data[1].startswith(last.capitalize()):
             print("{:<15} {:<15} {:<15}{:<15} {:<15} {:<15}".format(data[0],data[1],data[2],data[3],data[4],data[5]))
             foundRecord = True
    
    if foundRecord == False:
        print("Could not find a record for the given Last Name:" + last)
    

def grading_year():
    year=input('Enter the graduating year: ')
    foundRecord = False 
    for data in result:
        if data[3]==year:
           print("{:<15} {:<15} {:<15}{:<15} {:<15} {:<15}".format(data[0],data[1],data[2],data[3],data[4],data[5]))
           foundRecord = True 
           
    if foundRecord == False:
        print("There are no valid record for the request")
            
            
def summary():
    year=input('Enter the graduating year: ')
    
    if int(year) > 9999 or int(year) < 999:
        raise Exception("Invalid year entered")
    
    my_data={}
    for data in result:
        if data[3]==year:
            if data[5] not in my_data.keys():
                my_data[data[5]]=[data[0]]
            else:
                my_data[data[5]].append(data[0])
    if len(my_data)==0:
        print("Data unavailable for given input")
    
#     print('\nNumber of people in each course')
    for key,value in my_data.items():
        count=0
        for val in value:
            count=count+1
        print(key,':',count)

while True:
    printMenu()
    choice=input('Please enter your choice: ')
    

    if choice=='1':
        print_students()
        
    elif choice=='2':
        last_name()
        
    elif choice=='3':
        grading_year()
    
    elif choice=='4':
        summary()
    
    elif choice=='5':
        print("Bye")
        break
    else:
        raise Exception("Invalid choice selected")

