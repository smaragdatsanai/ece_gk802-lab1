import requests # εισαγωγή της βιβλιοθήκης

url = str(input()) # προσδιορισμός του url

with requests.get(url) as response: # το αντικείμενο response
    headers = response.headers

    print("HTTP headers:")
    for header, value in headers.items():
        print("{:30s} {}".format(header, value))
