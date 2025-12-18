def element(n):
    if n % 3 == 0 and n%5 == 0:
        print("Buzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("FizzBuzz")
    else :
        print (n)

element(3)
element(5)
element(15)
element(7)

              