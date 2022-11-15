# Huffman Encoding for Json files

> This method is built to compress the content of JSON files. Base on the Huffman encoding method but has a few differences. 

## Explanation:

Content of JSON file:

```json
{
    "ID": "ID1234",
    "NAME": "name",
    "NUMBER": 21.200049152125832
}

```

The JSON file contains information in the form of a string of characters, after reading the data from the file, extract the different characters that appear inside the file into a string . This string is called the string key.

String key:

```python
string_key = "gHE5AN6xao1I8.sBywL03(C7]Mh{Un:uTi9l2GDp S4PceR}[YO,)'tm6"
```

Huffman code is generated by the index of the character in the string key, last character is the length of each Huffman code.

```python
huffman_code_of _letter_g = '{:0{}b}'.format(string_key.index('g'), string_key[-1]) == 000000
# string_key[-1] = length of each huffman code = last character = 6
# string_key.index('g') = position of letter 'g' in string key = first letter = 0
```

## Implement:
```python
def main():
    huffman('js.json')
    dehuffman('huff.bin', 'keys.json')
```
- Replace ```sample_js.json``` with your path of JSON to encode.
- This code contained Encoding function. Comment ```dehuffman('huff.bin', 'keys.json')``` if u don't want to use.

## Result:
    
- ```huff.bin``` file to save Huffman encoded string from the input file.  
    
- ```keys.json``` file to store String key. 
    
- ```original_js.json``` file to save the original content of the input file.






