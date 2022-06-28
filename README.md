# SensorFabric-Dash

A demo application used to showcase Senor Fabric version 0.1 using Dash. 
Sample screenshot shows synthetic data hosted on Rstudio Connect.

![Screenshot of the dash application in action](/screenshots/sensorfabric-demo-screenshot.png "Demo application using Sensor Fabric and Dash.")

# Installation

It is highly recommeded to create a python virtual environment to run this application.
The application has been tested using `python3.9.12` and `python3.7.7`

``` bash
git clone https://github.com/nextgensh/SensorFabric-Dash.git
cd SensorFabric-Dash
# Pull sensor fabric dependency.
git clone https://github.com/nextgensh/sensorfabric.git
# Create a new python virtual environment (optional step)
python3 -m venv .env
source .env/bin/activate
# Install the dependencies
pip3 install -r requirements.txt
# Start the dash application
python3 app.py
```

# Debug Mode

By default the application will start on `http://127.0.0.1:8050/` with the following output :

``` bash
Dash is running on http://127.0.0.1:8050/

INFO:__main__:Dash is running on http://127.0.0.1:8050/

 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
```

Debug mode allows the application to reload automatically when a change is made. In order to disable it remove `debug=True` from `app.run_server()` inside `app.py`

# Data

Data being demoed in this application comes directly from the underlying sensor fabric layer. Please refer to the sensor fabric layer documentation for further details.
