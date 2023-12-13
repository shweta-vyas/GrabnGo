import tkinter as tk
from tkinter import ttk
from tkinter import*
from PIL import Image, ImageTk
import random
from datetime import date
from datetime import datetime

root  = Tk()

prices = {
    "Coffee": 7,
    "Croissant": 6,
    "Donut": 5,
    "Matcha": 7.5,
    "Pancake": 7.5,
    "Juice": 5.5,
}


root.title("GRAB N GO")
combo_deal_applied = False
# ------------------------------------FUNCTIONS--------------------------------------------- #

#region Generating a random Order ID when starting a new order
def ORDER_ID():
    global combo_deal_applied
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    order_id = "GG_"
    random_letters = ""
    random_digits = ""
    for i in range(0,3):
        random_letters += random.choice(letters)
        random_digits += str(random.choice(numbers))

    order_id += random_letters + random_digits
    return order_id
#endregion

# region Add to Order Button
def add():
    global combo_deal_applied
     # updating the transaction label
    current_order = orderTransaction.cget("text")
    added_dish = displayLabel.cget("text") + "...." + str(prices[displayLabel.cget("text")]) + "$ "
    updated_order = current_order + added_dish
    orderTransaction.configure(text=updated_order)

    # updating the order total label
    order_total = orderTotalLabel.cget("text").replace("TOTAL : ", "")
    order_total = order_total.replace("$", "")
    updated_total = float(order_total) + prices[displayLabel.cget("text")]
     
    
    # Applying discounts/offers
    if "Coffee" in displayLabel.cget("text") and "Croissant" in current_order:
        updated_total -= 2  # Combo deal discount
        combo_deal_applied = True
    
    elif "Croissant" in displayLabel.cget("text") and "Coffee" in current_order:
        updated_total -= 2  # Combo deal discount
        combo_deal_applied = True
    
    elif "Croissant" in current_order and "Coffee" in current_order:
        orderTotalLabel.configure(text="TOTAL : " +  str(round(updated_total, 2)) + "$")

    else: orderTotalLabel.configure(text="TOTAL : " +  str(round(updated_total, 2)) + "$")
# endregion

#region Remove Button Function
def remove():
    dish_to_remove = displayLabel.cget("text") + "...." + str(prices[displayLabel.cget("text")])
    transaction_list = orderTransaction.cget("text").split("$ ")
    transaction_list.pop(len(transaction_list) - 1)

    # Update discount/applied flags when removing items

    if dish_to_remove in transaction_list:
        # update transaction label
        transaction_list.remove(dish_to_remove)
        updated_order = ""
        for item in transaction_list:
            updated_order += item + "$ "

        orderTransaction.configure(text = updated_order)

        # update transaction total
        order_total = orderTotalLabel.cget("text").replace("TOTAL : ", "")
        order_total = order_total.replace("$", "")
        updated_total = float(order_total) - prices[displayLabel.cget("text")]
        orderTotalLabel.configure(text="TOTAL : " + str(updated_total) + "$")

#endregion

# region Display Button Functions

def displayCoffee():
    coffeeDishFrame.configure(
        relief="sunken",
        style="SelectedDish.TFrame"
    )
    crossointDishFrame.configure(style="DishFrame.TFrame")
    donutDishFrame.configure(style="DishFrame.TFrame")
    matchaDishFrame.configure(style="DishFrame.TFrame")
    pancakeDishFrame.configure(style="DishFrame.TFrame")
    juiceDishFrame.configure(style="DishFrame.TFrame")

    displayLabel.configure(
        image=coffeeImage,
        text="Coffee",
        font=('Helvetica', 14, "bold"),
        foreground="white",
        compound="bottom",
        padding=(5, 5, 5, 5),
    )


def displayCrossoint():
    crossointDishFrame.configure(
        relief="sunken",
        style="SelectedDish.TFrame"
    )
    coffeeDishFrame.configure(style="DishFrame.TFrame")
    donutDishFrame.configure(style="DishFrame.TFrame")
    matchaDishFrame.configure(style="DishFrame.TFrame")
    pancakeDishFrame.configure(style="DishFrame.TFrame")
    juiceDishFrame.configure(style="DishFrame.TFrame")
    displayLabel.configure(
        image=crossointsImage,
        text="Croissant",
        font=('Helvetica', 14, "bold"),
        foreground="white",
        compound="bottom",
        padding=(5, 5, 5, 5),
    )


