#loading both files
books <- read.csv("books.csv")
authors <- read.csv("authors.csv")

#locating books with the author name 'Mia Morgan'
books[books$author == "Mia Morgan",]

#locating books with the topic 'music' that released in 1613
filter <- books$topic == "Music" & books$year == 1613
books[filter,]

#locating book for silent traveler from year 1775 with author Lysandra Silverleaf or Elena Petrova
filter <- books$year == 1775 & (books$author == "Lysandra Silverleaf" | books$author == "Elena Petrova")
books[filter,]

#locating art book for the painter either 1990 or 1992, 200-300 pages
filter <- books$topic == "Art" & (books$pages>=200 & books$pages <= 300) & (books$year == 1990 | books$year == 1992)
books[filter,]

#locating book for Scientist
filter <- grepl("Quantum Mechanics", books$title)
books[filter,]

#locating book for Teacher
authors_filter <- authors$hometown == "Zenthia"
potential_authors <- authors[authors_filter,]

filter <- (books$year >= 1700 & books$year <= 1799) & books$topic == "Education" & books$author %in% potential_authors$author
books[filter,]