#print("Olá Mundo!!!")
from PIL import Image
#Read image
im = Image.open('pcb.jpg')
Display image
im.show()

'''# ou o códido a seguir

import HYP_Utils
import sys

from PIL import Image

scriptDir = HYP_Utils.GetDemoDir()

PIL_Version = Image.VERSION

img_filename = "%s/pcb.jpg" % scriptDir
im = Image.open(img_filename)
im.show()'''

