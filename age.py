try:
    age = int(input("Please enter your age"))
    10/age
    print(age)

except ZeroDivisionError as err:
    print(f"Please do not provide 0 as age {err}")
except ValueError as err1:
    print(f"Please enter a number {erradsdds1}")
finally:
    print('Ok I am done')