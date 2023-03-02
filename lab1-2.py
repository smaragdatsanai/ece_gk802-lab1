import requests # εισαγωγή της βιβλιοθήκης
import datetime 

url = str(input()) # προσδιορισμός του url

with requests.get(url) as response: # το αντικείμενο response
    headers = response.headers

    print("HTTP headers:")
    for header, value in headers.items():
        print(f"{header}: {value}")
print("\n\n\n")
with requests.get(url) as response: # το αντικείμενο response

    server_os = response.headers.get("server")
    
    print("Tο λογισμικό που χρησιμοποιεί ο web server για να απαντήσει στο αίτημα:",server_os)
    cookies = response.cookies
    count=len(cookies)
    if count == 0:print("ΔΕΝ ΧΡΗΣΙΜΟΠΟΙΟΥΝΤΑΙ COOKIES")
    else:
        print("ΧΡΗΣΙΜΟΠΟΙΟΥΝΤΑΙ COOKIES \nΤα cookies αυτά είναι:")
        for cookie in cookies:
            print('Cookie name:', cookie.name)
            #πόσο διάστημα θα είναι έγκυρο
            cookie_expiry_date = datetime.datetime.fromtimestamp(int(cookie.expires))#μετατροπή απο timestamp σε datetime ωστε να κανω σύγκριση
            expiration_duration = cookie_expiry_date - datetime.datetime.now()
            print('Expiration duration in seconds:', expiration_duration.total_seconds())#διάρκεια σε δευτερόλεπτα
            print('Expiration duration in days:', expiration_duration.days,end="\n\n")#διάρκεια σε μέρες
    

        
        
