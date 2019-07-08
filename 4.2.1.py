import re
string =  'mtMmEZUOmcq'

pattern = '([a-z]+)'
print(re.findall(pattern, string))
