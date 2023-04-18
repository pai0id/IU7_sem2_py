from PIL import Image


def encrypt_image(img_path, message):
    image = Image.open(img_path)
    pixels = image.load()
    width, height = image.size
    try:
        message_bytes = bytearray(message, "ascii")
    except UnicodeEncodeError:
        return img_path, 1
    message_bytes.extend(b"\x00\x00\x00")
    index = 0
    cnt = 0
    bits = bin(message_bytes[index]).lstrip("0b").zfill(8)
    for row in range(height):
        for col in range(width):
            r, g, b = pixels[col, row]
            if index < len(message_bytes):
                bits = bin(message_bytes[index]).lstrip("0b").zfill(8)
                r &= 0b11111110
                r |= int(bits[cnt])
                cnt += 1
                g &= 0b11111110
                g |= int(bits[cnt])
                cnt += 1
                if cnt != 8:
                    b &= 0b11111110
                    b |= int(bits[cnt])
                    cnt += 1
                if cnt == 8:
                    cnt = 0
                    index += 1
            pixels[col, row] = (r, g, b)

    new_path = f"{img_path.rstrip('.bmp').rstrip('_enc')}_enc.bmp"
    image.save(new_path)
    return new_path, 0


def decrypt_image(img_path):
    image = Image.open(img_path)
    pixels = image.load()
    width, height = image.size
    message_bytes = bytearray()
    cnt = 0
    curr_bits = ''
    for row in range(height):
        for col in range(width):
            r, g, b = pixels[col, row]
            bits = ""
            bits += bin(r & 0b00000001).lstrip("0b").zfill(1)
            bits += bin(g & 0b00000001).lstrip("0b").zfill(1)
            if cnt % 3 != 2:
                bits += bin(b & 0b00000001).lstrip("0b").zfill(1)
            curr_bits += bits
            cnt += 1
            if cnt % 3 == 0:
                message_bytes.extend(bytes([int(curr_bits, 2)]))
                curr_bits = ''
                if message_bytes[-3:] == b"\x00\x00\x00":
                    try:
                        return message_bytes[:-3].decode("ascii")
                    except UnicodeDecodeError:
                        pass

    return ""
