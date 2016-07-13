
from PIL import Image, ImageFont, ImageDraw
import os.path

CHAR_WIDTH = 6
CHAR_HEIGHT = 8
START_PIXEL_W = 0
START_PIXEL_H = 1

img = Image.open("font_ati_smallw_6x8.png")

f = open('font.h', 'w')
f.write('const unsigned char font[][%d] = {\n' % (CHAR_WIDTH,))

print ("Image width x height: ", img.size)

for i in range(START_PIXEL_H, img.size[1]-1, CHAR_HEIGHT):
    for j in range(START_PIXEL_W, img.size[0]-1, CHAR_WIDTH):
        print (i, j)
        ints = []
        for jj in range(CHAR_WIDTH):
            val = 0
            for ii in range(CHAR_HEIGHT):
                rgb = img.getpixel((j+jj, i+ii))
                val = (val >> 1) | (0x80 if rgb[0] > 0 else 0)
            ints.append('0x%.2x' % (val))
        f.write('\t{%s}, \n' % (','.join(ints),))


f.write('};\n\n')


