
from PIL import Image, ImageFilter

im = Image.open('pix.png')

imageSizeW, imageSizeH = im.size

nonWhitePixels = []

for y in range(0, imageSizeW):
    for x in range(0, imageSizeH):
        pixVal = im.getpixel((x,y))
        if pixVal != (255, 255, 255):
            nonWhitePixels.append([x, y])

print(nonWhitePixels)

'''#Read image
im = Image.open('pcb.jpg')
#Display image
im.show()

imageW = im.size[0]
imageH = im.size[1]

for y in range(0, imageH):
    for x in range(0, imageW):
        #offset = y*imageW + x
        xy = (x, y)
        rgb = im.getpixel(xy)
        #HYP_Texture.SetValueTex2DByteRgb(texId, offset, rgb[0], rgb[1], rgb[2])
    if (rgb[0] == 0):
        break
print(xy)

#Applying a filter to the image
im_sharp = im.filter(ImageFilter.MinFilter)
#Saving the filtered image to a new file
im_sharp.save( 'pcb2.jpg','JPEG' )

#Splitting the image into its respective bands, i.e. Red, Green,
#and Blue for RGB
r,g,b = im_sharp.split()

#Viewing EXIF data embedded in image
im = Image.open('pcb2.jpg')
#Display image
im.show()


exif_data = im._getexif()
exif_data'''

