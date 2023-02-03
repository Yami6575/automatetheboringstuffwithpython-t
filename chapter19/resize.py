'''import os
from PIL import Image

size = 300
logo= 'catlogo.png'

logoim = Image.open(logo)
logowidth, logoheight = logoim.size

os.makedirs('withLogo', exist_ok=True)

for filename in os.listdir('.'):
    if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg')
            or filename.lower().endswith('.gif') or filename.lower().endswith('bmp')) \
            or filename == logo:
        continue   

    im = Image.open(filename)
    width, height = im.size

    
    if width > size and height > size:
        
        if width > height:
            height = int((size / width) * height)
            width = size
        else:
            width = int((size / height) * width)
            height = size


    print('Resizing {}...'.format(filename))
    im = im.resize((width, height))
    width, height = im.size
    if width < logowidth * 2 or height < logoheight * 2:
        print("The logo wouldn't look good on an image this size so "
              "it is being skipped. The unadorned image will still be saved "
              "to the 'withLogo' directory.")
    else:
        print('Adding logo to {}...'.format(filename))
        im.paste(logoim, (width - logowidth, height - logoheight), logoim
    )

    # Save changes.
    im.save(os.path.join('withLogo', filename))'''
import os
from PIL import Image as img

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = img.open(LOGO_FILENAME)
logoIm = logoIm.resize((75,75))
logoWidth, logoHeight = logoIm.size

os.makedirs('withLogo', exist_ok=True)

for filename in os.listdir('.'):
    if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpeg') or filename.lower().endswith('.jpg') or filename.lower().endswith('.bmp') or filename.lower().endswith('gif')) or filename == LOGO_FILENAME:
        continue
    im = img.open(filename)
    width, height = im.size
    if not (width >= 2 * logoWidth and height >= 2 * logoHeight):
        print("Skipping logo addition to %s" % (filename))
        continue
    

    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            height = int((SQUARE_FIT_SIZE/width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE/height) * width)
            height = SQUARE_FIT_SIZE
        print('Resizing %s... ' % (filename))
    
        im = im.resize((width, height))
    
    print('Adding logo to %s...' % (filename))
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

    im.save(os.path.join('withLogo',filename))