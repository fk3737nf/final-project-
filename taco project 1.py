from  PIL import Image, ImageDraw, ImageFont

image = Image.open('christine-siracusa-vzX2rgUbQXM-unsplash.jpg')    # this where you put the picture you want to to resize the image

image.thumbnail((800, 800))                  # k puting image.thumball an double (())resixing image to 800 800
image.save('christine_thumbnail.jpeg')         # saves the image as christine_thumbnail.jpeg

