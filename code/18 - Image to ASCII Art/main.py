from PIL import Image, ImageDraw, ImageFont


CHARACTER = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]



def get_pixel_density(pixel):
    return pixel // 25


def intensity_to_character(intensity):
    return CHARACTER[intensity]


def save_image(ascii_string, width, height, out_file):
    ascii_image = ""
    line = 0
    for index in range(0, len(ascii_string), width):
        ascii_image += ascii_string[index : index + width]
        ascii_image += "\n"
        line += 1

    with open(f"{out_file}.txt", "w") as file:
        # file.write(HTML_TEMPLATE.format(CSS_STYLE, ascii_image))
        file.write(ascii_image)

    print(width, height)
    image = Image.new("L", (width * 2, height * 4))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("RobotoMono-Regular.ttf", 4)
    # draw.text((0, 0), "test")
    print("Writing text in image")
    draw.multiline_text((0, 0), ascii_image, font=font, fill="white", spacing=0)
    # image.show()
    image.save("test.png")


def convert(image_path):
    img = Image.open(image_path).convert("L")
    width, height = img.size

    ratio = height / width
    # width = 500
    width = width * 4
    height = int(ratio * width * 0.5)
    # img.thumbnail((width, height), Image.Resampling.LANCZOS)
    img = img.resize((width, height))

    ascii_string = ""
    for pixel in img.getdata():
        intensity = get_pixel_density(pixel)
        character = intensity_to_character(intensity)
        ascii_string += character

    return ascii_string, width, height


ascii_, width, height = convert("566208.jpg")
save_image(ascii_, width, height, "res")
