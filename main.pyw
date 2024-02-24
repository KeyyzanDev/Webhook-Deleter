import time
import os
import tkinter
import sys
import webbrowser

try:
    from PIL import Image
except:
    os.system('py -m pip install pillow')
    from PIL import Image
try:
    import requests
except:
    os.system("py -m pip install requests")
    import requests
try:
    import customtkinter as ctk
except:
    os.system("py -m pip install customtkinter")
    import customtkinter as ctk

# window
app = ctk.CTk()
app.title("")
app.geometry("600x350+650+325")
app.iconbitmap('assets/favicon.ico')
app.attributes('-alpha',0.9)
app.resizable(False,False)
ctk.set_appearance_mode("dark")

# widgets
    #logo
logo = ctk.CTkImage(light_image=Image.open('assets/logolight.png'),
                    dark_image=Image.open('assets/logodark.png'),
                    size=(300,83))
logolabel = ctk.CTkLabel(app, text="", image=logo)
logolabel.pack(pady=15)

    # entry
entry = ctk.CTkEntry(app, placeholder_text="Enter Webhook URL", width=300, corner_radius=5)
entry.pack()

# delete webhook
    #result
result = ""
label = ctk.CTkLabel(app, text=result)
label.pack()
def delete():
    #verify
    webhook = entry.get()
    verify = requests.get(webhook)
    if verify.status_code == 200:
        result = ("This webhook has been successfully deleted.")
        label.configure(text=result)
    elif verify.status_code == 404:
        result = ("This webhook isn't available.")
        label.configure(text=result)
    #delete
    requests.delete(webhook)

button = ctk.CTkButton(app, text="Delete", fg_color="#00fff6",
                       hover_color="#03d2cb",
                       text_color="#000000",
                       command=delete,
                       height=50,
                       font=("Tahoma", 20))
button.pack(pady=10)

    #combobox
def optionmenu_callback(choice):
    ctk.set_appearance_mode(optionmenu.get())

optionmenu = ctk.CTkOptionMenu(app, values=["System", "Dark", "Light"],
                               command=optionmenu_callback,
                               dynamic_resizing=True,
                               width=90,
                               fg_color="#00fff6",
                               text_color="#000000",
                               button_color="#03d2cb",
                               button_hover_color="#00918c",
                               corner_radius=20)
optionmenu.set("Themes")
optionmenu.pack()
optionmenu.place(x=15,y=305)
    #credits
credits = ctk.CTkLabel(app, text="Credits: Keyyzan")
credits.pack()
credits.place(x=485, y=305)

url = "https://github.com/KeyyzanDev"

def redirect(url):
    webbrowser.open_new(url)
credits.bind("<Button-1>", lambda e: redirect("https://github.com/KeyyzanDev"))

# run
app.mainloop()

