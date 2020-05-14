# TheHackerNews Scrapper
 This script scraps the data from [TheHackerNews](https://thehackernews.com) and stores into MongoDB cloud database.
 

### How to Run?

#### PreRequisites
  * [Python ~3.7](https://www.python.org/)
  
#### Setup Project:
#####  1. Clone or Download the project and `cd` into the `TheHackerNews/` folder.

#####  2. Upgrade pip
   ```
   $ python3 -m pip install --user --upgrade pip
   ```

#####  3. Install virtualenv
  - On macOS and Linux:
  ```
  $ python3 -m pip install --user virtualenv
  ```

  - On Windows:
  ```
  py -m pip install --user virtualenv
  ```
  
  
##### 4. Creating a virtual environment
 - On macOS and Linux:
 
 ```
 python3 -m venv env
 ```
 
 -On Windows:
 ```
 py -m venv env
 ```
#####  5. Commands to activate virtual env:

  - On macOS and Linux:
  ```
  $ source env/bin/activate
  ```

  - On Windows:
  ```
  .\env\Scripts\activate
  ```

#####  6. Install dependencies:
  ```
  $ pip install -r requirements.txt
  ```

#####  7. Change `USERNAME` and `PASSWORD` in `scrapper.py` file.
  ```

  ```

#### Launch Project
#####  1. run the app using command:
  ```
  $ python scrapper.py
  ```



### If you're running into issues:
contact me on [twitter](https://www.twitter.com/harshsahu97/)
