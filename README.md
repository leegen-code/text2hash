# text2hash

`text2hash` is a Python script that allows you to compute the hash of a given text using various hashing algorithms. The script provides a user-friendly interface to select the desired hashing algorithm and displays the resulting hash value.

## Features

- Supports multiple hashing algorithms available in the `hashlib` library.
- Displays a banner using the `colorama` library for enhanced terminal output.
- Provides a list of available hashing algorithms for user selection.

## Requirements

- Python 3.x
- `colorama` library

You can install the required library using pip:

```sh
pip install colorama
```

## Usage

1. Clone the repository or download the script to your local machine.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script using Python:

```sh
python main.py
```

4. Enter the text you want to hash when prompted.
5. Choose a hashing algorithm from the displayed list by entering the corresponding number.
6. The script will display the computed hash value of the input text.

## Example

```sh
$ python main.py
```

```
Enter the text you want to hash: hello
Choose hashing algorithm from the following list:
1. blake2b
2. blake2s
3. md5
4. sha1
5. sha224
6. sha256
7. sha3_224
8. sha3_256
9. sha3_384
10. sha3_512
11. shake_128
12. shake_256
13. sm3
Enter the number corresponding to your choice: 6
The sha256 hash of the input is: 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
```

## License

This project is licensed under the MIT License.
```