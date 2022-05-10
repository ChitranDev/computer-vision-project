import string    
import random # define the random module  
S = 10  # number of characters in the string.  
# call random.choices() string module to find the string in Uppercase + numeric data.  
ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    
print("The randomly generated string is : " + str(ran)) # print the random data  

# Import the following modules
from captcha.image import ImageCaptcha

# Create an image instance of the given size
image = ImageCaptcha(width = 280, height = 90)

# Image captcha text
captcha_text = str(ran)

# generate the image of the given text
data = image.generate(captcha_text)

# write the image on the given file and save it
image.write(captcha_text, 'CAPTCHA.png')

input_c = input("enter the captcha code: ")
if input_c == str(ran):
    print("submitting form...")
else:
    print("sorry you are not real person !")
