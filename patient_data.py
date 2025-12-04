from enum import IntEnum
import medi_scores as ms
from datetime import datetime, timedelta
"""
Patient data will hold the PatientData class definition and functions
Each patients data will be set using this class, ensuring scalable and safe operations for the MediScore

I have kept all Get methods for the scores inside the class, this ensures that each score return is also limited by the strict type checks.
By defining each get_<data_point>_score methods independently, I can have more flexible reporting, debugging and be ready for future functionality.
"""

#Enum  object for on_oxygen value
class OnOxygen(IntEnum):
    AIR = 0
    OXYGEN = 2

#Enum object for consciousness value
class Consciousness(IntEnum):
    ALERT = 0
    CVPU = 1

class PatientData():
    def __init__(self, on_oxygen, consciousness, resp_rate, oxygen_sat,  temp, prior_list=[] ):
        
        #Enforce types of each value
        
        if not isinstance(on_oxygen, OnOxygen):
            raise TypeError("Attribute on_oxygen is not of type OnOxygen")
        if not isinstance(consciousness, Consciousness):
            raise TypeError("Attribute consciousness is not of type Consciousness")
        if not isinstance(resp_rate, int):
            raise TypeError("Attirbute resp_rate is not of type int")
        if not isinstance(oxygen_sat, int):
            raise TypeError("Attribute oxygen_sat is not of type int")
        if not isinstance(temp, float):
            raise TypeError("Attribute temp is not of type float")
        if not isinstance(prior_list, list):
            raise TypeError("Attribute prior_list is not of type List")
        
        self.current_score = None
        self.prior_list = prior_list
        self.on_oxygen = on_oxygen
        self.consciousness = consciousness
        self.resp_rate = resp_rate
        self.oxygen_sat = oxygen_sat
        self.temp = round(temp, 1) #Round to one decimal point

    #Get functions for all scores
    def get_on_oxygen_score(self):
        return ms.on_oxygen_scores(self.on_oxygen)
    def get_consciousness_score(self):
        return ms.consciousness_scores(self.consciousness)
    def get_resp_rate_score(self):
        return ms.resp_rate_scores(self.resp_rate)
    def get_oxygen_sat_score(self):
        return ms.oxygen_sat_scores(self.oxygen_sat, self.on_oxygen)
    def get_temp_score(self):
        return ms.temp_scores(self.temp)
    
    def get_medi_score(self):
        return ( self.get_on_oxygen_score() +
            self.get_consciousness_score() +
            self.get_resp_rate_score() +
            self.get_oxygen_sat_score() +
            self.get_temp_score()
        )
    
    #Sets the patient score and updates the prior list, also returns a flag dictating whether score has increased by more than 2 in last 24 hours
    def patient_medi_score(self):

        medi_score = self.get_medi_score()
        #Append score and time of score taken to object list
        self.prior_list.insert(0, [medi_score, datetime.now()])
        self.current_score = medi_score

        if len(self.prior_list) > 1:
            #If time of last score taken is less than 24 hours and current score is more than 2 greater than latest medi score, create alert
            if (datetime.now() - self.prior_list[1][1]) < timedelta(hours=24) and self.current_score -  self.prior_list[1][0] > 2:
                print("ALERT: Score increased by more than 2 points in the last 24 hours. Additional risk flagged.")
                return 1 #Return 1 if alert is required
        return 0 #Return 0 if finishes fine
