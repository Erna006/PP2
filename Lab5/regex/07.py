import re

text = "decwe_srva_awrfa_vervaer"
pattern = r"_([a-z])"

def repl(match):
    return match.group(1).upper()

result = re.sub(pattern, repl, text)
print(result)