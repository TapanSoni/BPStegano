# BPStegano
```
_______  _______ _______ __
|   _   \|   _   |   _   |  |_.-----.-----.---.-.-----.-----.
|.  1   /|.  1   |   1___|   _|  -__|  _  |  _  |     |  _  |
|.  _   \|.  ____|____   |____|_____|___  |___._|__|__|_____|
|:  1    |:  |   |:  1   |          |_____|
|::.. .  |::.|   |::.. . |
`-------'`---'   `-------'
```

BPStegano is a steganography tool created by students at Rowan University for their graduate cryptography class.

## Features
1) AES-128-CFB encryption of input data
2) Random Least Significant Bit (LSB) pixel encoding
3) Supports plain text (raw string) data
4) Supports encoding of multiple files of any type

## Installation


```bash
git clone https://github.com/TapanSoni/BPStegano

cd BPStegano

pip install -r requirements.txt
```


## Usage

Windows

```python
python stegano.py
```

Linux
```python
python3 stegano.py
```

#### Hiding raw strings inside an image

BPStegano supports raw strings of any length (limited only by the size of the image).

![Hiding raw strings](Demo/plain_text.gif)

#### Hiding files inside an image

BPStegano supports hiding of any type of file and any amount (limited only by the size of the image) inside an image.

![Hiding multiple files](Demo/files.gif)

#### Extracting raw strings from an image

BPStegano extracts the raw string and displays it for you in terminal.

![Extracting raw strings](Demo/extract_plain_text.gif)

#### Extracting files from an image

BPStegano only requires the secret key and the encoded image. It will recognize whether an image is hiding a raw string or files inside it.

![Extracting files](Demo/extract_files.gif)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Disclaimer
This piece of software is provided as is. Neither the authors or Rowan University take any responsibility whatsoever for any action performed by a user of this software, or this software, intentionally or unintentionally.

## Authors
**Tapan Soni** - *Principle Developer* - [TapanSoni](https://github.com/TapanSoni)

**Richard Baird** - *Principle Developer*

**Kriyanshi Patel** - *Developer*
