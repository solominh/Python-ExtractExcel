import bs4
import requests


def find_downloadurl_in(url):
    res = requests.get(url)
    try:
        res.raise_for_status()
    except:
        return None

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    css_selector = '#post-body-318540220416044168 > a'
    elements = soup.select(css_selector)
    if not elements:
        return None

    a_element = elements[0]
    url = a_element['href']
    return url


def download_file_from_url(url, savepath):
    res = requests.get(url)
    try:
        res.raise_for_status()
    except:
        return False

    with open(savepath, 'wb') as f:
        f.write(res.content)
    return True
