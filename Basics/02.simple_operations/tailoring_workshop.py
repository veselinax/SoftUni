squared_tables_count = int(input())
d_squared_tables_meters = float(input())
s_squared_tables_meters = float(input())
care_tables_count = squared_tables_count
a_cover = d_squared_tables_meters + 0.3 + 0.3  # 0.3 + 0.3 za vseki rub (stranata a ima 2 ruba)
b_cover = s_squared_tables_meters + 0.3 + 0.3  # 30cm / 100= 0.3m
area_cover = squared_tables_count * a_cover * b_cover
a_care = d_squared_tables_meters / 2
area_care = care_tables_count * a_care * a_care
usd_cover = area_cover * 7
usd_care = area_care * 9
usd_total = usd_cover + usd_care
print(f"{usd_total:.2f} USD")
bg_total = usd_total * 1.85
print(f"{bg_total:.2f} BGN")
