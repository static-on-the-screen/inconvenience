import tkinter as gui
from tkinter import messagebox

with open("malice.txt") as file:
    orbcontent = file.readlines()
    orbmalice = orbcontent[0]
    print(orbmalice)

root = gui.Tk()
root.title("Inconvenience Store")
root.geometry("900x650")
root.configure(bg='#CAFAD5')


def kanadewindow():
    window = gui.Toplevel(root)
    window.geometry("600x450")
    window.configure(bg='#CAFAD5')
    water = gui.PhotoImage(file = r'C:\Users\emilhilv\Pictures\dehydrated.png')
    gui.Label(window, image=water).pack()
    gui.Label(window, text="Dehydrated Water").pack()
    gui.Label(window, text="NOTE: Item is permanently out of stock due to unwanted necessity.", fg="red").pack()
    window.mainloop()


def orbwindow():
    global file
    root.destroy()
    messagebox.showerror("Error!", "There was a problem with the system. Please restart the program.")
    with open('malice.txt', 'w')as file:
        file.truncate(0)
        file.write('False')
        file.close()

header = gui.Menu(root)
header_account = gui.Menu(header, tearoff = 0)
root.config(menu = header)
header.add_cascade(label = "Account", menu = header_account)
header_account.add_command(label = "View Employees", command = 'None')
header_account.add_separator()
header_account.add_command(label = "Sign Out...", command = 'None')
header.add_cascade(label = "Stock")


kanade = gui.PhotoImage(file = r'C:\Users\emilhilv\Pictures\dehydrated.png')
gui.Button(root, text="please", image = kanade, command = kanadewindow).pack()
gui.Label(root, text="Dehydrated Water").pack()
gnomesuke = gui.PhotoImage(file = r'C:\Users\emilhilv\Pictures\gnomesuke.png')
gui.Button(root, text="please", image = gnomesuke, command = "None").pack()
gui.Label(root, text="?????").pack()
if orbmalice == 'True':
    orb = gui.PhotoImage(file = r'C:\Users\emilhilv\Pictures\orb.png')
elif orbmalice == 'False':
    orb = gui.PhotoImage(file=r'C:\Users\emilhilv\Pictures\normalorb.png')
gui.Button(root, image = orb, command = orbwindow).pack()

# motto = Image.open("C:/Users/emilhilv/Downloads/wordart (4).png")
# motto = ImageTk.PhotoImage(motto)
# image_label = gui.Label(root, image=motto)
# image_label.pack()

root.mainloop()
