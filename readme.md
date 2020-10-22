# Readme file
## A few notes on how to install and operate this app
1. Requirements:
    * SQL Server installed
    * Dependencies installed:
        - flask
        - werkzeug
        - excel2json
    * [install command: pip install <package> (run it on anaconda prompt)]
2. config.json in root folder with the following properties:
    * server_name
    * database_name
3. The entry file to the app
    * In our app the file 'controller.py' is the entry point, 
        that flask saves in an environtment variable.
    * In order to set the variable, run the command: 'set FLASK_APP=controller.py'
    * To run in debug mode, run the command: 'set FLASK_ENV=development'
4. In order to run the app, run the command: 'flask run'