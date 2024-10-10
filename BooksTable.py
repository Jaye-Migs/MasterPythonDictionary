#Python List
Book1 = {
  "ID" : 1,
  "Title" : "The Great Gatsby",
  "Author" : "F. Scott Fitzgerald",
  "Genre" : "Fiction",
  "Published Year" : 1925,
  "ISBN" : "978-0743273565",
  "Stock" : 20,
  "Price" : 15.99
}
Book2 = {
  "ID" : 2,
  "Title" : "To Kill a Mockingbird",
  "Author" : "Harper Lee",
  "Genre" : "Fiction",
  "Published Year" : 1960,
  "ISBN" : "978-0060935467",
  "Stock" : 35,
  "Price" : 10.99
}
Book3 = {
  "ID" : 3,
  "Title" : "1984",
  "Author" : "George Orwell",
  "Genre" : "Dystopian",
  "Published Year" : 1949,
  "ISBN" : "978-0451524935",
  "Stock" : 40,
  "Price" : 9.99
}
Book4 = {
  "ID" : 4,
  "Title" : "The Catcher in the Rye",
  "Author" : "J.D. Salinger",
  "Genre" : "Fiction",
  "Published Year" : 1951,
  "ISBN" : "978-0316769488",
  "Stock" : 25,
  "Price" : 8.99
}
Book5 = {
  "ID" : 5,
  "Title" : "A Brief History of Time",
  "Author" : "Stephen Hawking",
  "Genre" : "Non-Fiction",
  "Published Year" : 1988,
  "ISBN" : "978-0553380163",
  "Stock" : 10,
  "Price" : 18.99
}
Books = [Book1, Book2, Book3, Book4, Book5]
for Book in Books:
    print(f"ID: {Book.get('ID')}, Title: {Book.get('Title')}, Author: {Book.get('Author')}, Genre: {Book.get('Genre')}, Published Year: {Book.get('Published Year')}, ISBN: {Book.get('ISBN')}, Stock: {Book.get('Stock')}, Price: {Book.get('Price')}")