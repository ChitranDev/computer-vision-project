from barcode import EAN13
from barcode.writer import ImageWriter

# you can write any number here
number = '123456781234'
my_code = EAN13(number, writer=ImageWriter())

my_code.save("barcode")