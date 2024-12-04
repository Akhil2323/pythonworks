def swap_decorator(fn):

    def wrapper(n1,n2):

        if n1<n2:

            (n1,n2)=(n2,n1)

        return fn(n1,n2)
    
    return wrapper

def round_dec(fn):

    def wrapper(num1,num2):

        num1=round(num1)

        num2=round(num2)

        return fn(num1,num2)
    
    return wrapper

@swap_decorator
@round_dec

def add_number(num1,num2):

    return num1+num2

@swap_decorator
@round_dec

def substraction(num1,num2):

    return num1-num2

@swap_decorator
@round_dec

def division(num1,num2):

    return num1/num2

print(division(2,10))

print(add_number(10.2,20))

print(substraction(8.5,20))