# pip install qrcode[pil]
import qrcode

qr = qrcode.make('Add information')
qr.save('Myqrcode.png')

# second and easier method
