import re

log = "INFO: System boot\nERROR: Disk full"

# re.match only checks index 0 ("INFO..."), so it fails even with MULTILINE
print("Match function",re.match(r"ERROR", log, flags=re.MULTILINE))   # None

# re.search with MULTILINE recognizes the start of line 2
print("Search function",re.search(r"^ERROR", log, flags=re.MULTILINE))