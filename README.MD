# Create CMS Spaces

This python script reads a list of space names and pins from the SpaceNames.csv file and creates the spaces on CMS.

clone the git repository to your local server

Create a virtual environment...navigate to the new folder and run the following commands...

    python3 -m venv venv
    source venv/bin/activate

install required packages by running the following command: pip install -r requirements.txt

Create a .env file in the root folder to add the environment variables used to connect to your CMS server.

update the csv file and run the following command in a terminal window...

python3 Create_Spaces.py