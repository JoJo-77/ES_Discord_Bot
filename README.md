# ES_Discord_Bot

## Requirements
 - Download selenium package for python
 - Download Chromedriver 
## Useage 

## Links
 - [Public ES Schedule](https://account.subitup.com/public/?5t7i0fpakJA%3d#byTimeDay)
 - [Selenium](https://selenium-python.readthedocs.io/installation.html)
 - [Chromedriver](http://chromedriver.storage.googleapis.com/index.html?path=72.0.3626.7/)

## Notes
- Scraped website by grabbing all raw text and parsing it for schedules 
- Days of the week are selected by multiple elements structured as: ```div class="d_x day``` where x is the day of the week, 0 being the current day and 6 being the seventh day of the week.
  - This means that selecting 0 will always give you the current day, not monday, so weeks are relative not absolute.
- ### Ideas
  - Support functionality for user commands or automation (or both)
  - See about exporting data to google spreadsheet if necessary
- ### Implementations / Milestones
  - Created webscraper using selenium
    - correctly parses text and converts it into a dictionary of worker keys and shift values
