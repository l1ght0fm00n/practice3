Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
# Loading the image
image = Image.open(filename)
filename = filename.replace(".jpg", "")
# Converting image from JPG to PNG format
image.save(filename + ".png")
print("Image successfully converted!")