travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇



def add_new_country(country, visits, cities):
    # Create a decoy list to be added
    new_country_log = [
    {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
    }
    ]

    new_country_log[0]["country"] = country
    new_country_log[0]["visits"] = visits
    new_country_log[0]["cities"] = cities
    
    travel_log.append(new_country_log)

   
add_new_country("Russia",2,["Moscow", "Saint Petersburg"])

add_new_country("Vietnam",3,["Saigon", "Hanoi"])


print(travel_log)

print(len(travel_log))

