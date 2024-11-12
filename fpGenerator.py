"""
FelipedelosH
Creates random fp
"""
import base64
import urllib.parse
import os

def generate_random_fp():
    random_bytes = os.urandom(16)
    fp = base64.b64encode(random_bytes).decode('utf-8').rstrip("=") + "=="
    _encoded_fp = urllib.parse.quote(fp)

    return _encoded_fp


for fp in range(100):
    fp = generate_random_fp()
    print(f"&fp: {fp}, len: {len(fp)}")
    