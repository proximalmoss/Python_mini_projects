import pyqrcode
from pyqrcode import QRCode
s="https://youtu.be/1fVogQNYYzk?si=rxbEQgPimrpsWZ7C"
url=pyqrcode.create(s)
url.svg("meme.svg",scale=8)