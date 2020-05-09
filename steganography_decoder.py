"""
    Steganography Decoder
"""
class Decoder:

    def __init__(self, values, img):
        self.values = values
        self.img = img

    def read_image_chars(self, img, a, b, c, n):
        str = []
        for i in range(n):
            ch = 0
            for j in self.values:
                num = self.img[a][b][c]
                if num % 2 != 0:
                    ch += j
                a += 1
            str.append(chr(ch))

        return ''.join(str)


    def read_image(self, img):
        res = self.read_image_chars(self.img, 0, 0, 0, 15)
        if res != "^BEGIN_MESSAGE:":
            return res

        a, b, c = 8*20, 0, 0
        dig = []
        flag = 0
        for i in range(100):
            if flag == 1:
                break
            ch = 0
            for j in self.values:
                num = img[a][b][c]
                if num % 2 != 0:
                    ch += j
                a += 1
            if ch == ord(':'):
                flag = 1
                break
            else:
                dig.append(chr(c))

        dig = int(''.join(dig))
        res = self.read_image_chars(self.img, na, 0, 0, dig)
        return res

    def get_values(self):
        val = self.read_image(self.img)
        return val