def displayDonut():
    donutDishFrame.configure(
        relief="sunken",
        style="SelectedDish.TFrame"
    )
    coffeeDishFrame.configure(style="DishFrame.TFrame")
    crossointDishFrame.configure(style="DishFrame.TFrame")
    matchaDishFrame.configure(style="DishFrame.TFrame")
    pancakeDishFrame.configure(style="DishFrame.TFrame")
    juiceDishFrame.configure(style="DishFrame.TFrame")
    displayLabel.configure(
        image=donutsImage,
        text="Donut",
        font=('Helvetica', 14, "bold"),
        foreground="white",
        compound="bottom",
        padding=(5, 5, 5, 5),
    )


def displayMatcha():
    matchaDishFrame.configure(
        relief="sunken",
        style="SelectedDish.TFrame"
    )
    coffeeDishFrame.configure(style="DishFrame.TFrame")
    crossointDishFrame.configure(style="DishFrame.TFrame")
    donutDishFrame.configure(style="DishFrame.TFrame")
    pancakeDishFrame.configure(style="DishFrame.TFrame")
    juiceDishFrame.configure(style="DishFrame.TFrame")
    displayLabel.configure(
        image=matchaImage,
        text="Matcha",
        font=('Helvetica', 14, "bold"),
        foreground="white",
        compound="bottom",
        padding=(5, 5, 5, 5),
    )


def displayPancake():
    pancakeDishFrame.configure(
        relief="sunken",
        style="SelectedDish.TFrame"
    )
    coffeeDishFrame.configure(style="DishFrame.TFrame")
    crossointDishFrame.configure(style="DishFrame.TFrame")
    donutDishFrame.configure(style="DishFrame.TFrame")
    matchaDishFrame.configure(style="DishFrame.TFrame")
    juiceDishFrame.configure(style="DishFrame.TFrame")
    displayLabel.configure(
        image=pancakesImage,
        text="Pancake",
        font=('Helvetica', 14, "bold"),
        foreground="white",
        compound="bottom",
        padding=(5, 5, 5, 5),
    )


def displayJuice():
    juiceDishFrame.configure(
        relief="sunken",
        style="SelectedDish.TFrame"
    )
    coffeeDishFrame.configure(style="DishFrame.TFrame")
    crossointDishFrame.configure(style="DishFrame.TFrame")
    donutDishFrame.configure(style="DishFrame.TFrame")
    matchaDishFrame.configure(style="DishFrame.TFrame")
    pancakeDishFrame.configure(style="DishFrame.TFrame")
    displayLabel.configure(
        image=juiceImage,
        text="Juice",
        font=('Helvetica', 14, "bold"),
        foreground="white",
        compound="bottom",
        padding=(5, 5, 5, 5),
    )


# endregion

#region Generating Receipt from Order Button
def order():
    new_receipt = orderIDLabel.cget("text")
    new_receipt = new_receipt.replace("ORDER ID : ","")
    transaction_list = orderTransaction.cget("text").split("$ ")
    transaction_list.pop(len(transaction_list) - 1)

    order_day = date.today()
    order_time = datetime.now()

    for item in transaction_list:
        item += "$ "

    with open(new_receipt, 'w') as file:
        file.write("Grab n Go")
        file.write("\n")
        file.write("________________________________________________________")
        file.write("\n")
        file.write(order_day.strftime("%x"))
        file.write("\n")
        file.write(order_time.strftime("%X"))
        file.write("\n\n")
        for item in transaction_list:
            file.write(item + "\n")
        file.write("\n\n")
        file.write(orderTotalLabel.cget("text"))

    orderTotalLabel.configure(text = "TOTAL : 0$")
    orderIDLabel.configure(text = "ODER ID: " + ORDER_ID())
    orderTransaction.configure(text = "")

#endregion

# ---------------------------------- STYLING AND IMAGES ------------------------------------ #

#region Style configurations
s = ttk.Style()
s.configure('MainFrame.TFrame', background = "#2B2B28")
s.configure('MenuFrame.TFrame', background = "#4A4A48")
s.configure('DisplayFrame.TFrame', background = "#0F1110")
s.configure('OrderFrame.TFrame', background = "#B7C4CF")
s.configure('DishFrame.TFrame', background = "#4A4A48", relief = "raised")
s.configure('SelectedDish.TFrame', background = "#C4DFAA")
s.configure('MenuLabel.TLabel',
            background = "#0F1110",
            font = ("Arial", 13, "italic"),
            foreground = "white",
            padding = (5, 5, 5, 5),
            width = 21
            )
