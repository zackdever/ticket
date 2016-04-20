1. Service to do the actual conversion:

    # imagemagick -> make a new image only keeping red pixels
    $ convert ticket.jpg -fuzz 10% -fill black -opaque "#c5513b" -threshold 3% ticket-converted.jpg

    # tesseract -> read image, only looking for numbers on a single line
    $ tesseract ticket-converted.jpg stdout digits
    
2. App that submits photo, allows for confirmation and manual fix.

3. Where to store photos?

=====================

web server that can run flask app, has permissions to run system commands,
and has imagemagick and tesseract installed

probably docker on ec2/ecs?
