from bs4 import BeautifulSoup
import requests

def get_text(tag):
    if not tag:
        return ''

    return tag.get_text(strip=True)

rs = requests.get('https://www.net.kg/?pp=600&main_cat=&cat=&old_sort=&orient=&sort=&scroll=1')
root = BeautifulSoup(rs.content, 'html.parser')

table = root.select_one('#main_block > table:nth-child(27)')

items = []

for tr in table.select('tr'):
    td_list = tr.select('td')
    if not td_list:
        continue

    pos, _, site, kg_hits, hits, visitors, hosts, _ = td_list
    if not site.a.has_attr('title'):
        continue

    items.append(
        (get_text(pos), site.a['title'], get_text(kg_hits),
         get_text(hits), get_text(visitors), get_text(hosts))
    )
print(items,'\t')

with open("Stat.txt", "w") as file:
    print(*items, file=file)
