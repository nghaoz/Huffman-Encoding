import os
import json
import timeit

# huffman
def distinct_character(str_):
    distinctChar = list(set(str_))

    # calculate bit length
    bit_length = 0
    tmp = len(distinctChar)
    if (tmp == 0): 
        return distinctChar, 0
    else:
        while (tmp > 1):
            bit_length += 1
            tmp = tmp / 2
    # end calculate bit length

    return distinctChar, bit_length or 1

def generatecode(i, maxlength):
    return '{:0{}b}'.format(i, maxlength)   

def sendBinaryData(path, encodedstring):
    from bitstring import BitArray
    file = open(path, 'wb')
    obj = BitArray(bin=encodedstring)
    obj.tofile(file)
    file.close()

def huffman (file):
    start_time = timeit.default_timer()

    # open json file
    print(f'{os.path.basename(file)} {os.path.getsize(file)} byte')
    with open(file, 'r') as File:
        str_ = str(json.load(File))
    # print(str_)

    # extract distinct character and count bit length
    distinctChar, bit_length = distinct_character(str_)
    print(distinctChar)
    print(f'distinct character: {len(distinctChar)} \nbit need: {bit_length}')
    
    huffman_string = ''
    for item in str_:
        for char in range(0, len(distinctChar), 1):
            if item == distinctChar[char]:
                huffman_string += generatecode(char, bit_length)
    print(f'{huffman_string}')

    file = 'huff.bin'
    sendBinaryData(file, huffman_string)
    print(f'{os.path.basename(file)} {os.path.getsize(file)} byte')

    distinctChar_string =''
    for item in distinctChar:
        distinctChar_string += item
    file = 'keys.json'
    with open(file, 'w') as f:
        json.dump(distinctChar_string+str(bit_length), f)
    print(f'{os.path.basename(file)} {os.path.getsize(file)} byte')

    print(f'huffman done with {timeit.default_timer() - start_time}s\n')

# end huffman

#dehuffman
def dehuffman(binFile, keyFile):
        start_time = timeit.default_timer()

        import bitarray
        binaryFromFile = bitarray.bitarray()
        with open(binFile, 'rb') as f:
            binaryFromFile.fromfile(f)
        # print(f'{type(binaryFromFile)}\n{str(binaryFromFile)}')
        
        binaryFromFile = str(binaryFromFile)[10:-2]
        # print(f'{type(binaryFromFile)}\n{str(binaryFromFile)}')

        with open(keyFile, 'r') as f:
            keys = json.load(f)
        # print(f'{keys}')
        # print(f'{keys[1]}')
        bit_length = int(keys[-1])
        str_ = ''
        for item in range(0, len(binaryFromFile)-(1+bit_length), bit_length):
            str_ += keys[int(binaryFromFile[item:item+bit_length],2)]
        str_ = str_.replace("'", '"')
        # print(f'{type(str_)} {str_}')
        str_ = json.loads(str_)
        # print(f'{type(str_)} {str_}')

        file = 'original_js.json'
        with open(file, 'w') as f:
            json.dump(str_, f)

        print(f'decode done with {timeit.default_timer()-start_time}s')        
# end dehuffman

def main():
    huffman('js.json')
    dehuffman('huff.bin', 'keys.json')

if __name__ == '__main__':
    main()




