from PIL import Image, ImageDraw, ImageFont

text = "平泉 最高"

font_path = "C:\Windows\Fonts/BIZ-UDGOTHICB.TTC"
font_size = 333
font_color = (100, 230, 236)
font = ImageFont.truetype(font_path, font_size)

im = Image.open("konjikido_01.jpg")
im = im.resize((3084, 1356))
draw = ImageDraw.Draw(im)

(font_w, font_h), (offset_x, offset_y) = font.font.getsize(text)
img_w, img_h = im.size
pos = ((img_w - font_w) / 2, (img_h - font_h) / 2)

draw.text(pos, text, font=font, fill=font_color)
im.save("ex2.jpg")
im.show()
