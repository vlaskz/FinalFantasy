from PIL import Image, ImageFilter

def achar_borda(eixo):
    largura = im.size[0]
    altura = im.size[1]
    mx = round(largura/2)
    my = round(altura/2)
    #white = (255, 255, 255, 255)
    #black = (0, 0, 0, 255)
    branco = (255)
    preto = (0)
    if eixo=='x':
        for i in range(0, largura):
            pixVal = im.getpixel((i, my))
            if pixVal == branco:
                break
    if eixo=='y':
        for i in range(0, altura):
            pixVal = im.getpixel((mx, i))
            if pixVal == branco:
                break
    return i

# --------- MAIN --------------
im = Image.open('pcb.bmp')
im.show()
print('posx='+ str(achar_borda('x')), ' posy='+ str(achar_borda('y')))

