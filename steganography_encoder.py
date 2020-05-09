"""
    Encoder
"""
class Encoder:

    def __init__(self, values, img):
        self.values = values
        self.img = img

    def write_msg(self, image, msg):
        msg_string = '^BEGIN_MESSAGE:' + str(len(msg)) + ':' + msg
        sa, sb, sc = image.shape
        a, b, c = 0, 0, 0

        for s in msg:
            for i in self.values:
                if ord(s) & i == 0:
                    if image[a][b][c] % 2 != 0:
                        image[a][b][c] -= 1
                else:
                    if image[a][b][c] % 2 == 0:
                        image[a][b][c] += 1

                if a < sa-1:
                    a += 1
        return image
