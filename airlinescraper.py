import pandas as pd

# Wikipedia airline list URLs
urls = [
    'https://en.wikipedia.org/wiki/List_of_airlines_of_the_United_States',
    'https://en.wikipedia.org/wiki/List_of_airlines_of_Canada',
    'https://en.wikipedia.org/wiki/List_of_airlines_of_Mexico'
]

icao_codes = set()

for url in urls:
    print(f"Scraping {url} ...")
    try:
        tables = pd.read_html(url)
        for table in tables:
            cols = [c.lower() for c in table.columns]
            if 'icao' in cols or 'icao code' in cols:
                for col in table.columns:
                    if 'icao' in col.lower():
                        codes = table[col].dropna().astype(str).str.strip().str.upper()
                        for code in codes:
                            if code.isalpha() and len(code) == 3:
                                icao_codes.add(code)
    except Exception as e:
        print(f"Failed to read {url}: {e}")

icao_codes_list = sorted(list(icao_codes))

# Output as Python list
print("\n✅ Extracted ICAO codes:")
print(', '.join(icao_codes_list))
print(f"\nTotal: {len(icao_codes_list)} airlines")

# Output as Python variable for app.py
print("\nPaste this into app.py:\n")
print("NA_ICAO_AIRLINES = [")
for code in icao_codes_list:
    print(f"    '{code}',")
print("]")
