# Sintegrate
The project is designed for catering industry to implement a online ordering platform. It can calculate the ETA based on the locations of customers and restauarnt

# Requirement
  Python >= 3.6
  
  pip install -r requirement.txt
  
# Setup
  
  To start running the proejct, use the following commands in terminal:
  
  python manage.py runserver
  
  To make migratiton in models, ctrl + c to stop the server, and then use the following commands:
  
  python manage.py makemigrations
  
  python mange.py migrate
 
  After the migration, use the runserver command to restart the server.
 
# Customer View
  The customer view can be found in 127.0.0.1:8000/
  
# Admin View
  The admin view can be found in 127.0.0.1:8000/admin
  
  The order list can be found in 127.0.0.1:8000/order
   
  To create super user, first ctrl + c to stop server.
  
  Then go to terminal and use the following commands:
  
  python manage.py makesuperuser
  
  After following the instructions and input the userid, password, restart server.
  
  Visit the admin page using the super user id and password. Then you can add instances for testing.
  