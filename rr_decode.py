import sys

def decode_b0747746(enc_data):
    print('[!] Type [b0747746] is detected!')
    print('[+] Decoding...')

    dec_data = []
    xor_key = 1219836524

    for i in range(len(enc_data)):
        for _ in range(7):
            x0 = (xor_key & 0x20000000) == 0x20000000
            x1 = (xor_key & 8) == 8
            x2 = xor_key & 1
            x3 = 1 + (x0 ^ x1 ^ x2)
            xor_key = ((xor_key + xor_key) + x3) & 0xFFFFFFFF
        dec_data.append(int.from_bytes(enc_data[i], "little") ^ (xor_key % 256))

    return dec_data

def decode_b25a6f00(enc_data):
    print('[!] Type [b25a6f00] is detected!')
    print('[+] Decoding...')

    dec_data = []

    for i in range(len(enc_data)):
        if i % 2 == 0:
            dec_data.append(int.from_bytes(enc_data[i],  "little") ^ 0xff)
        else:
            dec_data.append(int.from_bytes(enc_data[i],  "little"))

    return dec_data

def decode_b2a66dff(enc_data):
    print('[!] Type [b2a66dff] is detected!')
    print('[+] Decoding...')

    dec_data = []

    for i in range(len(enc_data)):
        dec_data.append(int.from_bytes(enc_data[i],  "little") ^ 0xfc)
    
    dec_data[0] = 0x4d
    dec_data[2] = 0x90

    return dec_data

def decode_f2a32072(enc_data):
    print('[!] Type [f2a32072] is detected!')
    print('[+] Decoding...')

    dec_data = []
    xor_key = 2079624803

    for i in range(len(enc_data)):
        for _ in range(7):
            x0 = (xor_key & 0x40000000) == 0x40000000
            x1 = (xor_key & 8) == 8
            x2 = xor_key & 1
            x3 = x0 ^ x1 ^ x2
            xor_key = ((xor_key + xor_key) + x3) & 0xFFFFFFFF
        dec_data.append(int.from_bytes(enc_data[i], "little") ^ (xor_key % 256))

    return dec_data

def decode_b2a46eff(enc_data):
    print('[!] Type [b2a46eff] is detected!')
    print('[+] Decoding...')

    dec_data = []

    for i in range(len(enc_data)):
        dec_data.append(int.from_bytes(enc_data[i],  "little") ^ 0xff)
    
    dec_data[1] = 0x5a
    dec_data[2] = 0x90

    return dec_data

def decode_a9a46efe(enc_data):
    print('[!] Type [a9a46efe] is detected!')
    print('[+] Decoding...')

    dec_data = []

    for i in range(len(enc_data)):
        dec_data.append(((int.from_bytes(enc_data[i],  "little") ^ 0x7b) + 0x7b) % 256)
    
    return dec_data

def decode_945fdad8(enc_data):
    print('[!] Type [945fdad8] is detected!')
    print('[+] Decoding...')

    dec_data = []
    xor_key = 1387678300

    for i in range(len(enc_data)):
        for _ in range(7):
            x0 = (xor_key & 0x20000000) == 0x20000000
            x1 = (xor_key & 8) == 8
            x2 = xor_key & 1
            x3 = 1 + (x0 ^ x1 ^ x2)
            xor_key = ((xor_key + xor_key) + x3) & 0xFFFFFFFF
        dec_data.append(int.from_bytes(enc_data[i], "little") ^ (xor_key % 256))

    return dec_data

def decode_95a2748e(enc_data):
    print('[!] Type [95a2748e] is detected!')
    print('[+] Decoding...')

    dec_data = []
    xor_key = 1404390492

    for i in range(len(enc_data)):
        for _ in range(7):
            x0 = (xor_key & 0x20000000) == 0x20000000
            x1 = (xor_key & 8) == 8
            x2 = xor_key & 1
            x3 = 1 + (x0 ^ x1 ^ x2)
            xor_key = ((xor_key + xor_key) + x3) & 0xFFFFFFFF
        dec_data.append(int.from_bytes(enc_data[i], "little") ^ (xor_key % 256))

    return dec_data

def rc4_ksa(key):
    x = 0
    y = 0
    s = list(range(256))

    for i in range(0x100):
        y = (key[x % len(key)] + s[i] + y) & 0xff
        s[i], s[y] = s[y], s[i]
        x += 1
    return s

def rc4_prga(enc_data, s):
    x = 0 
    y = 0
    for i in range(len(enc_data)):
        x = (x + 1) & 0xff
        y = (s[x] + y) & 0xff
        s[x], s[y] = s[y], s[x]
        enc_data[i] = int.from_bytes(enc_data[i], "little") ^ s[(s[x] + s[y]) & 0xff]
    return bytes(enc_data)

