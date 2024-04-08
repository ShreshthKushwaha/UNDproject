# Welcome to Server Side Implementation of UND Project

## To fire up the Flask server, follow these steps:

0. Make sure you have the latest Python, MySQL, and pip installed. It's also recommended to install MySQL Workbench. After installing pip, ensure that you install any packages shown as missing or not found by Python in the provided files. Once Python recognizes all the packages, you can proceed with the following steps.

1. Open your terminal or command prompt.

2. Navigate to the UND_PROJECT folder using the `cd` command.

3. Edit the `database_config` file with your appropriate credentials.

4. Navigate to the `scripts` directory.

5. Run the command `python3 database_config.py`. Verify that the relevant database and its tables are present in your MySQL Workbench database.

6. Run the command `python3 ingestion_command.py`.

7. Enter the start and end dates of the data you want to import into your RDBMS.

8. Run the command `python3 flask_apis.py`.

9. Go to the relevant URL shown by the terminal.

10. Use Postman to hit those endpoints. Here are the steps to hit the endpoints:

    1. Hit the login endpoint with a POST request type and body `{"username":"username1", "password":"password1"}`.
    
    2. Copy and paste the token somewhere safe. Note that this token will be valid for 30 minutes. After that, you may need to generate another token.
    
    3. Now, you can proceed to hit other endpoints with the required parameters. Before hitting, navigate to the Headers tab in Postman. Set Key=Authorization and Value=your_copied_token.
    
    4. Send the requests and retrieve your desired data.
