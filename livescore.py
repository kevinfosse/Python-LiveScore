from bs4 import BeautifulSoup
import requests



url = "https://www.matchendirect.fr/live-score/"
result = requests.get(url)
doc = BeautifulSoup(result.text, "lxml")
#print(doc.prettify())
temp = []

matchs = doc.find_all(class_='panel-info')

print("=====================================================================")
for match in matchs:
        for each in match.find_all('tr', class_='sl'):
                for eq1 in each.find_all('span', class_="lm3_eq1"):
                        equipe1 = eq1.text
                for score in each.find_all('span', class_="lm3_score"):
                        score = score.text
                for eq2 in each.find_all('span', class_="lm3_eq2"):
                        equipe2 = eq2.text

                result = equipe1 + " " + score + " " + equipe2
                print(result)
                print("\r\r")
