country_code={"India":"+91",
              "Pakistan":"+92",
              "Nepal":"+977",
              "Japan":"+81"
} 
print("Country code for India")
print(country_code.get("India","notfound"))
print("Country code for China")
print(country_code.get("Chhina","notfound"))
print("Country code for Nepal")
print(country_code.get("Nepal","notfound"))