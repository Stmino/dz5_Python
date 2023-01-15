#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def encode(data):
    rle_encode= ''
    last_char= ''
    count=1
    for char in data:
        if char !=last_char:
            if last_char:
                rle_encode +=str(count) + last_char
            count=1
            last_char=char
        else:
            count+=1
    else:
        rle_encode+=str(count) + last_char
        return rle_encode

def decode(data):
    rle_decode= ''
    count = ''
    for char in data:
        if char.isdigit():
            count+=char 
        else:
            rle_decode+=char*int(count)
            count= ''
    return rle_decode

encoded = encode('111112222334445888')
print(encoded)   
decoded= decode('6A1F2D7C1A17E17t') 
print(decoded)



