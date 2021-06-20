from PIL import ImageOps
from PIL import Image


def achar_borda(im: Image, opt: bool, borda: str):
    largura = im.size[0]
    altura = im.size[1]
    mx = round(largura / 2)
    my = round(altura / 2)
    # white = (255, 255, 255, 255)
    # black = (0, 0, 0, 255)

    if not opt:
        cor = (0, 0, 0)  # branco = (255) #preto = (0)
    else:
        cor = (255, 255, 255)

    if borda == 'esq':  # borda esquerda
        for i in range(0, largura):
            pix_val = im.getpixel((i, my))
            if pix_val == cor:
                break

    if borda == 'dir':  # borda direita
        for i in range(largura - 1, 0, -1):
            pix_val = im.getpixel((i, my))
            if pix_val == cor:
                break

    if borda == 'sup':  # borda superior
        for i in range(0, altura):
            pix_val = im.getpixel((mx, i))
            if pix_val == cor:
                break

    if borda == 'inf':  # borda inferior
        for i in range(altura - 1, 0, -1):
            pix_val = im.getpixel((mx, i))
            if pix_val == cor:
                break
    return i


def get_concat_h_repeat(im: Image, column: int):
    dst = Image.new('RGB', (im.width * column, im.height))
    for x in range(column):
        dst.paste(im, (x * im.width, 0))
    return dst


def get_concat_v_repeat(im: Image, row: int):
    dst = Image.new('RGB', (im.width, im.height * row))
    for y in range(row):
        dst.paste(im, (0, y * im.height))
    return dst


def get_concat_tile_repeat(im: Image, row: int, column: int):
    dst_h = get_concat_h_repeat(im, column)
    return get_concat_v_repeat(dst_h, row)


def openImage(path: str, is_photolit: bool):
    # Sugestão: Adotar isso como argumento no método, via linha de comando.
    # fotolito = False  # Se fotolito=True não inverte, senão faz a inversão (quando for utilizado o método térmico)
    im2 = Image.open(path).convert('RGB')
    if not is_photolit:
        im2 = ImageOps.invert(im2)
    # qual a conta feita pra chegar nesses números?
    # print(img2.getpixel((120, 180)))

    # vou suprimir isto para o ambiente de produção. Por favor se quiser, habilite novamente.
    # print('Esq=' + str(m.achar_borda(img, fotolito, 'esq')), ' Dir=' + str(m.achar_borda(img, fotolito, 'dir')))
    # print('Sup=' + str(m.achar_borda(img, fotolito, 'sup')), ' Inf=' + str(m.achar_borda(img, fotolito, 'inf')))
    return borda(im2, is_photolit, 20)


def borda(img, fotolito, espessura):
    x1 = achar_borda(img, fotolito, 'esq')
    y1 = achar_borda(img, fotolito, 'sup')
    x2 = achar_borda(img, fotolito, 'dir')
    y2 = achar_borda(img, fotolito, 'inf')
    box = (x1 + 1, y1 + 1, x2 + 0, y2 + 0)
    im2 = img.crop(box)
    im2 = ImageOps.expand(im2, espessura, fill='white')
    return im2
