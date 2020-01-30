# pip install qrcode[pil]
import qrcode


# for styling the QRCode
qr = qrcode.QRCode(
    version=1,
    box_size=15,
    border=5
)

# data holds the information
data = 'What ever you add here is data'
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('SecondGo.png')