from patient_data import PatientData, Consciousness, OnOxygen
from datetime import datetime, timedelta

""" 
Completing testing by using given examples in AireLogic readme  to ensure my logic is working.
Added some of my own edge cases to stretch logic.
Function outputs final score and error messages when applicable
"""



#Airelogic given examples (provided my own default CBG values)

patient1 = PatientData(OnOxygen.AIR, Consciousness.ALERT, 15, 95, 37.1, 5.9, datetime.now())
patient2 = PatientData(OnOxygen.OXYGEN, Consciousness.ALERT, 17, 95, 37.1, 4.0, datetime.now())
patient3 = PatientData(OnOxygen.OXYGEN, Consciousness.CVPU, 23, 88, 38.5, 5.9, datetime.now())

#Edge cases

patient4 = PatientData(OnOxygen.AIR, Consciousness.ALERT, 8, 97, 37.0, 6.1, datetime.now() - timedelta(hours=3))
patient5 = PatientData(OnOxygen.AIR, Consciousness.ALERT, 11, 90, 39.1, 5.9, datetime.now())  

#Time flag cases

#Should be an flag
patient6 = PatientData(OnOxygen.OXYGEN, Consciousness.ALERT, 17, 95, 37.1, 4.3, datetime.now(), [[1, datetime.now() - timedelta(hours=12)]])
#Shouldnt be an flag
patient7 = PatientData(OnOxygen.AIR, Consciousness.ALERT, 15, 95, 37.1, 3.7, datetime.now() - timedelta(hours=5), [[2, datetime.now() - timedelta(hours=12)]])
#Shouldnt be an flag
patient8 = PatientData(OnOxygen.OXYGEN, Consciousness.ALERT, 17, 95, 37.1, 5.4, datetime.now(), [[1, datetime.now() - timedelta(hours=30)]])

test_list = [[0, patient1], [7, patient2], [8, patient3], [6, patient4], [3, patient5]]

test_list_2 = [[1, patient6], [0, patient7], [0, patient8]]

def assert_medi_score(test_list):
    passed = 0
    for i in range(len(test_list)):
        num = i+1
        expected = test_list[i][0]
        actual = test_list[i][-1].get_medi_score()
        #Output message if expected and actual aren't a match, otherwise output success message
        try:
            assert expected == actual, f"<ERROR> Error with test {num}. Expected: {expected} while Actual: {actual}"
            print(f"<SUCCESS> Test {num} passed: {actual} == {expected}")
            passed += 1
        except AssertionError as e:
            print(e)

        
    print(f"Passed {passed}/{len(test_list)} tests")


"""
Testing for the time increase flag in Extension 1
"""
def assert_medi_alerts(test_list):
    passed = 0
    for i in range(len(test_list)):
        num = i+1
        expected = test_list[i][0]
        actual = test_list[i][-1].patient_medi_score()
        try:
            assert expected == actual, f"<ERROR> Error with test {num}. Expected: {expected} while Actual: {actual}"
            print(f"<SUCCESS> Test {num} passed: {actual} == {expected}")
            passed += 1
        except AssertionError as e:
            print(e)
    print(f"Passed {passed}/{len(test_list)} tests")


assert_medi_score(test_list)

assert_medi_alerts(test_list_2)

