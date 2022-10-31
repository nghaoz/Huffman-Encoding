# Huffman-Encoding-Json

This method is built to compress the content of JSON files. Base on the Huffman encoding method but has a few differences. 
We will slightly go through each step to understand the differences.

Content of JSON file:

```json
{
    "MaBN": "08092003",
    "TenBN": "NGUYEN HOANG LE PHUONG",
    "Ngaysinh": "20120101",
    "Ngaychup": "20200908",
    "IDmay": "(6444)",
    "Eye": "OD",
    "S": 22,
    "N": 54,
    "T": 28,
    "I": 30,
    "xC": 21.200049152125832,
    "yC": 7.999970078021559,
    "hC": 0.133681,
    "wC": 0.065104,
    "xD": 8.227269818181817,
    "yD": 4.837219478652248,
    "hD": 0.223958,
    "wD": 0.171875,
    "Resolution": [
        768,
        576
    ]
}
```

The JSON file contains patient information in the form of a string of characters, after reading the data from the file, we will extract the different characters that appear inside the file into a string . This string is called the string key.

String key:

```json
"gHE5AN6xao1I8.sBywL03(C7]Mh{Un:uTi9l2GDp S4PceR}[YO,)'tm6"
```








