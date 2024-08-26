#3
Sex    = str(input("Enter your sex:  "))
Value_hemoglobin = int(input("Enter your hemoglobin: "))
if Sex == "Man":

    if (167 >= Value_hemoglobin >= 134):
        print("Pass. You are good!")
    elif Value_hemoglobin > 167:print("Fail. You are not good!")
    elif Value_hemoglobin < 134:print("Fail. You are not good!")
if Sex == "Woman":
    if 155 >= Value_hemoglobin >= 117:
        print("Pass. You are good!")
    elif Value_hemoglobin > 155:print("Fail. You are not good!")
    elif Value_hemoglobin < 117:print("Fail. You are not good!")




