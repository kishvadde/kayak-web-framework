# kayak

It is web backend framework built using the python.

To Run the application
 - Create virtual evironment and install the requirements in requirement.txt
 - To run the application with gunicorn server, run following command with virtualenv activated from kayak root folder
   "gunicorn -w <number_of_workers> <path_to_wsgi_interface_of_application>"
   Ex: "gunicorn -w 2 core.wsgi:app"

