from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
    return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)

# 随机颜色2:
def rndColor2():
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)

width = 60 * 6
height = 60*6
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('/usr/share/fonts/wps-office/simhei.ttf', 80)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
image.save('code1.jpg', 'jpeg')
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())

image.save('code2.jpg', 'jpeg')
# 输出文字:
for t in range(6):
    draw.text((60 * t + 10, random.randint(10,280)), rndChar(), font=font,fill=rndColor2())
# 模糊:
image.save('code4.jpg', 'jpeg')
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')