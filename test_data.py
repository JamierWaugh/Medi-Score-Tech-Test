from patient_data import PatientData, Consciousness, OnOxygen

""" 
Completing testing by using given examples in AireLogic readme  to ensure my logic is working.
Added some of my own edge cases to stretch logic.
Function outputs final score and error messages when applicable
"""



#Airelogic given examples

patient1 = PatientData(OnOxygen.AIR, Consciousness.ALERT, 15, 95, 37.1)
patient2 = PatientData(OnOxygen.OXYGEN, Consciousness.ALERT, 17, 95, 37.1)
patient3 = PatientData(OnOxygen.OXYGEN, Consciousness.CVPU, 23, 88, 38.5)

#Edge cases

patient4 = PatientData(OnOxygen.AIR, Consciousness.ALERT, 8, 97, 37.0)
patient5 = PatientData(OnOxygen.AIR, Consciousness.ALERT, 11, 90, 39.1)  

test_list = [[0, patient1], [4, patient2], [8, patient3], [3, patient4], [3, patient5]]

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

assert_medi_score(test_list)
