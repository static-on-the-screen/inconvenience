import tkinter as gui
from PIL import Image, ImageTk

root = gui.Tk()
root.title("Inconvenience Store")
root.geometry("900x650")
root.configure(bg='#CAFAD5')

header = gui.Menu(root)
header_account = gui.Menu(header, tearoff = 0)
root.config(menu = header)
header.add_cascade(label = "Account", menu = header_account)
header_account.add_command(label = "View Employees", command = 'None')
header_account.add_separator()
header_account.add_command(label = "Sign Out...", command = 'None')
header.add_cascade(label = "Stock")

kanade = gui.PhotoImage(file = r'C:\Users\emilhilv\Downloads\lizarddog.png')
gui.Button(root, text="please", image = kanade).pack()


# motto = Image.open("C:/Users/emilhilv/Downloads/wordart (4).png")
# motto = ImageTk.PhotoImage(motto)
# image_label = gui.Label(root, image=motto)
# image_label.pack()

root.mainloop()