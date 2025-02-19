import re

def check(s):
    pattern = r"[A-Z][a-z]+"
    # res = re.match(pattern, s)
    # print(res)
    if re.search(pattern, s):
        return True
    else:
        return False

test_strings = ["arbhlwfge_dfknvser", "awduibdcvA_sjrb", "auierf_Auierv", "Ayvjkasdc_Aiufv", "uerbher9_ae4rgas", "erfaer"]

for s in test_strings:
    print(f"'{s}': {check(s)}")