s.configure('orderTotalLabel.TLabel',
            background = "#0F1110",
            font = ("Arial", 10, "bold"),
            foreground = "white",
            padding = (2, 2, 2, 2),
            anchor = "w"
            )
s.configure('orderTransaction.TLabel',
            background = "#4A4A48",
            font = ('Helvetica', 12),
            foreground = "white",
            wraplength = 170,
            anchor = "nw",
            padding = (3, 3, 3, 3)
            )

# endregion

# region Images
# Top Banner images

TopBannerImageObject = Image.open("Images/restaurant top banner.png").resize((918, 238))
TopBannerImage = ImageTk.PhotoImage(TopBannerImageObject)

# Menu images
displayDefaultImageObject = Image.open("Images/display - Default.png").resize((350,360))
displayDefaultImage = ImageTk.PhotoImage(displayDefaultImageObject)

coffeeImageObject = Image.open("Images/menu/coffee.png").resize((350,334))
coffeeImage = ImageTk.PhotoImage(coffeeImageObject)

crossointsImageObject = Image.open("Images/menu/crossoints.png").resize((350,334))
crossointsImage = ImageTk.PhotoImage(crossointsImageObject)

donutsImageObject = Image.open("Images/menu/donuts.jpg").resize((350,334))
donutsImage = ImageTk.PhotoImage(donutsImageObject)

juiceImageObject = Image.open("Images/menu/juice.jpeg").resize((350,334))
juiceImage = ImageTk.PhotoImage(juiceImageObject)

matchaImageObject = Image.open("Images/menu/matcha.png").resize((350,334))
matchaImage = ImageTk.PhotoImage(matchaImageObject)

pancakesImageObject = Image.open("Images/menu/pancakes.jpg").resize((350,334))
pancakesImage = ImageTk.PhotoImage(pancakesImageObject)


#endregion

#----------------------------------- WIDGETS ----------------------------------------------- #

# region Frames

# Section Frames
mainFrame = ttk.Frame(root, width = 800, height = 580, style = 'MainFrame.TFrame')
mainFrame.grid(row = 0, column = 0, sticky = "NSEW")

topBannerFrame = ttk.Frame(mainFrame)
topBannerFrame.grid(row = 0, column = 0, sticky = "NSEW", columnspan = 3)

menuFrame = ttk.Frame(mainFrame, style = 'MenuFrame.TFrame')
menuFrame.grid(row = 1, column = 0, padx = 3, pady = 3, sticky = "NSEW")

displayFrame = ttk.Frame(mainFrame, style = "DisplayFrame.TFrame")
displayFrame.grid(row = 1, column = 1, padx = 3, pady = 3, sticky = "NSEW")

orderFrame = ttk.Frame(mainFrame, style = "OrderFrame.TFrame")
orderFrame.grid(row = 1, column = 2, padx = 3, pady = 3, sticky = "NSEW")

# Dish Frames
coffeeDishFrame = ttk.Frame(menuFrame, style = "DishFrame.TFrame")
coffeeDishFrame.grid(row = 1, column = 0, sticky = "NSEW")

crossointDishFrame = ttk.Frame(menuFrame,style ="DishFrame.TFrame")
crossointDishFrame.grid(row = 2, column = 0, sticky ="NSEW")

donutDishFrame = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
donutDishFrame.grid(row = 3, column = 0, sticky ="NSEW")

juiceDishFrame = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
juiceDishFrame.grid(row = 4, column = 0, sticky ="NSEW")

matchaDishFrame = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
matchaDishFrame.grid(row = 5, column = 0, sticky ="NSEW")

pancakeDishFrame = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
pancakeDishFrame.grid(row = 6, column = 0, sticky ="NSEW")

#endregion

# region Top Banner Section

RestaurantBannerLabel = ttk.Label(topBannerFrame, image = TopBannerImage, background = "#0F1110")
RestaurantBannerLabel.grid(row = 0, column = 1, sticky = "NSEW")

# endregion

#region Menu Section
MainMenuLabel = ttk.Label(menuFrame, text = "MENU", style = "MenuLabel.TLabel")
MainMenuLabel.grid(row = 0, column = 0, sticky = "WE")
MainMenuLabel.configure(
    anchor = "center",
    font = ("Helvetica", 14, "bold")
)

coffeeDishLabel = ttk.Label(coffeeDishFrame, text ="Coffee ..... 7$", style ="MenuLabel.TLabel")
coffeeDishLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

