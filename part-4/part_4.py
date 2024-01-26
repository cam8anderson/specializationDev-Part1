#import sys
#for path in sys.path:
#    print(path)
#exit(0)
### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here
#def book_insert():
#    title = input('Title of the book you want to add? - ')
#    author = input('Author of the book you want to add? - ')
#    year = input('Year of the book you want to add? - ')
#    rating = input('Rating of the book you want to add? - ')
#    pages = input('Pages of the book you want to add? - ')
#    
#    new_book = {
#         'title': title,
#         'author': author,
#         'year': year,
#         'rating': rating,
#         'pages': pages,
#    }
#    return new_book

#print(book_insert())

### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here

#def book_insert():
#    title = input('Title of the book you want to add? - ')
#    author = input('Author of the book you want to add? - ')
#    year = int(input('Year of the book you want to add? - '))
#    rating = float(input('Rating of the book you want to add? - '))
#    pages = int(input('Pages of the book you want to add? - '))
#
#    new_book = {
#         'title': title,
#         'author': author,
#         'year': year,
#         'rating': rating,
#         'pages': pages,
#    }
#    return new_book
#
#print(book_insert())

### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here

def book_insert():
    title = input('Title of the book you want to add? - ')
    author = input('Author of the book you want to add? - ')
    try:
        year = int(input('Year of the book you want to add? - '))
    except:
        year = int(input('Please put a number for the year? - '))
    try:
        rating = float(input('Rating of the book you want to add? - '))
    except:
        rating = float(input('please put in a number for the rating?(ex:4.44) - '))
    try:
        pages = int(input('Pages of the book you want to add? - '))
    except:
        pages = int(input('please put a number for the pages?(ex:444) - '))

    new_book = {
         'title': title,
         'author': author,
         'year': year,
         'rating': rating,
         'pages': pages,
    }
    return new_book

#print(book_insert())

### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here
def main_menu():
    choice = int(input("\nbook insert:1 \nbest rating:2 \npage count:3 \nnewest book:4 \nnames of all books:5 \nexit:6 \n\nwhich number did you pick? - "))
    print(choice)

    if choice == 1:
        new_book = book_insert()

        with open('library.txt', 'a') as f:
        
            f.write(f"{new_book['title']}, {new_book['author']}, {new_book['year']}, {new_book['rating']}, {new_book['pages']}\n")
    elif choice == 2:
        print('best rating')

        with open('library.txt', 'r') as f:
            file = f.readlines()

            rating = []

            for line in file:
                line = line.split(', ')
                rating.append(float(line[3]))

            rating.sort(reverse=True)
            print(f'the best rating is {rating[0]}')
    elif choice == 3:
        print('page count')

        with open('library.txt', 'r') as f:
            file = f.readlines()

            total_pages = 0

            for line in file:
                line = line.split(', ')
                total_pages += int(line[4])
            
            print(f'the total pages is {total_pages}')
    elif choice == 4:
        print('newest book')

        with open('library.txt', 'r') as f:
            file = f.readlines()

            age = []

            for line in file:
                line = line.split(', ')
                age.append(int(line[2]))

            age.sort(reverse=True)
            print(f'newest book is from{age[0]}')

    elif choice == 5:
        print('names of all books')

        with open('library.txt', 'r') as f:
            file = f.readlines()

            names = []

            for line in file:
                line = line.split(', ')
                names.append(line[0])
            print(names)
    elif choice == 6:
        print('exit')
        exit(0)
    else:
        print('you did not put a number available')
    return choice


### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here
def power_button():
    while main_menu() != 6:
        print('works')
