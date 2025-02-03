#Take input for the student that he can attend the exam or not
medical_cause=input("Did you have a medical cause Yes or No: ")

#Take input of the attendance
attendance = int(input("Enter the attendance of the student: "))

#Checking the user input predicting output accordingly
if medical_cause == 'Yes': #Checking the condition 1
    print ("You are allowed")
else:
    if attendance>=75: #Checking the condition 2
        print ("Allowed")
    else:
        print("Not allowed")