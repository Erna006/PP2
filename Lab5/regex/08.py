import re

text = "HelloWorldHowAreYou"
spl = re.findall(r'[A-Z][^A-Z]*', text)
print(spl)