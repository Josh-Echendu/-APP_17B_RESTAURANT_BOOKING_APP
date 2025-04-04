import qrcode

# Create QR image
image = qrcode.make("http://127.0.0.1:8000") # replace "http://127.0.0.1:8000/" with the domain name

# Create image file
image.save('qr.png')

# Create project: django-admin startproject mysite .
# Create app:python manage.py startapp restaurant_menu 
# Then go to setting and insert your app name there
# Run a project: python manage.py runserver
# Create database module: 