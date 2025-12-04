# Medi-Score-Tech-Test
Medi score tech test for airelogic
## Patient Data
I have decided to create a class to facilitate the storage of the health data attributes as Patient Data. This will help ensure scalability in the solution and data consistency across functions. To implement this safely, I have enforced strict type control on initialisation so the system can fail fast with incorrect values. 

Furthermore, I have created Enum classes to facilitate setting of unique values such as AIR for on_oxygen values. This comes in handy when handling data that is not as simple as an integer value

PatientData then has get methods for each individual score for all the attributes by calling the medi_score functions. These methods can then be used to find the summation of all scores and thus, the final Medi Score.

## Medi Scores
The Medi Scores file is used here to keep scoring logic separate from class, reducing complexity of the class and keeping it maintainable and scalable.

The file itself contains all scoring logic that can then be called by the patient data class to calculate the Medi score.

Each scoring system should contain checks for any scoring outcome, but if not it will raise a run time error in the applicable score attribute.

## Test Data
I have gathered test data from the official examples given by AireLogic. By comparing expected output and actual output, I can assess whether or not the system is functional. I have tried to ensure the test system is scalable by not hardcoding test calls but instead relying on a loop through a list of tests.

## Extension 1: Flag checks for rapidly changing score
For the first extension, I have chosen to implement a "prior_list", a small data structure to act as historical data for the patient's scores. This list is set at default to [] but can have a list passed into it as a parameter. This prior_list can then be queried when a new score is calculated in order to see whether the score has changed by more than 2 points in less than 24 hours. If it has changed rapidly, it will produce an alert message in the terminal and return a 1 flag, where the system could be further developed to provide more functionality with this. If no flag occurs a 0 is returned. I am using the datetime library to get the current time and I am hardcoding timedeltas into the test data in order to simulate older data in the list.

## Extension 2: Capillary Blood Glucose implementation
For the second extension, I initially struggled to understand the scoring system with the Capillary Blood Glucose (CBG) levels. Eventually I believe I came to the right conclusion of assuming fasting was determined as longer than 2 hours since the last meal, and the other scoring was when the last meal was within the last two hours. With this decided, it wasn't too difficult to implement as it was simply just another attribute that needed checking and scoring. The scoring system was a little more complex with multiple potential scores for the same attribute but I believe I implemented it correctly. 

## End Notes
I have really enjoyed this challenge. It was a nice reminder of how functional and applicable Object Orientated Programming can be, which is something that hasn't been the focus of my coursework recently. I am happy with my solution and the fact it passes all of my test cases. The system should be relatively easy to test yourself if you just add tests to the test_list. I hope you like my solution and any feedback for improvements would be appreciated.
