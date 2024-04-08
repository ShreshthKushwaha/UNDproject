Welcome to Server Side Implementation of UND Project

##To fire the flask server follow the steps:

0. MAke sure you have latest python,msql, and pip installed. I also recommend installing mysql workbench. After installing pip make sure to install any packages shown missing or not found by python in these files. After making sure that python recognizes all the packages you can move forward with following steps. 

1. Go to terminal or CMD 
2. cd/ to the UND_PROJECT folder
3. edit database_config file with your appropriate credentials
4. navigate to scripts
5. run the command "python3 database_config.py". Verify that the relevant database and its tables should be present in your mysql workbench database.
6. run the command "python3 ingestion_command.py"
7. Enter start and end dates of the data you want to import in your rdbms.
8. run the command "python3 flask_apis.py"
9. go to the relevant url shown by the terminal 
10. Use the postman to hit those end points. Here are the steps to hit the end points

1. Hit login end point with POST type and body {"username":"username1",
"password":"password1"}   
2. Copy and paste the token somewhere. Please beware that this token would be valid for 30 mins. After that you may need to generate another token.
3. Now you can go ahead and hit another pointers with the required parameters. Before hitting you need to navidate to headers tab. Set key=Authorization and Value = your_copied_token
4. Send the requests and get your desired data.


