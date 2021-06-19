from PIL import Image, ImageOps

def achar_borda(im, opt, borda):
    largura = im.size[0]
    altura = im.size[1]
    mx = round(largura/2)
    my = round(altura/2)
    #white = (255, 255, 255, 255)
    #black = (0, 0, 0, 255)

    if opt==False:
        cor = (0, 0, 0) #branco = (255) #preto = (0)
    else:
        cor = (255, 255, 255)

    if borda=='esq': # borda esquerda
        for i in range(0, largura):
            pixVal = im.getpixel((i, my))
            if pixVal == cor:
                break

    if borda == 'dir':  # borda direita
        for i in range(largura-1, 0, -1):
            pixVal = im.getpixel((i, my))
            if pixVal == cor:
                break

    if borda=='sup': # borda superior
        for i in range(0, altura):
            pixVal = im.getpixel((mx, i))
            if pixVal == cor:
                break

    if borda == 'inf':  # borda inferior
        for i in range(altura-1, 0, -1):
            pixVal = im.getpixel((mx, i))
            if pixVal == cor:
                break
    return i

# -------------- MAIN ------------------
fotolito=False; # Se fotolito=True não invert, senão faz a inversão (quando for utilizado o método térmico)
img = Image.open('pcb.bmp').convert('RGB')
if fotolito==False:
    img = ImageOps.invert(img)
img.show()

print(img.getpixel((120, 180)))


print('Esq=' + str(achar_borda(img, fotolito, 'esq')), ' Dir=' + str(achar_borda(img, fotolito, 'dir')))
print('Sup=' + str(achar_borda(img, fotolito, 'sup')), ' Inf=' + str(achar_borda(img, fotolito, 'inf')))

x1 = achar_borda(img, fotolito, 'esq')
y1 = achar_borda(img, fotolito, 'sup')
x2 = achar_borda(img, fotolito, 'dir')
y2 = achar_borda(img, fotolito, 'inf')
box = (x1+1, y1+1, x2+0, y2+0)
im2 = img.crop(box)
im2.show()

