Service to do the actual conversion:

    # imagemagick -> make a new image only keeping red pixels
    $ convert ticket.jpg -fuzz 10% -fill black -opaque "#C1372C" -threshold 3% ticket-converted.jpg

    # tesseract -> read image, only looking for numbers on a single line
    $ tesseract ticket-converted.jpg stdout digits

App that submits photo, allows for confirmation and manual fix.

Where to store photos? dropbox, s3?

=====================

    $ docker build -t zackdever/wiggly-numbers .
    $ docker run -p 5000:5000 zackdever/wiggly-numbers
