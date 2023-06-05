import argparse
import os
import sys

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


def convert(image_path, custom_width):
    img = Image.open(image_path).convert("L")
    width, height = img.size

    ratio = height / width
    if not custom_width:
        if width > 700:
            width = 700
    else:
        width = custom_width

    height = int(ratio * width * 0.55)
    img = img.resize((width, height))

    ascii_string = ""
    for pixel in img.getdata():
        intensity = get_pixel_density(pixel)
        character = intensity_to_character(intensity)
        ascii_string += character

    return ascii_string, width, height


def check_img_path(image_path):
    return os.path.isfile(image_path)


def check_out_dir(out_path):
    directory = os.path.dirname(out_path)
    directory = directory if len(directory) > 0 else "./"
    return os.path.isdir(directory)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Image To Ascii Art", description="Convert an image to Ascii art."
    )

    parser.add_argument("file", help="Path to image to convert")
    parser.add_argument("out", help="Path where to save converted image")
    parser.add_argument(
        "-w", "--width", type=int, help="Specify custom width of output"
    )
    args = parser.parse_args()

    if not check_img_path(args.file):
        print(f"The file {args.file} does not exist. Check that the path is correct.")
        sys.exit()

    if not check_out_dir(args.out):
        print(f"The directory {args.out} does not exist. Check that the is correct.")
        sys.exit()

    ascii_string, width, height = convert(args.file, args.width)
    save_image(ascii_string, width, height, args.out)
