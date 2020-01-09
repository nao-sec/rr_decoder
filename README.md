
# rr_decoder
This script is to decode `Royal Road RTF Weaponizer` 8.t object

The encodings that can be decoded are:
- B0 74 77 46
- B2 5A 6F 00
- B2 A4 6E FF
- B2 A6 6D FF
- F2 A3 20 72

## Usage
```
$ python3 rr_decoder [Input] [Output]
```

## Example
```
$ python3 rr_decoder sample/b2a66dff.bin b2a66dff.exe
```

## License
`rr_decoder` is open-sourced software licensed under the [MIT License](LICENSE)

## Change Log
- 2020/01/09 - 0.1.0 - First Commit
