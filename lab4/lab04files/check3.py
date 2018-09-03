from PIL import Image

im1 = Image.open('1.jpg')
im2 = Image.open('2.jpg')
im3 = Image.open('3.jpg')
im4 = Image.open('4.jpg')
im5 = Image.open('5.jpg')
im6 = Image.open('6.jpg')

im = Image.new('RGB',(1000,360))
im_1 = im1.resize((int(im1.size[0]/(im1.size[1]/256)),256))
im_2 = im2.resize((int(im2.size[0]/(im1.size[1]/256)),256))
im_3 = im3.resize((int(im3.size[0]/(im1.size[1]/256)),256))
im_4 = im4.resize((int(im4.size[0]/(im1.size[1]/256)),256))
im_5 = im5.resize((int(im5.size[0]/(im1.size[1]/256)),256))
im_6 = im6.resize((int(im6.size[0]/(im1.size[1]/256)),256))

a = int(im1.size[0]/(im1.size[1]/256))
b = int(im1.size[0]/(im2.size[1]/256))
c = int(im1.size[0]/(im3.size[1]/256))
d = int(im1.size[0]/(im4.size[1]/256))
e = int(im1.size[0]/(im5.size[1]/256))
f = int(im1.size[0]/(im6.size[1]/256))

im.paste(im_1,(31,20))
im.paste(im_2,((41+a),60))
im.paste(im_3,((51+a+b),20))
im.paste(im_4,((61+a+b+c),60))
im.paste(im_5,((71+a+b+c+d),20))
im.paste(im_6,((81+a+b+c+d+e),60))

im.save('im.jpg')
im.show()
