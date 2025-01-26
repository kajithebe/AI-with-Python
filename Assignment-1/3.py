'''Make simple Supermarket -program,
• having 10 products with prices in a list as follows:[10,14,22,33,44,13,22,55,66,77].
• asking product number from 1 to 10 and summing its price to totalsum and printing product number and price for every product as in example.
• asking products until user gives '0' to quit the program (while-loop).
• printing "Total:" and the total sum of prices.
• asking "Payment:" from user and printing "Change:" and finally calculating and printing the amount of change (payment - totalsum) to customer.
• You must use in this program: while, input'''

print("Supermarket \n===================")
prices = [10, 14, 22, 33, 44, 13, 22, 55, 66, 77]

total_sum = 0
try:
    while True:
        selected_product = int(input("Please select product (1-10) or 0 to quit: "))
        if 10 >= selected_product > 0: #Filtering out the inputs other than product selection
            total_sum += prices[selected_product-1]
            print(f"Product {selected_product} Price: {prices[selected_product-1]}")
        elif selected_product == 0: #In case of quit
            print(f"Total: {total_sum}")
            while True: #To keep asking to provide make payment not less than total amount
                payment = int(input("Payment: "))
                if payment < total_sum:
                    print(f"Insufficient payment. Please enter an amount not less than {total_sum}.")
                else:
                    print(f"Payment: {payment} \nChange: {payment - total_sum}")
                    break #Exiting after successful payment
            break #Exit the whole program
        else:
            print("Invalid product selection. Please select a number between 1 and 10.")
except ValueError:
    print("Please enter an integer.")