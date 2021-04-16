# Sintegrate by Slack Overflow (Team No.: Team163)
The project Sintegrate in HackUST is designed for catering industry to implement a online ordering platform. It can calculate the ETA based on the locations of customers and restauarnt. By knowing ETA in advance, restaurants can manage take-away, dine-in orders efficiently.

The template of our design can be found at https://www.figma.com/proto/uHcpL3mVZhMhRz6NrOWgua/HackUST?node-id=16%3A1159&scaling=scale-down&page-id=0%3A1

The main app interfaces:
![Image of UI-](https://github.com/Andrew-FungKinHo/Dynamic-Queuing-Solution/blob/master/demo-media/reserve_for_now.jpeg)
Reserving for Now:
![Image of UI-](https://github.com/Andrew-FungKinHo/Dynamic-Queuing-Solution/blob/master/demo-media/main.jpeg)

The list of orders from the restaurant's view will be:
![Dynamic Table](https://github.com/Andrew-FungKinHo/Dynamic-Queuing-Solution/blob/master/demo-media/dynamic_table.gif)

## Requirement
  Python version >= 3.6
  
  ```bash
  pip install -r requirement.txt
  ```
## Setup
  You will need an API key to be able to display the data on the Google Maps interface.
  For registration, go to: https://console.developers.google.com/?hl=zh-tw and make sure to enable Google Maps API and Geocoding API.

  With a valid key, go to `settings.py` and type `PLACES_MAPS_API_KEY` to the your actual token in the html input and you will able to view the results.

  To start running the proejct, use the following commands in terminal:
  ```bash
  python manage.py runserver
  ```
  To make migratiton in models, ctrl + c to stop the server, and then use the following commands:
  ```bash
  python manage.py makemigrations
  
  python mange.py migrate
  ```
  After the migration, use the runserver command to restart the server.
 
## Customer View
  The customer view can be found in 127.0.0.1:8000/
  
## Admin View
  The admin view can be found in 127.0.0.1:8000/admin
  
  The order list can be found in 127.0.0.1:8000/order
   
  To create super user, first ctrl + c to stop server.
  
  Then go to terminal and use the following commands:
  ```bash
  python manage.py makesuperuser
  ```
  After following the instructions and input the userid, password, restart server.
  
  Visit the admin page using the super user id and password. Then you can add instances for testing.
