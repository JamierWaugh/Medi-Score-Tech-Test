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