floppy_Mb = 1.44
Mb_to_Kb = 1024
Kb_to_B = 1024
page_n = 100
str_n = 50
symb_n = 25
symb_size_B = 4
floppy_B = floppy_Mb*Mb_to_Kb*Kb_to_B
book_size_ = symb_size_B*symb_n*str_n*page_n
number_of_books_ = floppy_B/book_size_
print("Количество книг, помещающихся на дискету:", int(number_of_books_))
