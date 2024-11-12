"""
Creates to analyzed and decrypt URL

The links hav next structure:

https://[root_host].[disponsable_url]/[A-Z]8/?u=[_usr]&o=[_oauth]&f=1&sid=[tX~[TOKEN]]&fp=[TOKEN]%3D%3D
"""
from fpGenerator import generate_random_fp
import urllib.parse
import base64
import json


_dataLinks = "" # Previuos information of all links
_root_host = []
_disponsable_url = []
_main_8_AZ = []
_main_tokens = {}

try:
    with open("zelda.txt", "r", encoding="UTF-8") as f:
        _dataLinks = f.read()
except:
    pass


# Update _root_host
def updateInfoRootHost(url):
    d = url.split(".")[0]
    d = d.replace("https://", "")

    if d not in _root_host:
        _root_host.append(d)


# Update _disponsable_url
def updateInfoDisponsableURL(url):
    d = url.split("?u=")[0]
    d = d.replace("https://", "")
    d = d.split("/")[0]
    d = d.split(".")
    d = f"{d[1]}.{d[2]}"

    if d not in _disponsable_url:
        _disponsable_url.append(d)


def updatetInfoMain8Pattern(url):
    d = url.split(".live/")[1]
    d = d.split("/")[0]

    if d not in _main_8_AZ:
        _main_8_AZ.append(d)
    else:
        pass
        #print(f"Duplicated TOKEN: {d}")

def updateMainTokens(arrUrls):
    # Fill dic
    for i in _main_8_AZ:
        _main_tokens[i] = {}

    # Fill credentials info
    for itter8Token in _main_tokens:
        for itterURL in arrUrls.split("\n"):
            if str(itterURL).strip() != "":
                if itter8Token in itterURL:
                    # GET sid
                    sid = itterURL.split("&sid=")[1]
                    sid = sid.split("&fp=")[0]
                    # Save
                    _main_tokens[itter8Token]["sid"] = sid
                    
                    # GET fp
                    fp = itterURL.split("&fp=")[1]
                    # Save
                    _main_tokens[itter8Token]["fp"] = fp

    # Save JSON
    with open('urlTokens.json', 'w', encoding="UTF-8") as archivo:
        json.dump(_main_tokens, archivo)

    
if _dataLinks != "":
    for i in _dataLinks.split("\n"):
        if str(i).strip() != "":
            updateInfoRootHost(i)
            updateInfoDisponsableURL(i)
            updatetInfoMain8Pattern(i)
    updateMainTokens(_dataLinks)


print("============STATITICS================")
print(f"ROOT_HOST: {len(_root_host)}")
print(f"DISPONSABLE_URL: {len(_disponsable_url)}")
print(f"MAIN 8 TOKENS: {len(_main_8_AZ)}")



# def decode_base64(encoded_str):
#     try:
#         # Decodificar Base64
#         decoded_bytes = base64.b64decode(encoded_str)
#         # Decodificar a cadena de texto (si es texto)
#         return decoded_bytes.decode('utf-8', errors='ignore')
#     except Exception as e:
#         return f"Decoding failed: {e}"
    

# for i in _main_tokens:
#     fp = _main_tokens[i]["fp"]
#     #print(f"&fp: {fp}, len: {len(fp)}")
#     decoded_fp = urllib.parse.unquote(fp)
#     decoded_content = decode_base64(decoded_fp)
#     print(f"ORIGINAL: {i} : Decrypt: {decoded_fp} : Base64: {decoded_content}")


# Try to generate random fp to mach with zelda.txt info
_counter = 0
for _ in range(10000000):
    _rndFP = generate_random_fp()
    _found = False
    for i in _main_tokens:
        if _rndFP == _main_tokens[i]["fp"]:
            print(f"ENCONTRADO: &fp:{_main_tokens[i]["fp"]} >> RNDFP: {_rndFP}")
            _found = True
            break
        _counter = _counter + 1

    if _found:
        print(f"Encontrado FP: {_rndFP}")
        break
    else:
        print(f"Inteto: {_counter} rndFP: {_rndFP}")
