import qrcode as qc
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def gen_qr():
    url = entry.get() 
    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL only!")
        return

    qr = qc.QRCode(version=1, error_correction=qc.constants.ERROR_CORRECT_L, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="pink", back_color="black")
    img.save("qrimg.png")

    qr_img = Image.open("qrimg.png")
    qr_img = qr_img.resize((200, 200))  
    qr_photo = ImageTk.PhotoImage(qr_img, master=root)  

    qr_label.config(image=qr_photo)
    qr_label.image = qr_photo 

root = Tk()
root.title("QR Code Generator")
root.geometry("400x400")

label = Label(root, text="Enter URL or Text:", font=("Arial", 14))
label.pack(pady=10)

entry = Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=5)

button = Button(root, text="Generate QR Code", font=("Arial", 12), command=gen_qr)
button.pack(pady=10)

qr_label = Label(root)
qr_label.pack(pady=20)

root.mainloop()
