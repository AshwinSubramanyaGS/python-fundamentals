import re

def validate_date_style(date_str):
    # Strip leading/trailing whitespaces for clean matching
    date_str = date_str.strip()
    
    
    # 1. MM - DD - YYYY
    us_numeric_pattern = r"^\d{1,2}\s*-\s*\d{1,2}\s*-\s*\d{4}$"
    
    # 2. US Month Name with hyphens or slashes
    us_alpha_pattern = r"^\d{1,2}\s*[-/]\s*[A-Za-z]{3}\s*[-/]\s*\d{4}$"
    
    
    # 3. DD-MM-YYYY Indian
    ind_numeric_pattern = r"^\d{1,2}[-/]\d{1,2}[-/]\d{4}$"

    # Match against patterns
    if re.match(us_numeric_pattern, date_str) or re.match(us_alpha_pattern, date_str):
        return "US"
    elif re.match(ind_numeric_pattern, date_str):
        return "Ind"
    else:
        return "Invalid"

# --- Test Cases ---
test_dates = [
    "12 - 20 - 1999",
    "50-Nov-1999",
    "22 /Nov /1999",
    "22-12-2000",
    "22/12/2000",
    "2023-13-45",       # Invalid month/day
    "Invalid-Date"
]

print(f"{'Date String':<20} | {'Detected Style'}")
print("-" * 37)
for d in test_dates:
    print(f"{d:<20} | {validate_date_style(d)}")