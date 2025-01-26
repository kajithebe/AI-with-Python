'''
In the second exercise the idea is to create a small grocery shopping list with the list datastructure. In short, create a program that allows the user to (1) add products to the list, (2) remove items and (3) print the list and quit. If the user adds something to the list, the program asks "What will be added?: " and saves it as the last item in the list. If the user decides to remove something, the program informs the user about how many items there are on the list (There are [number] items in the list.") and prompts the user for the removed item ("Which item is deleted?: "). If the user selects 0, the first item is removed. When the user quits, the final list is printed for the user "The following items remain in the list:" followed by the remaining items one per line. If the user selects anything outside the options, including when deleting items, the program responds "Incorrect selection.". When the program works correctly it prints out the following:
'''

shopping_list = []
while True:
    task = input("""Would you like to
    (1) Add or
    (2) Remove items or
    (3) Quit? """)

    if task == "1":
        add_item_name = input("What will be added? ")
        shopping_list.append(add_item_name) #adding item to the list
    elif task == "2":
        print(f"There are {len(shopping_list)} items in the list.")
        remove_item_index = int(input("What will be removed? "))
        if remove_item_index < len(shopping_list): #to filter out the input not within the range of list
            del shopping_list[remove_item_index]
        else:
            print("Incorrect selection.")
    elif task == "3":
        print(f"The following items remain in the list:")
        for item in shopping_list:
            print(item)
        break