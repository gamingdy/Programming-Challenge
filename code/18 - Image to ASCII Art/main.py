from PIL import Image, ImageDraw, ImageFont


CHARACTER = [".", ",", ":", ";", "+", "*", "?", "%", "$", "#", "@"]


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
        file.write(ascii_image)

    image = Image.new("L", (width * 2, height * 4))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("RobotoMono-Regular.ttf", 3)
    draw.multiline_text((0, 0), ascii_image, font=font, fill="white", spacing=0)
    image.save(out_file)


def convert(image_path):
    img = Image.open(image_path).convert("L")
    width, height = img.size

    ratio = height / width

    if width > 500:
        width = 500

    height = int(ratio * width * 0.55)
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
