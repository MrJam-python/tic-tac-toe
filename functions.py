def add_numbers(number1,number2):
    print (number2 + number1)
    # the datatype of this sum is an integer

add_numbers(3,7)



def mult_numbers(num1, num2):
    product = num1 * num2
    return product

print (mult_numbers(6,1))

number = mult_numbers(6,1) 

var_test = 0
var_test += mult_numbers(var_test, var_test)
print (mult_numbers(var_test, var_test))
