from enum import IntEnum
import medi_scores as ms
"""
Patient data will hold the PatientData class definition and functions
Each patients data will be set using this class, ensuring scalable and safe operations for the MediScore
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
    def __init__(self, on_oxygen, consciousness, resp_rate, oxygen_sat,  temp ):
        
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
        self.on_oxygen = on_oxygen
        self.consciousness = consciousness
        self.resprate = resp_rate
        self.oxygen_sat = oxygen_sat
        self.temp = round(temp, 1) #Round to one decimal point


