zipcode = []
country_codes = ['us', 'ca', 'mx', 'fr', 'ru']
zipcodes = {90003: 'Los Angeles', 90802: 'Long Beach',\
    91501: 'Burbank', 92101: 'San Diego',92139:'San Diego',\
    90071:'Los Angeles'}
for code in zipcodes.keys():
    zipcode.append(code)
print(f'ZipCodes-> {zipcode}')

mapped_countries = map(country_codes, zipcodes.keys())
print((mapped_countries))

generator_zipcode = (zc for zc in zipcodes.keys())
print(generator_zipcode)
for code in generator_zipcode:
    print(code)
