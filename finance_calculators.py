import math
# This program that allows the user to access two diffrent financial calculators : 
# !. An investiment calculator
# 2. A home loan repayment calculator

# This explains what a investment and what a bond is :
print("""investment - to calculate the amount of interest you'll earn on your investment.""")
print("""bond       - to calculate the amount you'll have to pay on a home loan.""" )

# User going to choose their finance calculator
user_calculater =input("\n Enter 'investment' or 'bond' from the menu above to proceed:")

# I am going to use if-elif-else :
if user_calculater.upper() == "INVESTMENT":
    #Asking amount of money invested
    deposit_money = int(input("Enter the amount of money that will be deposit :"))
    #Asking the interest rate
    interest_rate = int(input("""Enter the interst rate. Don't worry about "%", just input the number:"""))
    r = int(interest_rate)/100
    #Asking the amount of years investment
    number_years = int(input("The number of the years they plan on investing :"))
    interest = input(("Is it a compound or simple ?"))
    total_amount = 0
    
    #This is a if statement in a if statement:
    if interest.lower() == "simple":
        total_amount = deposit_money *(1 + r*number_years)
        
    else:
        total_amount = deposit_money * math.pow((1+r),number_years)
    print (f"R {total_amount}")
    
elif user_calculater.lower() == "bond":
    # Bond calculation:
    value_of_house = int(input("Enter value of the house:"))
    monthly_interest_rate = int(input("Enter monthly interest rate?"))
    number_months = int(input("Enter the numbers of months the bond must be repaid :"))
    
    total = (monthly_interest_rate * value_of_house)/(1 + (1 + monthly_interest_rate)**(-number_months))

    print (f"R {total}")

# If the wrong value is entered
else :
    print ("You entered nothing or the wrong value")


# I am struggeling with a error on line 62, I do not understand why it is a syntax error




