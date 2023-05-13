import requests
import time
import datetime
from pprint import pprint


if __name__ == "__main__":
    url = "https://api.stackexchange.com/2.3/questions"
    todate = int(time.mktime((datetime.date.today() + datetime.timedelta(days=1)).timetuple()))
    fromdate = datetime.date.today() - datetime.timedelta(days=2)
    params = {
        "max": f"{todate}",
        "min": f"{fromdate}",
        "tagged": "Python",
        "site": "stackoverflow",
        "sort": "creation",
        "order": "asc",
    }
    response = requests.get(url=url, params=params)
    result = response.json()
    questions = []
    for item in result["items"]:
        creation_date = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(float(item["creation_date"])))
        questions += [creation_date, "\n", item["title"], "\n", "\n"]
    with open("questions.txt", "wt", encoding="utf-8") as file:
        file.writelines(questions)
    pprint(result)