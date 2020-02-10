
def main():
    #Input
    results = 0

    # Ask user for 1st number & store input
    num1 = int(input('what is your first number?'))

    #Ask user for 2nd number & store input
    num2 = int(input('what is your second number'))

    #Process
    # Add num1 and num2 & store sum
    mathSum = num1 + num2

    # Mutiply num1 and num2 & store result
    results = num1 * num2

    #Output
    #Display num1, num2, sum and result
    print('users first number: ', num1)
    print('users second number: ', num2)
    print('sum of numbers: ', mathSum)
    print('Result of numbers: ', results)

main()
