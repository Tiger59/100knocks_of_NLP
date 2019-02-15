import gzip,json

def search_country_data(country):
    for line in gzip.open('../data/jawiki-country.json.gz', 'rt', encoding='utf-8'):
        json_data = json.loads(line)
        if json_data['title'] == country:
            return json_data['text']

def open_england():
    return open('england', encoding='utf-8')

england = search_country_data('イギリス')
with open('england', 'w', encoding='utf-8') as f:
    f.write(str(england))
print(england)