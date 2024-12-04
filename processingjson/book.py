from json import load

f=open("C:\\Users\\anush\\OneDrive\\Desktop\\pythonworks\\json\\book.json")

data=load(f)


# print all title

all_title=[book.get("title") for book in data]

# print(all_title)

# print book with page < 250

filter_page=[book.get("title") for book in data if book.get("pages")<250 ]

# print(filter_page)

# print all genres and not print repeated genre

all_genres=[book.get("genre") for book in data ]

# print(set(all_genres))

# print count of all genre

genre_count={genre:all_genres.count(genre) for genre in all_genres}

# print(genre_count)

# print costly book

costly_book=max(data,key=lambda d:d.get("price"))

# print(costly_book)

# print all authors

all_authors=[book.get("author") for book in data]

author_count={auth:all_authors.count(auth) for auth in all_authors}

print(author_count)

