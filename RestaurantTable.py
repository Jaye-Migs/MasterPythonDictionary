#Python List
Resto1 = {
  "ID" : 1,
  "Name" : "Vikings Luxury Buffet",
  "Location" : "Pasay City",
  "Cuisine Type" : "Buffet",
  "Established Year" : 2011,
  "Website" : ""
}
Resto2 = {
  "ID" : 2,
  "Name" : "Antonio\'s Restaurant",
  "Location" : "Tagaytay",
  "Cuisine Type" : "Fine Dining",
  "Established Year" : 2002,
  "Website" : "www.antoniosrestaurant.ph"
}
Resto3 = {
  "ID" : 3,
  "Name" : "Mesa Filipino Moderne",
  "Location" : "Makati City",
  "Cuisine Type" : "Filipino",
  "Established Year" : 2009,
  "Website" : "www.mesa.ph"
}
Resto4 = {
  "ID" : 4,
  "Name" : "Manam Comfort Filipino",
  "Location" : "Quezon City",
  "Cuisine Type" : "Filipino",
  "Established Year" : 2013,
  "Website" : "www.manam.ph"
}
Resto5 = {
  "ID" : 5,
  "Name" : "Ramen Nagi",
  "Location" : "Various Locations",
  "Cuisine Type" : "Japanese",
  "Established Year" : 2013,
  "Website" : "www.ramennagi.com.ph"
}
Restaurant = [Resto1, Resto2, Resto3, Resto4, Resto5]
for Resto in Restaurant:
    print(f"ID: {Resto.get('ID')}, Name: {Resto.get('Name')}, Location: {Resto.get('Location')}, Cuisine Type: {Resto.get('Cuisine Type')}, Established Year: {Resto.get('Established Year')}, Website: {Resto.get('Website')}")