def decode_4da2ee67(enc_data):
    print('[!] Type [4da2ee67] is detected!')
    print('[+] Decoding...')

    key = bytearray(b"123456")
    s = rc4_ksa(key)
    dec_data = rc4_prga(enc_data, s)

    return dec_data

def decode_8291706f(enc_data):
    print('[!] Type [8291706f] is detected!')
    print('[+] Decoding...')

    key = bytearray(b"2YlK77")
    s = rc4_ksa(key)
    dec_data = rc4_prga(enc_data, s)

    return dec_data

def decode_614a860c(enc_data):
    print('[!] Type [614a860c] is detected!')
    print('[+] Decoding...')

    key = bytearray(b"923hrg")
    s = rc4_ksa(key)
    dec_data = rc4_prga(enc_data, s)

    return dec_data

def decode_0f7850ba(enc_data):
    print('[!] Type [614a860c] is detected!')
    print('[+] Decoding...')

    key = bytearray(b"c34H4y")
    s = rc4_ksa(key)
    dec_data = rc4_prga(enc_data, s)

    return dec_data

def decode_8291986f(enc_data):
    print('[!] Type [8291986f] is detected!')
    print('[+] Decoding...')

    key = bytearray(b"2YlK77")
    s = rc4_ksa(key)
    dec_data = rc4_prga(enc_data, s)

    return dec_data

def decode_2333f765(enc_data):
    print('[!] Type [2333f765] is detected!')
    print('[+] Decoding...')

    key = bytearray(b"nigerdi")
    dec_data = []

    for i in range(len(enc_data)):
        dec_data.append(int.from_bytes(enc_data[i],  "little") ^ key[i % len(key)])

    return dec_data

def main():
    args = sys.argv
    if len(args) != 3:
        print('[!] Usage: "' + args[0] + ' [Input] [Output]"')
        sys.exit(-1)

    signature = [
        [0xb0, 0x74, 0x77, 0x46],
        [0xb2, 0x5a, 0x6f, 0x00],
        [0xb2, 0xa6, 0x6d, 0xff],
        [0xf2, 0xa3, 0x20, 0x72],
        [0xb2, 0xa4, 0x6e, 0xff],
        [0xa9, 0xa4, 0x6e, 0xfe],
        [0x94, 0x5f, 0xda, 0xd8],
        [0x95, 0xa2, 0x74, 0x8e],
        [0x4d, 0xa2, 0xee, 0x67],
        [0x82, 0x91, 0x70, 0x6f],
        [0x61, 0x4a, 0x86, 0x0c],
        [0x0f, 0x78, 0x50, 0xba],
        [0x82, 0x91, 0x98, 0x6f],
        [0x23, 0x33, 0xf7, 0x65]
    ]

    enc_data = []

    with open(args[1], 'rb') as f:
        while True:
            byte = f.read(1)
            if byte:
                enc_data.append(byte)
            else:
                break

    header = enc_data[:4]
    for i in range(4):
        header[i] = int.from_bytes(header[i], 'little')

    if header == signature[0]:
        dec_data = decode_b0747746(enc_data)
    elif header == signature[1]:
        dec_data = decode_b25a6f00(enc_data)
    elif header == signature[2]:
        dec_data = decode_b2a66dff(enc_data)
    elif header == signature[3]:
        dec_data = decode_f2a32072(enc_data)
    elif header == signature[4]:
        dec_data = decode_b2a46eff(enc_data)
    elif header == signature[5]:
        dec_data = decode_a9a46efe(enc_data)
    elif header == signature[6]:
        dec_data = decode_945fdad8(enc_data)
    elif header == signature[7]:
        dec_data = decode_95a2748e(enc_data)
    elif header == signature[8]:
        dec_data = decode_4da2ee67(enc_data)
    elif header == signature[9]:
        dec_data = decode_8291706f(enc_data)
    elif header == signature[10]:
        dec_data = decode_614a860c(enc_data)
    elif header == signature[11]:
        dec_data = decode_0f7850ba(enc_data)
    elif header == signature[12]:
        dec_data = decode_8291986f(enc_data)
    elif header == signature[13]:
        dec_data = decode_2333f765(enc_data)
    else:
        print('[!] Error: Unknown Format')
        sys.exit(-1)

    print('[!] Complete!')

    with open(args[2], 'wb') as f:
        f.write(bytearray(dec_data))

if __name__ == '__main__':
    main()
