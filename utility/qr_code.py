import qrcode

data = input('enter the text or URL for the QR code: ' ).strip()
img = qrcode.make(data)
filename = input('enter the file name: ').strip() + '.png'
path = f"images/{filename}"
img.save(path)
print(f'file saved as {filename}') 
