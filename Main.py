import calendar  

def print_months(year):  
    for mm in range(1, 13):  
        month_name = calendar.month_name[mm]  
        print(month_name)

yy = 2025
print_months(yy)