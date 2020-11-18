from bs4 import BeautifulSoup
import urllib.request

def get_links_from_page(url):
    links = set()
    try:
        resp = urllib.request.urlopen(url)
        soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'))
    except:
        return links
    try:
        for link in soup.find_all('a', href=True):
            links.add(link['href'])
    except:
        return links
    return links