crossointDishLabel = ttk.Label(crossointDishFrame, text ="Crossoints ..... 6$", style ="MenuLabel.TLabel")
crossointDishLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

donutDishLabel = ttk.Label(donutDishFrame, text ="Donuts ..... 5$", style ="MenuLabel.TLabel")
donutDishLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

juiceDishLabel = ttk.Label(juiceDishFrame, text ="Juice ..... 5.5$", style ="MenuLabel.TLabel")
juiceDishLabel.grid(row = 0, column = 0, padx =10, pady = 10, sticky = "W")

matchaDishLabel = ttk.Label(matchaDishFrame, text ="Matcha ..... 5.5$", style ="MenuLabel.TLabel")
matchaDishLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

pancakeDishLabel = ttk.Label(pancakeDishFrame, text ="Pancake .... 7.5$", style ="MenuLabel.TLabel")
pancakeDishLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

#Buttons
coffeeDisplayButton = ttk.Button(coffeeDishFrame, text ="Display", command = displayCoffee)
coffeeDisplayButton.grid(row = 0, column = 1, padx = 10)

crossointDisplayButton = ttk.Button(crossointDishFrame, text ="Display", command = displayCrossoint)
crossointDisplayButton.grid(row = 0, column = 1, padx = 10)

donutDisplayButton = ttk.Button(donutDishFrame, text ="Display", command = displayDonut)
donutDisplayButton.grid(row = 0, column = 1, padx = 10)

juiceDisplayButton = ttk.Button(juiceDishFrame, text ="Display", command = displayJuice)
juiceDisplayButton.grid(row = 0, column = 1, padx = 10)

matchaDisplayButton = ttk.Button(matchaDishFrame, text ="Display", command = displayMatcha)
matchaDisplayButton.grid(row = 0, column = 1, padx = 10)

pancakeDisplayButton = ttk.Button(pancakeDishFrame, text ="Display", command = displayPancake)
pancakeDisplayButton.grid(row = 0, column = 1, padx = 10)

# endregion

#region Order Section
orderTitleLabel = ttk.Label(orderFrame, text = "ORDER")
orderTitleLabel.configure(
    foreground="white", background="black",
    font=("Helvetica", 14, "bold"), anchor = "center",
    padding = (5, 5, 5, 5),
)
orderTitleLabel.grid(row = 0, column = 0, sticky = "EW")

orderIDLabel = ttk.Label(orderFrame, text = "ORDER ID : " + ORDER_ID())
orderIDLabel.configure(
    background = "black",
    foreground = "white",
    font = ("Helvetica", 11, "italic"),
    anchor = "center",
)
orderIDLabel.grid(row = 1, column = 0, sticky = "EW", pady = 1)

orderTransaction = ttk.Label(orderFrame, style = 'orderTransaction.TLabel')
orderTransaction.grid(row = 2, column = 0, sticky = "NSEW")

orderTotalLabel = ttk.Label(orderFrame, text = "TOTAL : 0$", style = "orderTotalLabel.TLabel")
orderTotalLabel.grid(row = 3, column = 0, sticky = "EW")

orderButton = ttk.Button(orderFrame, text = "ORDER", command = order)
orderButton.grid(row = 4, column = 0, sticky = "EW")


# endregion

# region Display Section
displayLabel = ttk.Label(displayFrame, image = displayDefaultImage)
displayLabel.grid(row = 0, column = 0 , sticky = "NSEW", columnspan = 2)
displayLabel.configure(background = "#0F1110")

addOrderButton = ttk.Button(displayFrame, text = "ADD TO ORDER", command = add)
addOrderButton.grid(row = 1, column = 0, padx = 2, sticky = "NSEW")

removeOrderButton = ttk.Button(displayFrame, text = "REMOVE", command = remove)
removeOrderButton.grid(row = 1, column = 1, padx = 2, sticky = "NSEW")
#endregion



#----------------------------- GRID CONFIGURATIONS -------------------------------------------#
mainFrame.columnconfigure(2, weight = 1)
mainFrame.rowconfigure(1, weight = 1)
menuFrame.columnconfigure(0, weight = 1)
menuFrame.rowconfigure(1, weight = 1)
menuFrame.rowconfigure(2, weight = 1)
menuFrame.rowconfigure(3, weight = 1)
menuFrame.rowconfigure(4, weight = 1)
menuFrame.rowconfigure(5, weight = 1)
menuFrame.rowconfigure(6, weight = 1)
orderFrame.columnconfigure(0, weight = 1)
orderFrame.rowconfigure(2, weight = 1)



root.mainloop()
