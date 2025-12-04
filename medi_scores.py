from datetime import datetime, timedelta

"""
Defining all scoring systems in medi_scores file.
Allows class to dynamically call and assess individual values to compute overall medi score.
Each function returns the correct score value of the attribute, or an error if value is out of range.
"""
def on_oxygen_scores(on_oxygen):
    if on_oxygen == 0:
        return 0
    if on_oxygen == 2:
        return 2
    else:
        raise RuntimeError("Parameter on_oxygen did not contain the correct values")
    
def consciousness_scores(consciousness):
    if consciousness == 0:
        return 0
    #Enum sets CVPU to a non-zero value of 1
    if consciousness == 1:
        return 3
    else:
        raise RuntimeError("Parameter consciousness did not contain the correct values")
def resp_rate_scores(resp_rate):
    #Values are all inclusive
    if resp_rate >= 25 or resp_rate <= 8:
        return 3
    if resp_rate >= 21 and resp_rate <= 24:
        return 2
    if resp_rate >= 9 and resp_rate <= 11:
        return 1
    if resp_rate >= 12 and resp_rate <= 20:
        return 0
    else:
        raise RuntimeError("Parameter resp_rate did not contain the correct values")
    
    
def oxygen_sat_scores(oxygen_sat, on_oxygen):
    if oxygen_sat <= 83 or (oxygen_sat >= 97 and on_oxygen == 2):
        return 3
    if (oxygen_sat >= 84 and oxygen_sat <= 85) or ((oxygen_sat >= 95 and oxygen_sat <= 96) and on_oxygen == 2):
        return 2
    if (oxygen_sat >= 86 and oxygen_sat <= 87) or ((oxygen_sat >= 93 and oxygen_sat <= 94) and on_oxygen == 2):
        return 1
    if (oxygen_sat >= 88 and oxygen_sat <= 92) or (oxygen_sat >= 93 and on_oxygen == 0):
        return 0
    else:
        raise RuntimeError("Paramters oxygen_sat or on_oxygen did not contain the correct values")
    
def temp_scores(temp):
    if temp <= 35.0:
        return 3
    if temp >= 39.1:
        return 2
    if (temp >= 35.1 and temp <= 36.0) or (temp >= 38.1 and temp <= 39.0):
        return 1
    if temp >= 36.1 and temp <= 38.0:
        return 0
    else:
        raise RuntimeError("Parameter temp did not contain the correct values")
    
def cbg_scores(CBG, last_meal_time):
    #If last meal was less than 2 hours ago
    if datetime.now() - last_meal_time <= timedelta(hours=2):
        if CBG <= 4.5 or CBG >= 9.0:
            return 3
        if (CBG >= 4.5 and CBG <= 5.8) or (CBG >= 7.9 and CBG <= 8.9):
            return 2
        if CBG >= 5.9 and CBG <= 7.8:
            return 0 
    #If last meal was later than 2 hours ago (fasting phase)
    else:
        if CBG <= 3.4 or CBG >= 6.0:
            return 3
        if (CBG >= 3.5 and CBG <= 3.9) or (CBG >= 5.5 and CBG <= 5.9):
            return 2
        if CBG >= 4.0 and CBG <= 5.4:
            return 0


