### Step 1 - Lists ###

# Fill in this list with several authors you are a fan of. At least 7 or 8 should do.
my_authors = []

# Now let's add a new author to the end with the .append() method. Type your code below.

# Code here
my_authors.append('David Shannon')
my_authors.append('Evan Schellous')
my_authors.append('Ben Dickamore')
my_authors.append('Karli Kallas')
my_authors.append('Bridger Alishouse')
my_authors.append('Nick Kreipl')
my_authors.append('Parker Freestone')

# Example: my_authors.append("H.G. Wells")


# Now let's remove an element in the list

# Code here
my_authors.remove('David Shannon')
# Example: my_authors.remove("H.G. Wells")


# Now access an element by it's index. (Remember it indexes start at 0.)

# Code here
my_authors[5]
# Example: my_authors[2]


# Now slice the list.

# Code here
my_authors[0:3]
# Example: my_authors[1:4]


### Step 2 - Tuples ###

# Create your tuple below. Assign it to a variable name you can reference later in the exercise.

# Code here
my_author_tuple = ('cam', 'nick', 'parker', 'bridge')
# Example: my_author_tuple = ("F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury")


### Step 3 - Sets ###

# Create a set with your authors.

# Code here
my_authors_set = {'cam', 'nick', 'parker', 'bridge'}
# Example: my_author_set = {"F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury"}


# Add a new author to your set.

# Code here
my_authors_set.add('kar')
# Example: my_author_set.add("J.R.R. Tolkien")


# Try adding the same author again, and be sure to print your set.

# Code here
my_authors_set.add('kar')
# Example: my_author_set.add("J.R.R. Tolkien")



### Step 4 - For Loops ###

# Create a for-loop for each of the data-structures above.

# Code here
# Example:
def printingthang():
    for people in my_authors:
        print(people)
    
    for authors in my_author_tuple:
        print(authors)
    
    for skiing in my_authors_set:
        print(skiing)

# for book in my_authors:
    # print(book)

# for book in my_authors_tuple:
    # print(book)

# for book in my_authors_set:
    # print(book)

def testing():
    print('thatch')