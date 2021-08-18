

# How to use

## Linux

* Install Python
 
  * Use a package manager like apt or rpm, or go to the officiail website and follow the Installation instructions for installation on your flavor of linux
  * e.g. For Debian use:
  ```
  sudo apt-get install python3
  ```

* Create a virtual environment: Navigate to the project directory and run these commands
  
  1. ```bash
      #create a virtual environment
      sudo python3 -m venv <env_name>
     ``` 
  2. ```bash
      #activate the virtual environment
      source <env_name>/bin/activate
     ```
  3. ```bash
      #install the requirements
      pip3 install -r requirements.txt
     ```
  4. ```bash
      #run the server
      sudo python3 server.py
     ```

The server will start listening on port 5000.
Make sure to open incoming and outgoing connections to port 5000 from your firewall and also in the security group settings, if you are running from a VPS instance on the cloud.







