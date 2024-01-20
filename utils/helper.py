from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# Generate verification code png file
def generate_verification_code_image(width=120, height=30, font_file= 'Monaco.ttf', font_size=28, char_length=5):
    code =[]
    img = Image.new(mode="RGB", size=(width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img, mode="RGB")

    def rndChar():
        """Generate random number"""
        return chr(random.randint(65, 90))
    
    def rndColor():
        """Generate random color"""
        return (random.randint(0, 255), random.randint(10, 255), random.randint(64, 255))

    # Write text
    font = ImageFont.truetype(font_file, font_size)
    for i in range(char_length):
        char = rndChar()
        code.append(char)
        h = random.randint(0, 4)
        draw.text([i*width/char_length, h], char, font=font, fill=rndColor())

    # Draw disturbing points
    for i in range(40):
        draw.point([random.randint(0,width),random.randint(0, height)],fill=rndColor())

    # Draw disturbing circles
    for i in range(40):
        draw.point([random.randint(0, width),random.randint(0,height)], fill=rndColor())
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.arc((x, y, x + 4, y + 4), 0, 90,fill=rndColor())

    # Draw disturbing lines
    for i in range(5):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        draw.line((x1, y1, x2, y2), fill=rndColor())
    
    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    # print(img, ''.join(code))
    # with open('code.png', 'wb') as f:
    #     img.save(f, format="png")
    return img, ''.join(code)

generate_verification_code_image()