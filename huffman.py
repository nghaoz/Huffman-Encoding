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
    print(f'original string: {str_}')

    # extract distinct character and count bit length
    distinctChar, bit_length = distinct_character(str_)
    print(f'distinct character {len(distinctChar)}: {distinctChar} \nbit need: {bit_length}')
    
    huffman_string = ''
    for item in str_:
        huffman_string += generatecode(distinctChar.index(item), bit_length)
    print(f'encoded string: {huffman_string} \n')

    print(f'output')

    file = 'huff.bin'
    sendBinaryData(file, huffman_string)
    print(f'{os.path.basename(file)} {os.path.getsize(file)} byte')

    keys_string =''
    for item in distinctChar:
        keys_string += item
    file = 'keys.json'
    with open(file, 'w') as f:
        json.dump(keys_string+str(bit_length), f)
    print(f'{os.path.basename(file)} {os.path.getsize(file)} byte \n')

    print(f'huffman done with {timeit.default_timer() - start_time}s\n')

# end huffman

#dehuffman
def dehuffman(binFile, keyFile):
        start_time = timeit.default_timer()

        import bitarray
        binaryFromFile = bitarray.bitarray()
        with open(binFile, 'rb') as f:
            binaryFromFile.fromfile(f)

        
        binaryFromFile = str(binaryFromFile)[10:-2]


        with open(keyFile, 'r') as f:
            keys = json.load(f)

        bit_length = int(keys[-1])
        str_ = ''
        for item in range(0, len(binaryFromFile)-(bit_length), bit_length):
            str_ += keys[int(binaryFromFile[item:item+bit_length],2)]
        str_ = str_.replace("'", '"')

        str_ = json.loads(str_)

        print(f'original string: {str_}')

        file = 'original_js.json'
        with open(file, 'w') as f:
            json.dump(str_, f)

        print(f'decode done with {timeit.default_timer()-start_time}s')        
# end dehuffman

def main():
    huffman('sample_js.json')
    dehuffman('huff.bin', 'keys.json')

if __name__ == '__main__':
    main()
