from models.author import Author
from models.book import Book

import repos.book_repo as book_repo
import repos.author_repo as author_repo

book_repo.delete_all()
author_repo.delete_all()

author1 = Author("Junji Ito")
author_repo.create(author1)
author2 = Author("William Gibson")
author_repo.create(author2)
author3 = Author("Juno Dawson")
author_repo.create(author3)

author_repo.select_all()

book1 = Book("Uzumaki", author1, 12.99)
book_repo.create(book1)
book2 = Book("Neuromancer", author2, 8.99)
book_repo.create(book2)
book3 = Book("Gender Games", author3, 9.99)
book_repo.create(book3)

