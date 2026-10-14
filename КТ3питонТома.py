import csv
from functools import partial
from typing import List, Tuple, Any


def get_books(filename: str) -> List[List[Any]]:
    
    with open(filename, encoding='utf-8') as f:
        
        lines = f.readlines()[1:]
    
    def parse_row(row: str) -> List[Any]:
        parts = [x.strip() for x in row.strip().split('|')]
        return [
            parts[0],                    
            parts[1],                    
            parts[2],                    
            int(parts[3]),               
            float(parts[4])              
        ]
    
    return list(map(parse_row, lines))


def filtered_books(books: List[List[Any]], substring: str) -> List[List[Any]]:
    
    substring = substring.lower()
    
    def matches(book: List[Any]) -> bool:
        return substring in book[1].lower()
    
    def transform(book: List[Any]) -> List[Any]:
        isbn, title, author, qty, price = book
        return [isbn, f"{title}, {author}", qty, price]
    
    return list(
        map(transform,
            filter(matches, books))
    )


def calculate_totals(books: List[List[Any]]) -> List[Tuple[str, float]]:
  
    def to_tuple(book: List[Any]) -> Tuple[str, float]:
        return (book[0], book[2] * book[3])   
    
    return list(map(to_tuple, books))




if __name__ == "__main__":
    books = get_books("books.csv")
    print("Все книги:")
    for b in books:
        print(b)
    
    print("\nФильтр по 'python':")
    python_books = filtered_books(books, "python")
    for b in python_books:
        print(b)
    
    print("\nИтоговая стоимость по книгам:")
    totals = calculate_totals(python_books)   
    for t in totals:
        print(t)