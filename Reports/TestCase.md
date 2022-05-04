| Test Case ID | TC Description        | Test steps       | Test Data  | Expected results | Pass/Fail | Defect ID/Link |
| ------------ | --------------------- | ---------------- | ---------- | ---------------- | --------- | -------------- |
| TC01         | Check Search page elements | 1. open Search Page <br> 2. verify Search field</br><br>3. verify list of cities </br>| |  1. Search field is prefifilled with default 'Seach' <br>2. list of cities is in alphabetical order</br> | | |
| TC02 | Check Search results according to entered keywords | 1. open Search Page <br>2. start to enter search phrase</br>| dos | 1. when user start typing search phrase in text field -> search result should suggest words that matches typed keyword<br>2. search results for searching phrase displayed in alphabetical order </br>| | |
| TC03 | Check cities from the list are tapable | 1. open Search Page<br>2. tap random city from the list</br> | | 1. user redirected to 'google map' screen  <br>2. Pin set acccording chosen city</br> | | |
| TC04 | Check error message/ field tips displsyed | 1. open Search Page<br>2. do NOT enter search phrase</br><br>3. tap 'enter'</br> | | 1. error message/ field tips appears under 'Search field': "field can not be empty" |||
| TC05 | Check error message displayed on empty 'Search results' page | 1. open Search Page <br>2. enter incorrect keyword</br> | asdfghh<br>1233456</br><br>!@#$%%^^</br> | 1. error message displayed on serach results page: 'No results found, try to rephrase' |||
| TC06 | Check autocorrection | 1. open Search Page<br>2. enter search phrase 'ver'</br><br>3. observe list of search result</br><br>4. do NOT tap '-' , tap 'space'</br><br>5. observe Search results</br> | ver sur mer | autocorrect should be provided and presented in Search results: 'ver sur mer' = 'ver-sur-mer' |||







