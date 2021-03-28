from PIL import Image, ImageFont, ImageDraw
from colored import fg, bg, attr
import time
ShowText = ['เธอ','์NaRak','จัง']
fg = [fg('#FF6700'),fg('medium_orchid_1b'),fg('#21de58')]
for i in range(3):
    font = ImageFont.truetype('TH Krub Bold.ttf', 60) 
    size = font.getsize(ShowText[i]) 
    print("size",size)
    image = Image.new('1', size, 1) 
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), ShowText[i], font=font)
    color = fg[i]
    res = attr('reset')
    for rownum in range(size[1]): 
        line = []
        for colnum in range(size[0]):
            if image.getpixel((colnum, rownum)): line.append(' '),
            else: line.append('#'),
        print(color+''.join(line)+res)
    time.sleep(1.5)