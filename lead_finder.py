import requests
from bs4 import BeautifulSoup

def find_leads(url):

    response = requests.get(url, verify=False)

    soup = BeautifulSoup(response.text, "html.parser")

    leads = []

    for link in soup.find_all("a"):
        name = link.text.strip()

        if name:
            leads.append(name)

    return leads