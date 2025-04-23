import tkinter as gui


root = gui.Tk()
root.title("Inconvenience Store")
root.geometry("900x650")

header = gui.Menu(root)
header_account = gui.Menu(header, tearoff = 0)
root.config(menu = header)
header.add_cascade(label = "Account", menu = header_account)
header_account.add_command(label = "View Messages", command = 'None')
header_account.add_separator()
header_account.add_command(label = "Sign Out...", command = 'None')

motto = gui.PhotoImage(file = "glitter.gif")
motto_label = gui.Label(root, image = motto)
motto_label.pack()


root.mainloop()