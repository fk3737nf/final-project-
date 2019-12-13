from  PIL import Image, ImageDraw, ImageFont



image = Image.open('christine-siracusa-vzX2rgUbQXM-unsplash.jpg')    # this where you put the picture you want to to resize the image

image.thumbnail((800, 800))                  # k puting image.thumball an double (())resixing image to 800 800
image.save('christine_thumbnail.jpeg')         # saves the image as christine_thumbnail.jpeg



font = ImageFont.truetype('DejaVuSans (1).ttf', 40)     # i downdloaded DejaVusans from the website and insert it and use font= imagefont.true type to and 40 text draw the test around the taco image

# image font type, 40     to resize my picture u can use any number i just choose your font size

draw = ImageDraw.Draw(image)        # this will draw the image if u don't have it. it won't. draw= imageDraw.Draw(image)





# image font tyme, 40



draw.text([10, 475],' Random Taco Cookbook', fill='red', font=font)     # drawing text and putting 10 47 Rondom taco cookbook and it will appear on the picture.


image.show()
image.save('christine-siracusa-vzX2rgUbQXM-unsplash.jpg')           # using .save('saveing my picture)   this allows you to save your picture after u finish


 