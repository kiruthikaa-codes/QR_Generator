import qrcode as qc

def gen_qr(text):

    qr = qc.QRCode (
        version =1,
        error_correction = qc.constants.ERROR_CORRECT_L,
        border=5,
        box_size = 10
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color = "pink" , back_color="black")
    img.save("qrimage001.png")

url = input("Enter your url: ")
gen_qr(url)