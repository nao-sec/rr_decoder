
# rr_decoder
This script is to decode `Royal Road RTF Weaponizer` 8.t object

The encodings that can be decoded are:
- 4D A2 EE 67
- 61 4A 86 0C
- 82 91 70 6F
- 94 5F DA D8
- 95 A2 74 8E
- A9 A4 6E FE
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
- 2024/01/04 - 0.1.7 - Add decode_614a860c
- 2022/01/24 - 0.1.6 - Add decode_8291706f
- 2021/05/21 - 0.1.5 - Add decode_4da2ee67
- 2021/03/30 - 0.1.4 - Add decode_95a2748e
- 2020/10/28 - 0.1.3 - Add decode_945fdad8
- 2020/10/14 - 0.1.2 - Add decode_a9a46efe
- 2020/03/29 - 0.1.1 - Refactoring decode_b0747746 & decode_f2a32072
- 2020/01/09 - 0.1.0 - First Commit
