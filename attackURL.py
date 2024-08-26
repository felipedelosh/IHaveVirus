"""
Creates to decrypt URL
"""
import urllib.parse
import base64

values = [
    "Md%2Bb%2FogcsL6hTN%2FIdl07EQ%3D%3D",
    "PgJxGtpSbeXystT1Izv8Cg%3D%3D",
    "6Hsu7We1SMxgE36BjBtYvw%3D%3D",
    "0zNK8x040n85RsPDbQRlbw%3D%3D",
    "J0tGtZLaeppAA9svwVencw%3D%3D",
    "dZgngM70hemNUGuErnKGCA%3D%3D",
    "MlFTGuXKlT25neTD1K7eBA%3D%3D",
    "dZgngM70hemNUGuErnKGCA%3D%3D",
    "MlFTGuXKlT25neTD1K7eBA%3D%3D",
    "F9K88mvr%2FweY1MNhqzmHQg%3D%3D",
    "S9lR09RGUDftIPDo%2FHmcdA%3D%3D",
    "mVqoaLB4bCGWfQIY7ZjJPw%3D%3D",
    "MfvzKxsy%2BUko%2F9RoUAwSCw%3D%3D"
]


def decode_base64(encoded_str):
    try:
        # Decodificar Base64
        decoded_bytes = base64.b64decode(encoded_str)
        # Decodificar a cadena de texto (si es texto)
        return decoded_bytes.decode('utf-8', errors='ignore')
    except Exception as e:
        return f"Decoding failed: {e}"
    
    

for i in values:
    decoded_fp = urllib.parse.unquote(i)
    decoded_content = decode_base64(decoded_fp)
    print(f"ORIGINAL: {i} : Decrypt: {decoded_fp} : Base64: {decoded_content}")
