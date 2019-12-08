import collections
import matplotlib.pyplot as plt

from utils import timed


@timed
def part_one():
    img = open('inputs/2019-08.txt').read()
    layers = [img[i:i + 150] for i in range(0, len(img), 150)]

    min_zeros = 150
    min_layer = 0
    for i, layer in enumerate(layers):
        zeros = len([pixel for pixel in layer if pixel == '0'])
        if zeros < min_zeros:
            min_zeros = zeros
            min_layer = i

    ones = len([pixel for pixel in layers[min_layer] if pixel == '1'])
    twos = len([pixel for pixel in layers[min_layer] if pixel == '2'])
    print(ones * twos)

@timed
def part_two():
    img = open('inputs/2019-08.txt').read()
    layers = [img[i:i + 150] for i in range(0, len(img), 150)]

    i = 0
    determined_positions = {}
    for layer in layers:
        for i, pixel in enumerate(layer):
            if pixel != '2':
                if determined_positions.get(i) is None:
                    determined_positions[i] = pixel

    ordered_img = collections.OrderedDict(sorted(determined_positions.items()))

    msg = ''
    for v in ordered_img.values():
        msg += v

    formatted_msg_str = [msg[i:i + 25] for i in range(0, len(msg), 25)]
    formatted_msg = [[int(p) for p in layer] for layer in formatted_msg_str]
    plt.imshow(formatted_msg)
    plt.show()


part_one()
part_two()
