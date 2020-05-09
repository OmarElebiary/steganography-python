#! /usr/bin/env python3
import numpy as np
from PIL import Image
def read_image(image_path):
    # Read image file
    img = Image.open(image_path)
    image_arr = np.asarray(img).copy()
    return image_arr

if __name__ == '__main__':

    import argparse
    from steganography_decoder import Decoder
    from steganography_encoder import Encoder

    values = []

    for i in range(7, -1, -1):
        res = b'\x01'[0] << i
        values.append(res)

    parser = argparse.ArgumentParser()
    parser.add_argument('--action', required=True)
    parser.add_argument('--path', required=True)
    parser.add_argument('--output')
    parser.add_argument('--message')

    args = parser.parse_args()
    action = args.action.lower()
    output_path = args.output
    message = args.message
    file_path = args.path

    if action != 'encode' and action != 'decode':
        parser.error('action is not valid')

    image_array = read_image(file_path)

    if action == 'decode':
        decoder = Decoder(values, image_array)
        res = decoder.get_values()
        print('Result: ' + res)

    if action == 'encode':
        if not output_path or not message:
            parser.error('Missing output path and message')
        encoder = Encoder(values, image_array)
        encoded_image = encoder.write_msg(image_array, message)
        new_image = Image.fromarray(encoded_image)
        new_image.save(output_path)

