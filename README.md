# HelloWorldDjango

This app is designed to show Hello World! in bold font and to return it as a JSON response.

To start the server, open to the command prompt and navigate to the folder where you have downloaded the code and contains the manage.py file. <br/>
Run the command: python manage.py runserver 8080 (Any unused port can be used for 8080)
*This command starts the server
Open a brower and navigate to localhost:8080 (Or your custom port number)
*This will utilize the template and display a bold "Hello World!"
Navigate to localhost:8080/GetJSON
*This will produce the Hello World! text coorelating to the key "Message" as a JSON return object.
