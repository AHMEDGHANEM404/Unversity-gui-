import pyqrcode
url = pyqrcode.create('https://www.azhar.eg/splash.html')
url.svg('uca-url.svg', scale=8)
print(url.terminal(quiet_zone=1))