# Reminder Notification System
This is a simple reminder python program that shows you a particular notification base on your given *text and title* after your desired time (minutes).'

**NOTE : You can write to the CSV file (remind-data.csv)  by using MS Excel. But Don't change the title of the CSV File ``` Title, Message, Time```**

## Modules & Packages
### External Packages
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages.

```bash
> pip install pyttsx3 
> pip install plyer
```
### Import Modules
```
import os #To manage the CSV file exists
import time #To show the notification after a particular time 
import pandas as pd #To access the CSV file columns and rows
import pyttsx3 #To use the text to speech facility for speaking text
from plyer import notification #Show text and title as notification
```
## Usage
**You can give information and it will remind you the message**

```
1. First run the program and input the information
2. Open generated remind-data.csv on Excel and write 
   the Title, Message, Time
3. After giving the information on CSV run the program.
   It will remind the message after given minutes
```

## Overview
**If remind-data.csv doesn't exists it will ask such inputs one by one like below and fill the CSV file with the given data**
```python
 * Enter the remind short title (q to quit): [Title]
 * Enter the message to display : [Text]
 * Provide time in minutes : [Time]
--------------------------------------------------
 #Then the program will be started
```
## Run the program in the background
**Open the PowerShell on the directory and write the command as below***
```
pythonw ./main.py
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Version Information
| -----Python-----|----- 3.9 -----|
|---------	|--------	|
| Pip     	| 20.2.4 	|
| Pyttsx3 	| 2.90   	|
| Plyer   	| 1.4.3  	|

## License
**This is created by Fahad**
## Thanks for visiting
### Please help me to improve the notification system.
