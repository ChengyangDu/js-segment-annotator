from PIL import Image

img = Image.open('../data/images/1.jpg').convert('L')
img.save('../data/images/1gray.jpg')