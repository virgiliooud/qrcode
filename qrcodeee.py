import qrcode
from PIL import Image

link = str(input('Digite o link que voê quer transformar emm QRCODE:'))
imagem = qrcode.make(link)
imagem.save('meuqrcode.jpg')
# Abre a imagem
imagem = Image.open('meuqrcode.jpg')

# Mostra a imagem
imagem.show()