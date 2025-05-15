import tkinter as gui
from tkinter import messagebox
import json
from tkinter import ttk
import os

with open("malice.txt") as file:
    orbcontent = file.readlines()
    orbmalice = orbcontent[0]


root = gui.Tk()
root.title("Inconvenience Store")
root.geometry("900x650")
root.configure(bg='#CAFAD5')

def refresh_product_list():
    global image_refs
    image_refs.clear()

    for widget in root.grid_slaves():
        if int(widget.grid_info()["row"]) >= 2:
            widget.destroy()

    items = loaditems("stock.txt")
    row, col = 2, 0        

    for name, price, stocknumber, description, important, imagepath in items:
        try:
            img = gui.PhotoImage(file=imagepath)
            image_refs.append(img)
        except Exception as e:
            print(f"Error loading image '{imagepath}': {e}")
            continue

        btn = gui.Button(root, image=img, command=lambda n=name, p=price, s=stocknumber, d=description, im=important, ip=imagepath: show_item_details(n, p, s, d, im, ip))
        btn.grid(row=row, column=col, pady=25)
        lbl = gui.Label(root, text=name, bg="#CAFAD5")
        lbl.grid(row=row+1, column=col)

        col += 1
        if col >= 3:
            col = 0
            row += 2

def additem():
    addwindow = gui.Toplevel(root)
    addwindow.configure(bg='#CAFAD5')
    addwindow.title("Add Item")
    
    gui.Label(addwindow, text="Item Name:", bg='#CAFAD5').grid(row=0, column=0, sticky='w', padx=5, pady=5)
    entry_name = gui.Entry(addwindow, width=40)
    entry_name.grid(row=0, column=1, padx=10)

    gui.Label(addwindow, text="Price (CAD):", bg='#CAFAD5').grid(row=1, column=0, sticky='w', padx=5, pady=5)
    entry_price = gui.Entry(addwindow, width=40)
    entry_price.grid(row=1, column=1, padx=10, pady=10)

    gui.Label(addwindow, text="Amount in Stock:", bg='#CAFAD5').grid(row=2, column=0, sticky='w', padx=5, pady=5)
    entry_stocknumber = gui.Entry(addwindow, width=40)
    entry_stocknumber.grid(row=2, column=1, padx=10, pady=10)

    gui.Label(addwindow, text="Item Description:", bg='#CAFAD5').grid(row=3, column=0, sticky='w', padx=5, pady=5)
    entry_description = gui.Entry(addwindow, width=40)
    entry_description.grid(row=3, column=1, padx=10, pady=10)

    gui.Label(addwindow, text="Important Notices (eg. item sales):", bg='#CAFAD5').grid(row=4, column=0, sticky='w', padx=5, pady=5)
    entry_important = gui.Entry(addwindow, width=40)
    entry_important.grid(row=4, column=1, padx=10, pady=10)

    gui.Label(addwindow, text="Image Path:", bg='#CAFAD5').grid(row=5, column=0, sticky='w', padx=5, pady=5)
    entry_image = gui.Entry(addwindow, width=40)
    entry_image.grid(row=5, column=1, padx=10, pady=10)

    def additem_submitbutton():
        itemname = entry_name.get()
        try:
            itemprice = float(entry_price.get())
            itemamount = int(entry_stocknumber.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid price and/or stock quantity value (in numbers).")
            return
        itemdesc = entry_description.get()
        itemurgent = entry_important.get()
        itemimage = entry_image.get()
        itemimage=itemimage.replace("\\", "/")
        itemprice = round(itemprice, 2)

        if not itemname or not itemprice or not itemamount or not itemdesc or not itemurgent or not itemimage:
            messagebox.showerror("Error", "Please fill out all fields.")
            return

        with open("stock.txt", "a") as file:
            file.write(f"{itemname}\n${itemprice}\n{itemamount}\n{itemdesc}\n{itemurgent}\n{itemimage}\n***\n")

        addwindow.destroy()
        refresh_product_list()

    gui.Button(addwindow, text="Submit", command=additem_submitbutton).grid(row=6)



def employeeinfo():
    employeepngs = [
    {"name":"Sally Beaumont", "image":r"C:\Users\(Computer)\Pictures\sallypfp.png", "dob":"January 2, 2004", "gender":"Female","position":"Store Clerk, Janitor", "notes":"Hired June 20, 2019. Considering for promotion."},
    {"name":"Candy Calloway", "image":r"C:\Users\(Computer)\Pictures\candypfp.png", "dob":"June 8, 1997", "gender":"Female","position":"Junior Supervisor", "notes":"Hired May 11, 2011"},
    {"name":"Norma Fisher", "image":r"C:\Users\(Computer)\Pictures\normapfp.png", "dob":"July 21, 2004", "gender":"Female","position":"Gas Station Attendant", "notes":"Hired June 17, 2024"},
    {"name":"Emmett Katz", "image":r"C:\Users\(Computer)\Pictures\emmettpfp.png", "dob":"March 9, 2006", "gender":"Male","position":"Cashier, Store Clerk", "notes":"Hired July 2, 2024. Considering for promotion."},
    {"name":"Kiki Morgan", "image":r"C:\Users\(Computer)\Pictures\kikipfp.png", "dob":"April 7, 2001 BC", "gender":"████████","position":"Front Store Supervisor", "notes":"Hired May 21, 2011"}]
    entryindex = 0
    imagecache = None

    employee_window = gui.Toplevel(root)
    employee_window.title("Employee Information")
    employee_window.geometry("450x200")
    employee_window.configure(bg='#CAFAD5')
   
    name_label = gui.Label(employee_window, text="", font=("Helvetica", 24))
    name_label.grid(row=0, column=2, columnspan=3, sticky="NW",  padx=5, pady=5)
    name_label.config(bg='#CAFAD5')

    imagepfp_label = gui.Label(employee_window, text="")
    imagepfp_label.grid(row=0, column=1, padx=5, pady=5)

    dob_label = gui.Label(employee_window, text="")
    dob_label.grid(row=0, column=2, padx=5, pady=5, sticky="w")
    dob_label.config(bg='#CAFAD5')

    gender_label = gui.Label(employee_window, text="")
    gender_label.grid(row=1, column=2, padx=5, pady=5, sticky="nw")
    gender_label.config(bg='#CAFAD5')

    position_label = gui.Label(employee_window, text="")
    position_label.grid(row=2, column=2, padx=5, pady=5, sticky="nw")
    position_label.config(bg='#CAFAD5')

    notes_label = gui.Label(employee_window, text="")
    notes_label.grid(row=3, column=2, padx=5, pady=5,sticky="nw")
    notes_label.config(bg='#CAFAD5')

    def update_display():
        nonlocal imagepfp_label
        nonlocal employeepngs
        nonlocal entryindex
        entry = employeepngs[entryindex]
        name_label.config(text=entry["name"])
        dob_label.config(text="Date of Birth: "+entry["dob"])
        gender_label.config(text="Gender: "+entry["gender"])
        notes_label.config(text="Notes: "+entry["notes"])
        position_label.config(text="Position: "+entry["position"])

        img = gui.PhotoImage(file=entry["image"])
        imagepfp_label.config(image=img)
        imagepfp_label.image = img 


    def next_entry():
        nonlocal entryindex
        entryindex = (entryindex + 1) % len(employeepngs)
        update_display()

    def prev_entry():
        nonlocal entryindex
        entryindex = (entryindex - 1) % len(employeepngs)
        update_display()


    prev_button = gui.Button(employee_window, text="<", command=prev_entry)
    prev_button.grid(row=0, column=0, sticky="W")

    next_button = gui.Button(employee_window, text=">", command=next_entry)
    next_button.grid(row=0, column=3, sticky="E")

    update_display()

    employee_window.mainloop()

def kanadewindow():
    window = gui.Toplevel(root)
    window.geometry("600x450")
    window.configure(bg='#CAFAD5')
    water = gui.PhotoImage(file = r'C:\Users\(Computer)\Pictures\dehydrated.png')
    gui.Label(window, image=water).pack()
    gui.Label(window, text="Dehydrated Water").pack()
    gui.Label(window, text="NOTE: Item is permanently out of stock due to excessive necessity.", fg="red").pack()
        
    window.mainloop()


def orbwindow():
    global file
    with open('malice.txt') as file:
        orbcontent = file.readlines()
        orbmalice = orbcontent[0]
        if orbmalice == "True":
            root.destroy()
            messagebox.showerror("Error!", "There was a problem with the system. Please restart the program.")
            with open('malice.txt', 'w')as file:
                file.truncate(0)
                file.write('False')
                file.close()

def viewschedule():
    global showcontextmenu
    schedule_window = gui.Toplevel(root)
    schedule_window.title("Schedule")
    schedule_window.geometry("300x450")
    schedule_window.configure(bg='#CAFAD5')
    employees = ["Sally Beaumont", "Emmett Katz", "Candy Calloway", "Kiki Morgan", "Norma Fisher"]
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    schedule = {}
    dropdowns = {}

    for i, day in enumerate(days):
        label = gui.Label(schedule_window, text=day)
        label.grid(row=i, column=0, padx=5, pady=5)
        selected_employee = gui.StringVar()
        dropdown = ttk.Combobox(schedule_window, textvariable=selected_employee)
        dropdown['values'] = employees
        dropdown.grid(row = i, column = 1, padx=5, pady=5)
        dropdowns[day]=dropdown
    viewemployees = gui.Button(schedule_window, text="View Employee Information", command=employeeinfo, padx=5, pady=5).grid(row = i+10, column = 1)
    schedule_window.mainloop()


def loaditems(filename):
    items = []
    with open("stock.txt", 'r') as file:
        content = file.read()

    raw_items = content.split('***')
    for entry in raw_items:
        lines = [line.strip() for line in entry.strip().split('\n') if line.strip()]
        if len(lines) == 6:
            name, price, stocknumber, description, important, imagepath = lines
            items.append((name, price, stocknumber, description, important, imagepath))
        else:
            print("Skipping malformed entry: {lines}")
   
    return items


def show_item_details(name, price, stocknumber, description, important, imagepath):
    detail = gui.Toplevel(root)
    detail.title(name)
    detail.config(bg="#CAFAD5")
    image=None
    if imagepath!= "N/A":
        try:
            image = gui.PhotoImage(file=imagepath)
        except Exception as e:
            print(f"Error loading image: {e}")
    else:
        print("Image path is N/A, no image to show")


    if image:
        img_label = gui.Label(detail, image=image)
        img_label.image = image
        img_label.grid(row=0, column=0, rowspan=3, padx=25, pady=25, sticky='nw')

    namelabel = gui.Label(detail, text=name, font=("Helvetica", 24), bg="#CAFAD5").grid(row=0, column=1, sticky="NW")
    pricelabel = gui.Label(detail, text=price, font=("Times New Roman", 12), bg="#CAFAD5").grid(row=1, column=1, sticky="nw")
    desclabel = gui.Label(detail, text=description, justify="left", wraplength="300", font=("Times New Roman", 12), bg="#CAFAD5").grid(row=2, column=1, sticky="N")

    if important != "N/A":
        importantlabel  = gui.Label(detail, text=important, font=("Helvetica", 15, "bold"), bg="#CAFAD5", fg="red").grid(row=4, columnspan=3,column=0, sticky="nw")

header = gui.Menu(root)
header_account = gui.Menu(header, tearoff = 0)
root.config(menu = header)
header.add_cascade(label = "Account", menu = header_account)
header_account.add_command(label = "View Schedule", command = viewschedule)
stockheader = gui.Menu(header,tearoff=0)
header.add_cascade(label="Stock", menu=stockheader)
stockheader.add_command(label = "Add Item...", command = additem)



title = gui.PhotoImage(file=r'C:\Users\(Computer)\Desktop\wordart.png')
titlepng = gui.Label(root, image=title, borderwidth=0)
titlepng.grid(row=0, column=0, columnspan=3)
motto = gui.Label(root, text="The home of everything you'll never need!", bg='#CAFAD5', fg='white', font=("Times New Roman", 24, "bold", "italic"))
motto.grid(row=1, column=0, columnspan=3)

items = loaditems("stock.txt")
image_refs = []
row, col = 2,0

for name, price, stocknumber, description, important, imagepath in items:
    try:
        img = gui.PhotoImage(file=imagepath)
        image_refs.append(img)
    except Exception as e:
        print(f"Error loading image '{imagepath}':{e}")
        continue

    btn = gui.Button(root, image=img, command=lambda n=name, p=price, s=stocknumber, d=description, im=important, ip=imagepath: show_item_details(n, p, s, d, im, ip))
    btn.grid(row=row, column=col, pady=25)
    lbl = gui.Label(root,text=name, bg="#CAFAD5")
    lbl.grid(row=row+1, column=col)

    col += 1
    if col >= 3:
        col = 0
        row += 2

# motto = Image.open("C:/Users/emilhilv/Downloads/wordart (4).png")
# motto = ImageTk.PhotoImage(motto)
# image_label = gui.Label(root, image=motto)
# image_label.pack()

root.mainloop()


#how can I make a scheduling program for employees in Python?
