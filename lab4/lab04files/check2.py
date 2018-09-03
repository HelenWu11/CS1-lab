from PIL import Image
from check2_helper import make_square

imc = Image.open('ca.jpg')
imh = Image.open('hk.jpg')

im = Image.new('RGB',(512,512))
im_ca = make_square(imc)
im_hk = make_square(imh)
im.paste(im_ca, (0,0))
im.paste(im_hk, (256,0))
im.save('two_by_two.jpg')
im.show()