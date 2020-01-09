import sys

def decode_b0747746(enc_data):
    print('[!] Type [b0747746] is Detected!')
    print('[+] Decoding...')

    dec_data = []
    xor_key = 1219836524

    for i in range(len(enc_data)):
        for c in range(7):
            part1_1 = xor_key >> 26
            part1_2 = xor_key ^ part1_1
            part1_3 = part1_2 >> 3
            part1_4 = xor_key ^ part1_3
            part1_5 = part1_4 & 1
            part2_1 = 2 * xor_key
            part3 = part1_5 | part2_1
            xor_key = part3
            xor_key += 1
        dec_data.append(int.from_bytes(enc_data[i],  "little") ^ (xor_key % 256))
    return dec_data

def decode_b25a6f00(enc_data):
    print('[!] Type [b25a6f00] is Detected!')
    print('[+] Decoding...')

    dec_data = []

    for i in range(len(enc_data)):
        if i % 2 == 0:
            dec_data.append(int.from_bytes(enc_data[i],  "little") ^ 0xff)
        else:
            dec_data.append(int.from_bytes(enc_data[i],  "little"))

    return dec_data

def decode_b2a66dff(enc_data):
    print('[!] Type [b2a66dff] is Detected!')
    print('[+] Decoding...')

    dec_data = []

    for i in range(len(enc_data)):
        dec_data.append(int.from_bytes(enc_data[i],  "little") ^ 0xfc)
    
    dec_data[0] = 0x4d
    dec_data[2] = 0x90

    return dec_data

def decode_f2a32072(enc_data):
    print('[!] Type [f2a32072] is Detected!')
    print('[+] Decoding...')

    dec_data = []
    xor_key = 2079624803

    for i in range(len(enc_data)):
        for c in range(7):
            part1_1 = xor_key >> 27
            part1_2 = xor_key ^ part1_1
            part1_3 = part1_2 >> 3
            part1_4 = xor_key ^ part1_3
            part1_5 = part1_4 & 1
            part2_1 = 2 * xor_key
            part3 = part1_5 | part2_1
            xor_key = part3
        dec_data.append(int.from_bytes(enc_data[i], "little") ^ (xor_key % 256))

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
        [0xf2, 0xa3, 0x20, 0x72]
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
    else:
        print('[!] Error: Unknown Format')
        sys.exit(-1)

    print('[!] Complete!')

    with open(args[2], 'wb') as f:
        f.write(bytearray(dec_data))

if __name__ == '__main__':
    main()
