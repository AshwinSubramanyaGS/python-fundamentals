import re

# 1. Email validation
email_pat = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
print(bool(re.fullmatch(email_pat, "dev.team@company.kar.nic.in"))) 