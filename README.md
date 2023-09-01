# InventorySystem
This is a basic Flask Inventory System to manage the Ebikes4Africa Bushbike Production. 
It provides a simple and straightforward GUI to read and edit the data stored in a sqlite database. 

# Database
The Database consists of 3 main parts.
### Items:
In the items table all parts needed for the production can be listed. It stores information about the current reserved and unreserved stock and the ordered items. 

### Bikes
This table stores information on the bikes currently in production. It shows their individual name, a description and a due-date. 

### Delays
This table stores all the delays, which occured during the production period. It shows the reason for the delay, when it happened and who has been affected by it. 

# Running the code
### Running locally on your own machine
1. Download all Files / pull the files to your local storage
2. Install all the necessary libraries (flask, flask_sqlalchemy, datetime)  +  install sqlite if you wish to easily access and debug the database
3. run "app.py" file in your terminal
4. Go to the path shown in the terminal output (in most cases http://127.0.0.1:5000/)   (Sometimes there are some issues when trying to access the site via https. Just open it on http instead)

### Running on the web
Just open https://bushbike.pythonanywhere.com/ in any browser on any device. 

