my_book = {
    "title": "Then Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

this_book = {
    "title": "No, David!",
    "author": "David Shannon",
    "year": 1998,
    "rating": 4.45,
    "pages": 32
}

that_book = {
    "title": "The Cat In The Hat",
    "author": "Dr Seuss",
    "year": 1957,
    "rating": 4.22,
    "pages": 61
}

titles = [my_book, this_book, that_book]

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below
def book_info(book):
    book_string = f" Title: {book['title']} \n Author: {book['author']} \n Year: {book['year']} \n Rating: {book['rating']} \n Pages: {book['pages']}"
    return book_string
#print(book_info(my_book))

# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below

def book_title(book):
    return book['title']
      
def book_author(book):
    return book['author']
     
def book_year(book):
    return book['year']
     
    
def book_rating(book):
    return book['rating']
       
def book_pages(book):
    return book['pages']
      
def all_authors(arr):
    for book in arr:
        print(book['author'])

#all_authors(titles)
        
def total_pages(arr):
    total = 0
    for book in arr:
        total += book['pages']
    
    return total

#print(total_pages(titles))

# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below
def title_search(book):
    if "title" in book:
        book_string = f"{book['title']} is here\n{book_info(book)}"
        return book_string
    else:
        return "That title is not here." 
    
#print(title_search(my_book))


def longest_book(titles):
    book_length = []
    for book in titles:
         book_length.append(book['pages'])
    book_length.sort()
    return f'longest book is {book_length[-1]} pages long '


print(longest_book(titles))

def all_titles(arr):
    for book in arr:
        print(book['title'])

#all_titles(titles)