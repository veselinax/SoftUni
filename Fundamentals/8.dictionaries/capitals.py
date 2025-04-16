countries = input().split(", ")
capitals = input().split(", ")

country_capital_dict = {}
for country, capital in zip(countries, capitals):  # zip pairs each country with its corresponding capital
    country_capital_dict[country] = capital

#using comprehension
#country_capital_dict = {country: capital for country, capital in zip(countries, capitals)}

for country, capital in country_capital_dict.items():
    print(f"{country} -> {capital}")
