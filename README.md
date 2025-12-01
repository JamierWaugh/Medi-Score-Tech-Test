# Medi-Score-Tech-Test
Medi score tech test for airelogic
## Patient Data
I have decided to create a class to facilitate the storage of the health data attributes as Patient Data. This will help ensure scalability in the solution and data consistency across functions. To implement this safely, I have enforced strict type control on initialisation so the system can fail fast with incorrect values. 

Furthermore, I have created Enum classes to facilitate setting of unique values such as AIR for on_oxygen values. This comes in handy when handling data that is not as simple as an integer value