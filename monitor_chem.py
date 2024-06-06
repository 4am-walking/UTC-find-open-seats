import requests

pilotURL = "https://sis-reg.utc.edu:443/StudentRegistrationSsb/ssb/term/search?mode=search"
jsonURL = "https://sis-reg.utc.edu:443/StudentRegistrationSsb/ssb/searchResults/searchResults?txt_courseNumber=1120&txt_keywordlike=General%2520Chemistry%2520II&txt_term=202440&startDatepicker=&endDatepicker=&pageOffset=0&pageMaxSize=10&sortColumn=subjectDescription&sortDirection=asc"

session = requests.session()
session.get(pilotURL)

pilotData = {
    "term": "202440", 
}

requests.post(pilotURL, headers=session.headers, cookies=session.cookies, data=pilotData)
jsonResponse = requests.get(jsonURL, headers=session.headers, cookies=session.cookies).json()

try:
    for i in range(2):
        data = jsonResponse["data"][i]
        print(f"Seats available: {data['seatsAvailable']}")
except:
    print(jsonResponse)
