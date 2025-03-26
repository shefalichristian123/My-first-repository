try:
    dividend = int(input("Enter the dividend: "))
    divisor = int(input("Enter the divisor: "))
    result = dividend/divisor
    print("The result is:",result)
except ValueError:
    print("Please enter valid integers for dividend and divisor.")
except ZeroDivisionError:
    print("Divisor can not be zero.")
except Exception as e:
    print("An error occured:",e)