travel_log = [
{
  "country": "France",
  "cities": ["Paris", "Lille", "Dijion"],
  "visits": 12
},
{
  "country": "Germanny",
  "cities": ["Berlin", "Hamburg", "Stuttgart"],
  "visits": 5
}
]


def add_new_country(country, visits, cities):
  new_country = {
    "country": country,
    "cities": cities,
    "visits": visits
    }
  travel_log.append(new_country)


add_new_country("India", 12, ["Delhi", "Kolkata", "Mumbai"])
print(travel_log)
