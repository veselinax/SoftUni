import re
text = input()
# Regex pattern with numbered capturing groups
pattern = r"\b(\d{2})([./-])([A-Z][a-z]{2})\2(\d{4})\b"
matches = re.findall(pattern, text)
# Each match has a tuple of all the matches (day, separator, month, year)
# print(matches) -> [('13', '/', 'Jul', '1928'), ('10', '-', 'Nov', '1934'), ('25', '.', 'Dec', '1937')]
for match in matches:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")
