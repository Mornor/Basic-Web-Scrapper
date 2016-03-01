import requests
from bs4 import BeautifulSoup

# Constants
request_url = "http://www.boldsystems.org/index.php/Public_Ajax_RecordList?offset=0&limit=500&query="

searched_terms = ["Hydrobia ventrosa"]

# Input read fropm file
input = []
output = []


def replace_white_spaces(word):
    if ' ' in word:
        return word
    return word.replace(" ", "%20")


def load_input():
    with open("liste.txt", "r") as ins:
        for line in ins:
            input.append(line[:8])
    #print(input)
    return input


def fetch_output():
    results = []
    r = requests.post(request_url + replace_white_spaces(searched_terms[0])).text
    soup = BeautifulSoup(r, 'html.parser')
    i = 0
    for span in soup.find_all('span', text='Identifiers:'):
        output.append(span.nextSibling.lstrip()[:8])
        i += 1
    #print(output)
    return output


# load_input()
# fetch_output()

results = list(set(load_input()) - set(fetch_output()))
print(results)
print(len(results))
