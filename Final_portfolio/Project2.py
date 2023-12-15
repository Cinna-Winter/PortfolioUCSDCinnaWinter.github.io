
from PIL import Image

#Programs that open and mirror the image.

def open_image():
  img = Image.open("mirror.jpg")
  img.show()

def copy_image():
  img = Image.open("mirror.jpg")
  width, height = img.size
  for y in range(height):
    for x in range(width // 2):
      r, g, b = img.getpixel((width - x - 1, y))
      img.putpixel((x, y), (r, g, b))
  img.show()
  
#A program that merge two images together on one side of the image.

def merge_image():
  def resize_image(img, new_width, new_height):
        width, height = img.size
        new_img = Image.new("RGB", (new_width, new_height))
        for y in range(new_height):
            for x in range(new_width):
                ori_x = x * width // new_width
                ori_y = y * height // new_height
                r, g, b = img.getpixel((ori_x, ori_y))
                new_img.putpixel((x, y), (r, g, b))
        return new_img
  img = Image.open("mirror.jpg")
  img2 = Image.open("heaven.jpg")
  width, height = img.size
  img2 = resize_image(img2, width // 2, height) 
  for y in range(height):
    for x in range(width // 2):
      r, g, b = img.getpixel((width - x - 1, y))
      img.putpixel((x, y), (r, g, b))
      r1, g1, b1 = img.getpixel((x, y))
      r2, g2, b2 = img2.getpixel((x, y))
      r = int(r1 * 0.5 + r2 * 0.5)
      g = int(g1 * 0.5 + g2 * 0.5)
      b = int(b1 * 0.5 + b2 * 0.5)
      img.putpixel((x, y), (r, g, b))
  img.show()

  
#A program that does grayscale on the right side of the image.

def gray_image():
  img = Image.open("mirror.jpg")
  width, height = img.size
  for y in range(height):
    for x in range(width // 2):
      r, g, b = img.getpixel((width - x - 1, y))
      img.putpixel((x, y), (r, g, b))
 
  for y in range(height):
    for x in range(width // 2, width):  # Only apply to the right half of the image
        r, g, b = img.getpixel((x, y))
        gray = int((r + g + b) / 3)
        img.putpixel((x, y), (gray, gray, gray))
  img.show()


#A program that take merge_image and repeat it for a third image for the right side.
#Plus grayscale of the right side of the image.

def final_image():
    def resize_image(img, new_width, new_height):
        width, height = img.size
        new_img = Image.new("RGB", (new_width, new_height))
        for y in range(new_height):
            for x in range(new_width):
                ori_x = x * width // new_width
                ori_y = y * height // new_height
                r, g, b = img.getpixel((ori_x, ori_y))
                new_img.putpixel((x, y), (r, g, b))
        return new_img
    
    img = Image.open("mirror.jpg") #I believe I got this from  the Istock website
    img2 = Image.open("heaven.jpg") #I believe I got this from image search on Google.
    img3 = Image.open("reaper.jpg") #I believe I got this from image search on Google.
    width, height = img.size
    img2 = resize_image(img2, width // 2, height)  # Resize the second image without using the resize() function
    img3 = resize_image(img3, width // 2, height)  # Resize the third image without using the resize() function
   
         
    for y in range(height):
        for x in range(width // 2):
            r, g, b = img.getpixel((width - x - 1, y))
            img.putpixel((x, y), (r, g, b))
            r1, g1, b1 = img.getpixel((x, y))
            r2, g2, b2 = img2.getpixel((x, y))
            r = int(r1 * 0.6 + r2 * 0.6)
            g = int(g1 * 0.6 + g2 * 0.6)
            b = int(b1 * 0.6 + b2 * 0.6)
            img.putpixel((x, y), (r, g, b))
       
    for y in range(height):
        for x in range(width // 2, width):  # Only apply to the right half of the image
            r, g, b = img.getpixel((x, y))
            gray = int((r + g + b) / 3)
            img.putpixel((x, y), (gray, gray, gray)) 
                 
        for x in range(width // 2, width):
            r3, g3, b3 = img3.getpixel((width // 2 - (x - width // 2) - 1, y))
            r1, g1, b1 = img.getpixel((x, y))
            r = int(r1 * 0.4 + r3 * 0.4)
            g = int(g1 * 0.4 + g3 * 0.4)
            b = int(b1 * 0.4 + b3 * 0.4)
            img.putpixel((x, y), (r, g, b))

    img.show()
final_image()