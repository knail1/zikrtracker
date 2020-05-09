# zikrtracker
this simply python flask app has a db backend and enables daily tracking of zikr with a future feature of running reports

## TODO

### BACKEND:
- create a database 
- create a table with date and zikr tracked column 1 for yes, 0 for no

### FRONTEND:
- create an empty flask app
- post todays date on the top of the main (index) html page
- html javascript code underneath that date to for a big BUTTON to press
  - by default button is RED, and states zikr Not done
  - when clicked:
      - button turns GREEN, stats zikr done
      - an SQL update to the database table, marking the zikr state from 0 to 1 for that day
     
