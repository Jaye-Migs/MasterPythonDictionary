#Python Dictionary
Product1 = {
  "ID" : 1,
  "Name" : "Laptop",
  "Category" : "Electronics",
  "Price" : 750,
  "Stock" : 50,
  "Supplier Email" : "supplier1@gmail.com"
}
Product2 = {
  "ID" : 2,
  "Name" : "Desk Chair",
  "Category" : "Furniture",
  "Price" : 100,
  "Stock" : 200,
  "Supplier Email" : "supplier2@gmail.com"
}
Product3 = {
  "ID" : 3,
  "Name" : "Smartwatch",
  "Category" : "Electronics",
  "Price" : 200,
  "Stock" : 150,
  "Supplier Email" : "supplier3@gmail.com"
}
Product4 = {
  "ID" : 4,
  "Name" : "Notebook",
  "Category" : "Stationery",
  "Price" : 5,
  "Stock" : 500,
  "Supplier Email" : "supplier4@gmail.com"
}
Product5 = {
  "ID" : 5,
  "Name" : "Running Shoes",
  "Category" : "Apparel",
  "Price" : 80,
  "Stock" : 100,
  "Supplier Email" : "supplier5@gmail.com"
}
Products = [Product1, Product2, Product3, Product4, Product5]
for Product in Products:
    print(f"ID: {Product.get('ID')}, Name: {Product.get('Name')}, Category: {Product.get('Category')}, Price: {Product.get('Price')}, Stock: {Product.get('Stock')}, Supplier Email: {Product.get('Supplier Email')}")