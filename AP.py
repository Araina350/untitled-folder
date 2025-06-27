class INDIA:
    def capital(self):
        print("NEW DELHI IS THE CAPITAL OF INDIA")
    def language(self):
        print("INDIA HAS MANY LANGUAGES BUT HINDI AND ENGLISH ARE THE MOST COMMONLY SPOKEN LANGUAGES.") 
    def tc(self):
        print("INDIA IS A DEVELOPING COUNTRY") 
class USA:
    def capital(self):
        print("WASHINGTON D.C. IS THE CAPITAL OF USA")
    def language(self):
        print("IN THE U.S.A.  ENGLISH ISE THE MOST COMMONLY SPOKEN LANGUAGE.") 
    def tc(self):
        print("U.S.A. IS A DEVELOPED COUNTRY") 
obi=INDIA()
obii=USA()
for country in(obi,obii):
    country.capital()
    country.language()
    country.tc()