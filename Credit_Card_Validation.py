# -------------------- Validate Credit Card base on Lhun's Algorithm --------------------------- #

# -- Import library -- #
from tkinter import *

def validate_card():
    # -- Create card number -- #
    # card_no = "5610591081018250"

    # card_number = input("Enter your credit card number: ")
    # print(type(card_number))

    card_number = entry_card.get()

    odd_sum = 0
    double_list = []
    even_sum = 0

    number = list(card_number) # -- convert string to list
    # print(number)

    for idx,val in enumerate(number): # -- enumerate to show the index and value of this index ( index, value )
        # print(str(idx)+'=>'+val)
        if idx % 2 != 0: # this is odd number ( chia 2 khong ra so du )
            odd_sum += int(val)
        else:            # this is even number
            # print(idx, val)
            double_list.append(int(val)*2)

    # print(odd_sum)
    # print(double_list)

    # -- converting the list into a string
    double_string = ""
    for x in double_list:
        double_string += str(x)
    # print(double_string)

    # -- converting the string back to a list
    double_list = list(double_string)
    # print(double_list)

    # -- Calculate even index number after multi with 2 -- #
    for n in double_list:
        even_sum += int(n)
    # print(even_sum)

    net_sum = odd_sum + even_sum
    if net_sum % 10 == 0:
        print('Valid card!')
        label_result.config(text='Valid Card!')
    else:
        print('Invalid card!')
        label_result.config(text='Invalid Card!')

# -- Create a new window -- #
root = Tk()
root.geometry("300x300")

label_card = Label(root, text="Enter your credit card number")
label_card.pack()
entry_card = Entry(root)
entry_card.pack()

# -- Create a button for validating -- #
button = Button(root, text="Validate", command=validate_card)
button.pack()

label_result = Label(root)
label_result.pack()

# -- Create a loop to show the window -- #
root.mainloop()