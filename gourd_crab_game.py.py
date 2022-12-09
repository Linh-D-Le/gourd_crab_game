from tkinter import *
import tkinter.font as font
from PIL import Image, ImageTk
import random, sys, os



root = Tk()
root.title("Dice Game")
root.iconbitmap("dice.ico")

app_width = 930
app_height = 750
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = screen_width/2 - app_width/2
y = screen_height/2 - app_height/2

# Positions the window in the center of the page.
root.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

# Define background image
bg = PhotoImage(file="NewYear.png", master=root)
img_label= Label(root,image=bg)
#define the position of the image
img_label.place(x=0, y=0)

# Set the given balance when starting game
balance = 100

# Create Result Frame
result_frame = Frame(root).grid(row=5, column=0, columnspan=6)

# Create Labels
label1 = Label(root, text="Select Your Choice", font=('Times', 20), fg="red").grid(row=0, column=0, rowspan=2, columnspan=2, pady=20)

# Label for balance
label2 = Label(root, text=f"Your balance is ${balance}", font=('Times', 20), fg="red")
label2.place(x=500, y=30)

# Label for choice
label3 = Label(root, text="Your choice is: ", font=('Times', 15), fg="red")
label3.place(x=380, y=110)

# Label for amount
label4 = Label(root, text="How much would you like to bet?", font=('Times', 15), fg="red")
label4.grid(row=3, column=2, padx=30)

# Create dice labels
dice_label1 = Label(root, image="", bg="#ffde59")
dice_label1.place(x=375, y=350)

dice_label2 = Label(root, image="", bg="#ffde59")
dice_label2.place(x=525, y=350)

dice_label3 = Label(root, image="", bg="#ffde59")
dice_label3.place(x=675, y=350)

# Create message for valid/invalid betting amount
dice_label4 = Label(root, text="", font=('Times', 15), fg="red", bg="#ffde59")
dice_label4.place(x=400, y=300)

# Create Result Labels
result_label = Label(root, text="", font=('Times', 15), fg="red", bg="#ffde59")
result_label.place(x=495, y=480)

# Set images
# Deer
img_deer = Image.open(r"deer.jpg")
# Resize Image
new_img_deer = ImageTk.PhotoImage(img_deer.resize((120, 120), Image.ANTIALIAS))
label_deer = Label(root, image=new_img_deer)

# Gourd
img_gourd = Image.open(r"gourd.jpg")
# Resize Image
new_img_gourd = ImageTk.PhotoImage(img_gourd.resize((120, 120), Image.ANTIALIAS))
label_gourd = Label(root, image=new_img_gourd)

# Chicken
img_chicken = Image.open(r"chicken.jpg")
# Resize Image
new_img_chicken = ImageTk.PhotoImage(img_chicken.resize((120, 120), Image.ANTIALIAS))
label_chicken = Label(root, image=new_img_chicken)

# Fish
img_fish = Image.open(r"fish.png")
# Resize Image
new_img_fish = ImageTk.PhotoImage(img_fish.resize((120, 120), Image.ANTIALIAS))
label_fish = Label(root, image=new_img_fish)

# Crab
img_crab = Image.open(r"crab.jpg")
# Resize Image
new_img_crab = ImageTk.PhotoImage(img_crab.resize((120, 120), Image.ANTIALIAS))
label_crab = Label(root, image=new_img_crab)

# Shrimp
img_shrimp = Image.open(r"shrimp.jpg")
# Resize Image
new_img_shrimp = ImageTk.PhotoImage(img_shrimp.resize((120, 120), Image.ANTIALIAS))
label_shrimp = Label(root, image=new_img_shrimp)

# Dice
img_dice = Image.open(r"dice.jpg")
# Resize Image
new_img_dice = ImageTk.PhotoImage(img_dice.resize((50, 50), Image.ANTIALIAS))
label_dice = Label(root, image=new_img_dice)

# Create dice list
dice_list = [new_img_deer, new_img_gourd, new_img_chicken, new_img_fish, new_img_crab, new_img_shrimp]

get_choice = StringVar()
get_amount = StringVar()
get_result1 = StringVar()

e = Entry(root, textvariable=get_choice, width=10, bd=5, bg="red", font=('Times 20'), justify=CENTER)
e.place(x=620, y=100)

bet_entry = Entry(root, textvariable=get_amount, width=10, bd=5, bg="red", font=('Times 20'), justify=CENTER)
bet_entry.grid(row=3, column=3, sticky="w")


