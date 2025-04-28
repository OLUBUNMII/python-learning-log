def getDataFromUser():
    D = {}
    while True:
        studentId = input("Enter student ID: ")
        marksList = input("Enter the marks by comma seperated values: ")
        if studentId in D:
            print(studentId, "is already inserted")
        else:
            D[studentId] = marksList.split(",")
        while True:
            moreStudents = input('Do you want to insert another record? (yes/no): ')
            if moreStudents.lower() == "no":
                return D
            elif moreStudents.lower() == "yes":
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

studentData = getDataFromUser ()

print(studentData)

