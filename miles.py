#The company you work for pays expenses for employees who use their car to travel as part of their job.
#Mileage expenses for a trip are calculated as follows:
# No expenses for the first 2 miles;
# 50p per mile paid for miles 2 − 30;
# 32p per mile paid for miles 30 − 300;
# No extra expenses for miles beyond 300.

#An extra one-off overnight accommodation payment of £60 is paid for trips of 180 miles or more.
#Write a Python function named expenseCalc which takes one integer argument, the number of miles,
#and returns the expense amount in pounds according to the rules above. The return type should be a
#float rounded to 2 decimal places.
#The function should raise appropriate errors if the input is not integer or if it is negative.



def expenseCalc(m):
    """This function will calculate mileage expenses for a trip, through the user's input
            of the number of miles, and output the expence amount in pounds"""
    
    if type(m) is not int:
        raise TypeError("The input you have entered is not an integer")
    elif m < 0:
        raise ValueError("The number of miles entered is a negative number")
    if m <=2:
        return(0)
    elif m <= 30:
        firstMilesOff = m-2
        milesToPay = firstMilesOff *0.50
        return(round(milesToPay,2))
        
    elif m <=300:
        first2MilesOff = m-2
        paying50pPerMile = 30 * 0.50
        milesLeftToPay = first2MilesOff - 30             
        remaining32pPerMile = milesLeftToPay * 0.32
        expenseAmount = paying50pPerMile + remaining32pPerMile
        if m >=180:
            overnightAccommodationPayment = 60
            expenseAmount = expenseAmount + overnightAccommodationPayment
        return(round(expenseAmount,2))
        
    else:
        first2MilesOff = m-2
        paying50pPerMile = 30 * 0.50
        milesLeftToPay = first2MilesOff - 30   
        paying32pPerMile = 300*0.32
        furtherExpenseAmount = paying32pPerMile + paying50pPerMile
        overnightAccommodationPayment = 60
        return(round(furtherExpenseAmount + overnightAccommodationPayment,2))
    
        

