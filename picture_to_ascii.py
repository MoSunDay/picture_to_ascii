#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
import argparse
import sys

base_bit = 175
ascii_chars = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`\'. '

def get_char(r, g, b, alpha = 256):

    if alpha == 0:
        return ' '
    length = len(ascii_chars)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1) / length
    return ascii_chars[int(gray / unit)]

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('-o', '--output')
    parser.add_argument('--auto', type=bool, default=True, help='True|False')
    parser.add_argument('--width', type=int, default=0)
    parser.add_argument('--height', type=int, default=0)

    args = parser.parse_args()
    target_iamge = args.file
    target_iamge_width = args.width
    target_iamge_auto = args.auto
    target_iamge_height = args.height
    target_iamge_output = args.output

    target_iamge = Image.open(target_iamge)

    if target_iamge_width + target_iamge_height == 0:
        target_iamge_width, target_iamge_height = target_iamge.size
        if target_iamge_auto is True:
            if target_iamge_height >= target_iamge_width:
                target_iamge_width = int(base_bit * (float(target_iamge_width) / target_iamge_height))
                target_iamge_height = base_bit
            else:
                target_iamge_height = int(base_bit * (float(target_iamge_height) / target_iamge_width))
                target_iamge_width = base_bit
        else:
            if target_iamge_width or target_iamge_height == 0:
                print("width or height can't less 0 !")
                sys.exit(-1)
    else:
        pass
    # print target_iamge_width,target_iamge_height
    target_iamge = target_iamge.resize( (target_iamge_width, target_iamge_height ), Image.NEAREST)

    chars_txt = ""

    for height in range(target_iamge_height):
        for width in range(target_iamge_width):
            chars_txt += get_char(*target_iamge.getpixel((width, height)))
        chars_txt += '\n'

    print(chars_txt)

    if target_iamge_output:
        with open(target_iamge_output,'w') as f:
            f.write(chars_txt)
    else:
        with open("output.txt",'w') as f:
            f.write(chars_txt)