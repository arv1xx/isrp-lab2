books = [
    {"title": "Мартин Иден", "author": "Джек Лондон"},
    {"title": "1984", "author": "Джордж Оруэлл"}
]

def count_books():
    return f"Всего книг в библиотеке: {len(books)}"

def find_by_author(author):
    return [b for b in books if b["author"] == author]

def delete_book(title):
    global books
    books = [b for b in books if b["title"] != title]