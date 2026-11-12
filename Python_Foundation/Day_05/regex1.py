import re

text = "Employee ID: EMP-1022"

pattern = r"EMP-\d{4}"

result = re.search(pattern, text)

if result:
    print("Found:", result.group())
else:
    print("Pattern not found")