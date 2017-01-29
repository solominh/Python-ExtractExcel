import bs4
import requests


def find_downloadurl_in_(url):
    res = requests.get(url)
    try:
        res.raise_for_status()
    except:
        return False

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    css_selector = '#center-content > div.box-ketqua > div > table > tr:nth-of-type(11) > td:nth-of-type(2) > em'
    elements = soup.select(css_selector)
    return elements[0].text.strip()


def download_file_from_url(url, savepath):
    res = requests.get(url)
    try:
        res.raise_for_status()
    except:
        return False

    with open(savepath, 'w') as f:
        f.write(res.content)
    return True
