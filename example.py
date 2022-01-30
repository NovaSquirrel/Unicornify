import hashlib
from unicornavatar import create_avatar

hash = hashlib.md5("your.email@address.here4".encode('utf-8')).hexdigest()

# Creates a BMP file of 256x256 pixels (see docstring of create_avatar)
f = open("unicorn.bmp", "wb")
f.write(create_avatar(128, int(hash, 16)))
f.close()
