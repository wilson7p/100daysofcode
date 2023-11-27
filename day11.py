#Error handling (try, except)
print("\nWilson - Day 11 of 100DaysOfCode")
print("\n Error handling (try, except)")

try:
    x = int(input("Enter a number: "))
    result = 10 / x
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Please enter a valid number.")

except Exception as e:
    print("An unexpected error occurred:", e)

else:
    print("No exceptions were raised.")

finally:
    print("This block always executes.")