def button_click(choice):
    get_choice.get()
    e.delete(0, END)
    e.insert(0, str(choice))

# Get Dice Name 
def get_dice(n):
    if n == new_img_deer:
        return("Deer")
    elif n == new_img_gourd:
        return("Gourd")
    elif n == new_img_chicken:
        return("Chicken")
    elif n == new_img_fish:
        return("Fish")
    elif n == new_img_shrimp:
        return("Shrimp")
    else:
        return("Crab")

def roll():
    bet_amount = get_amount.get()
    global balance
    global b_amount, dice1, dice2, dice3
    try:
        if get_choice.get() not in ["Deer", "Gourd", "Chicken", "Fish", "Crab", "Shrimp"]:
            dice_label4.config(text="Please select your choice!")
        else:
            b_amount = int(bet_amount)
            bet_entry.delete(0, END)
            if b_amount > balance:
                dice_label4.config(text="Your betting amount is\nhigher than your balance. Please try again!")
            elif b_amount == 0:
                dice_label4.config(text="Please enter an amount!")
            else:
                dice_label4.config(text="")
                dice1 = random.choice(dice_list)
                dice2 = random.choice(dice_list)
                dice3 = random.choice(dice_list)
                # Update labels
                dice_label1.config(image=dice1)
                dice_label2.config(image=dice2)
                dice_label3.config(image=dice3)

                # Determine Dice Name
                result1 = get_dice(dice1)
                result2 = get_dice(dice2)
                result3 = get_dice(dice3)

                result_list = [result1, result2, result3]
                bingo=str(get_choice.get())
                count_bingo = result_list.count(bingo)
                
                if count_bingo == 0:
                    result_label.config(text=f"Sorry! You just lose ${b_amount}")
                    balance -= b_amount
                    label2.config(text=f"Your balance is ${balance}")
                    
                    if balance == 0:
                        label2.config(text=f"Your balance is ${balance}")
                        result_label.config(text="Sorry! Game over!")

                        # Create button "Play again"
                        button_again = Button(result_frame, text="Play again", font=('Times', 20), fg="black",
                                    width=10, bd=5, bg="green", command=lambda: [button_again.place_forget(), restart_program()])
                        button_again.place(x=500, y = 510)
                    
                else:
                    earn = count_bingo * b_amount
                    result_label.config(text=f"Congratulations! \nYou just earned ${earn}")
                    balance += earn
                    label2.config(text=f"Your balance is ${balance}")
            
    except ValueError:
        dice_label4.config(text="Please enter an amount")  


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

# Create buttons
# Button Deer
button_deer = Button(root, image=new_img_deer, text="Deer", compound=TOP, font=('Times', 20), fg="black",
              bd=5, bg="red", command=lambda: button_click("Deer"))
button_deer.grid(row=3, column=0, padx=10, pady=10)

# Button Gourd
button_gourd = Button(root, image=new_img_gourd, text="Gourd", compound=TOP, font=('Times', 20), fg="black",
                bd=5, bg="red", command=lambda: button_click("Gourd"))
button_gourd.grid(row=3, column=1, pady=10)

# Button Chicken
button_chicken = Button(root, image=new_img_chicken, text="Chicken", compound=TOP, font=('Times', 20), fg="black",
                bd=5, bg="red", command=lambda: button_click("Chicken"))
button_chicken.grid(row=4, column=0, padx=10, pady=10)

# Button Fish
button_fish = Button(root, image=new_img_fish, text="Fish", compound=TOP, font=('Times', 20), fg="black",
                bd=5, bg="red", command=lambda: button_click("Fish"))
button_fish.grid(row=4, column=1, pady=10)

# Button Crab
button_crab = Button(root, image=new_img_crab, text="Crab", compound=TOP, font=('Times', 20), fg="black",
                bd=5, bg="red", command=lambda: button_click("Crab"))
button_crab.grid(row=5, column=0, padx=10, pady=10)

# Button Shrimp
button_shrimp = Button(root, image=new_img_shrimp, text="Shrimp", compound=TOP, font=('Times', 20), fg="black",
                bd=5, bg="red", command=lambda: button_click("Shrimp"))
button_shrimp.grid(row=5, column=1, pady=10)

# Button Dice
button_roll = Button(root, image=new_img_dice, text="Roll", compound=LEFT, font=('Times', 20), fg="black",
              width=120, bd=5, bg="green", command=roll)
button_roll.place(x=520, y=230)

root.mainloop()