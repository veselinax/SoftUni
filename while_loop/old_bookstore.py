searched_book = input()
total_books = int(input())

looked_books = 0
book_found = False

while looked_books < total_books:
    book_name = input()
    if book_name == searched_book:
        book_found = True
        break
    looked_books += 1

if not book_found:
    print("The book you search is not here!")
    print(f"You checked {looked_books} books.")
else:
    print(f"You checked {looked_books} books and found it.")
