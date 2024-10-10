#Python List
University1 = {
  "ID" : 1,
  "Name" : "University of the Philippines",
  "Location" : "Quezon",
  "Established Year" : 1908 ,
  "Type" : "Public",
  "Website" : "www.up.edu.ph"
}
University2 = {
  "ID" : 2,
  "Name" : "Ateneo de Manila University",
  "Location" : "Quezon",
  "Established Year" : 1859,
  "Type" : "Private",
  "Website" : "www.ateneo.edu"
}
University3 = {
  "ID" : 3,
  "Name" : "De La Salle University",
  "Location" : "Manila",
  "Established Year" : 1911,
  "Type" : "Private",
  "Website" : "www.dlsu.edu.ph"
}
University4 = {
  "ID" : 4,
  "Name" : "University of Santo Tomas",
  "Location" : "Manila",
  "Established Year" : 1611,
  "Type" : "Private",
  "Website" : "www.ust.edu.ph"
}
University5 = {
  "ID" : 5,
  "Name" : "Polytechnic University of the Philippines",
  "Location" : "Manila",
  "Established Year" : 1904,
  "Type" : "Public",
  "Website" : "www.pup.edu.ph"
}
Universities = [University1, University2, University3, University4, University5]
for University in Universities:
    print(f"ID: {University.get('ID')}, Name: {University.get('Name')}, Location: {University.get('Location')}, Established Year: {University.get('Established Year')}, Type: {University.get('Type')}, Website: {University.get('Website')}")