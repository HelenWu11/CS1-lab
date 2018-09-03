from PIL import Image
def make_square(im):
    if im.size[0]>im.size[1]:
        im_crop = im.crop((0,0,im.size[1],im.size[1]))
        return im_crop.resize((256,256))
    elif im.size[0]<im.size[1]:
        im_crop = im.crop((0,0,im.size[0],im.size[0]))
        return im_crop.resize((256,256))


    
    
    