import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_aircraft_type_designators'

# Read all tables on the page
tables = pd.read_html(url)

icao_codes = set()

for table in tables:
    # Look for tables with 'ICAO' or 'Designator' column
    cols = [str(c).lower() for c in table.columns]
    if 'icao' in cols or 'designator' in cols:
        for col in table.columns:
            if 'icao' in str(col).lower() or 'designator' in str(col).lower():
                codes = table[col].dropna().astype(str).str.strip().str.upper()
                for code in codes:
                    if code.isalpha() and 3 <= len(code) <= 4:
                        icao_codes.add(code)

# Sort codes
icao_codes_list = sorted(list(icao_codes))

# Format as Python list
print("\nPaste this into your app.py:\n")
print("ICAO_AIRCRAFT_TYPES = [")
for code in icao_codes_list:
    print(f"    '{code}',")
print("]")
print(f"\nTotal codes: {len(icao_codes_list)}")
