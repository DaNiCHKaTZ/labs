import struct
def bytearay(file_path):
    with open(file_path, 'rb') as file:
        byte_array = []
        byte = file.read(1)
        while byte:
            byte_array.append(byte[0])
            byte = file.read(1)
    
    return byte_array
def read_bmp(file_path):
    with open(file_path, 'rb') as file:
        header = file.read(54)
        width = struct.unpack('<i', header[18:22])[0]
        height = struct.unpack('<i', header[22:26])[0]
        
        file.seek(54)
        pixels = file.read()
def encode_rle(data):
    encoded_data = bytearray()
    count = 1
    prev_byte = data[0]

    for byte in data[1:]:
        if byte == prev_byte:
            count += 1
        else:
            encoded_data.extend([count, prev_byte])
            prev_byte = byte
            count = 1
    encoded_data.extend([count, prev_byte])
    return encoded_data
def decode_rle(encoded_data):
    decoded_data = bytearray()
    i = 0
    while i < len(encoded_data):
        count = encoded_data[i]
        byte = encoded_data[i + 1]
        decoded_data.extend([byte] * count)
        i += 2
    return decoded_data
with open('example.bmp', 'rb') as file:
    bmp_data = bytearray(file.read())
encoded_data = encode_rle(bmp_data)
decoded_data = decode_rle(encoded_data)
print("Исходные данные:")
print(bmp_data)
print("\nЗакодированные данные:")
print(encoded_data)
print("\nДекодированные данные:")
print(decoded_data)
