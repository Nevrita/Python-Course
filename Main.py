def shutdown():  
    user_input = input("Do you want to shut down? (Yes/No): ")  

    if user_input == "Yes":  
        print("Shutting down...")  
    elif user_input == "No":  
        print("Hold on, we're not shutting down just yet!")  
    else:  
        print("Sorry.") 

shutdown()