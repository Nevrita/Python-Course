# Create Class
class Employee:

    # Initializing 
    def __init__(self):
        print('Emplyee created')

    # Calling destructor
    def __del__(self):
            print("Destructor called")

def  Create_obg():
            print('Making Object...')
            obj = Employee()
            print('function end...')
            return obj
        
print('Calling Create_obj() function...')
obj = Create_obg()
print('Program End...')