# ES_Discord_Bot

## Requirements

## Useage 

## Links
 - [Public ES Schedule](https://account.subitup.com/public/?5t7i0fpakJA%3d#byTimeDay)

## Notes
- The schedule data is run through scripts therefore we cannot use webscraping to pull data from the website
- Days of the week are selected by multiple elements structured as: ```div class="d_x day``` where x is the day of the week, 0 being the current day and 6 being the seventh day of the week.
  - This means that selecting 0 will always give you the current day, not monday, so weeks are relative not absolute.
- ### Ideas
  - Using a webdriver (I have experience in selenium with python) we can select all the text from the page and parse the resulting text to find schedules
  - Support functionality for user commands or automation (or both)
  - See about exporting data to google spreadsheet if necessary
- ### Implementations / Milestones
