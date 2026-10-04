books = [
    {"title": "Мартин Иден", "author": "Джек Лондон"},
    {"title": "1984", "author": "Джордж Оруэлл"}
]

def count_books():
    return len(books)

def find_by_author(author):
    return [b for b in books if b["author"] == author]