# TODO Найдите количество книг, которое можно разместить на дискете
value_discet_MB = 1.44
value_discet_bytes = value_discet_MB * 1024 * 1024
lists = 100
strok_in_lists = 50
symbols = 25
one_symbol_byte = 4

one_book = (((symbols * one_symbol_byte) * strok_in_lists) * lists)

disk_books = value_discet_bytes // one_book

# print("1 книга в байтах:", one_book)
# print("Байт в дискете:", value_discet_bytes)
print("Количество книг, помещающихся на дискету:", round(disk_books))
