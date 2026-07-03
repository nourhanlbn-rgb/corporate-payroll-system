# Function to calculate employee bonus based on performance rating
def calculate_bonus(base_salary, performance_rating):
    if performance_rating == 5 :
        bonus_percentage = 0.20
        
    elif performance_rating >= 3 :
        bonus_percentage = 0.10
        
    else : 
        bonus_percentage = 0.0
        
    return base_salary * bonus_percentage 
        
# Function to calculate tax deductions from gross salary    
def calculate_tax(gross_salary):
    if gross_salary > 7000 :
        tax_percentage = 0.15 
                
    elif gross_salary >= 3000 :
        tax_percentage = 0.10
                  
    else :
        tax_percentage = 0.0 
     
    return gross_salary * tax_percentage   
             
# Main application controller
def main_hr_app():
    print ("----- 🏢Corporate Payroll System 🏢 -----".center(90),"\n")    
    employee_name = input ("Please Enter Employee Name: ").strip().title()
    employee_department = input ("Please Enter Employee Department: ").strip().upper()
    base_salary = float(input ("Please Enter Employee Salary (EGP): ").strip())
    performance_rating = int(input ("Please Enter Employee Performance Rating: ").strip())
    if base_salary < 0 or performance_rating > 5 or performance_rating < 1 :
        print ("❌ Invalid data entered.\nPlease restart and check your inputs.")
        return
    
    bonus = calculate_bonus(base_salary, performance_rating)
    gross_salary = base_salary + bonus
    tax = calculate_tax(gross_salary)
    net_salary = gross_salary - tax 
    
    print ("=" * 50)
    print (f"📄 Payroll Statement for: {employee_name}")
    print ("=" * 50)
    print (f"- Department:     {employee_department}")
    print (f"- Base Salary:    {base_salary:.2f} EGP")
    print (f"- Earned Bonus:   {bonus:.2f} EGP")
    print (f"- Tax Deductions: {tax:.2f} EGP")
    print ("=" * 50)
    print (f"💵Net Payable Cash: {net_salary:.2f} EGP")
    print ("=" * 50)
     
    
    
main_hr_app()  
    
    
    
    
    