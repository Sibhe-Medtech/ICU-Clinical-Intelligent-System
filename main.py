# ICU Clinical Intelligent System
def menu():
    print( "-" * 50)
    print("           ICU CLINICAL INTELLIGENT SYSYTEM")
    print( "-" * 50)
    print("1. Register Patient")
    print("2. View Patient")
    print("3. Search Patient") 
    print("4. Edit")
    print("5. Delete")
    print("6. Assess Patient")
    print("7. View Assessment")
    print("8. Patient priority")
    print("9.Exit")

    while True:
        try:
            choice = int(input("Enter Your Choice : "))
            if 1 <= choice <= 9:
                break
            print("Invalid Choice. Enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Enter numbers only.")
    print("You Selected : ", choice)
    print("-"*35)
    if choice == 1:
          register_patient()
    elif choice == 2:
          view_patient()
    elif choice == 3:
            search_patient()
    elif choice == 4:
            edit_patient()
    elif choice == 5:
          delete_patient()
    elif choice == 6:
          assess_patient()
    elif choice == 7:
         view_assessments()
    elif choice ==8:
         patient_priority()
    elif choice == 9:
         print("Thanks for Visiting")
    else:
          print("Invalid Choice")
          return menu()
def generate_patient_id():
    file = open("patients.csv", "r")
    used_ids = []
    for line in file:
        patient_data = line.strip().split(",")
        if len(patient_data) == 6:
             used_ids.append(patient_data[0])
    file.close()
    count = 1
    while True:
        patient_id = "P" + str(count).zfill(3)
        if patient_id not in used_ids:
            return patient_id
        count = count + 1

def show_bed_status():
    occupied_beds = []
    file = open("patients.csv", "r")
    for line in file:
        patient = line.strip().split(",")
        if len(patient) ==6:
            bed_number = int(patient[5])
            if bed_number not in occupied_beds:
                occupied_beds.append(bed_number)
    file.close()

    total_beds = 50
    available_beds = []
    for bed in range(1, total_beds + 1):
        if bed not in occupied_beds:
            available_beds.append(bed)
    print("\n----- ICU BED STATUS -----")
    print("Total Beds     :", total_beds)
    print("Occupied Beds  :", len(occupied_beds))
    print("Available Beds :", len(available_beds))
    print("\nOccupied Beds:")
    print(occupied_beds)
    print("\nAvailable Beds:")
    print(available_beds)

    return available_beds
          
def register_patient():
                print("---Patient Registraion---")
                print("-"*40)
                patient_id = generate_patient_id()
                print("Patient ID :", patient_id)
                while True:
                     print("main Menu - Press 0")
                     patient_name = input("Enter Patient Name : ").strip()
                     if patient_name =="0":
                          return menu()      
                     if patient_name != "":
                          break
                     print("Patient Name cannot be empty. Please enter a name.")
                
                while True:
                    try:
                        age = int(input("Enter Age : "))
                        if 0 <= age <= 120:
                          break
                        print("Invalid Age. Enter a value between 0 and 120.")
                    except ValueError:
                         print("Invalid Age. Enter numbers only.")

                while True:
                     gender = input("Enter Gender : ").lower()
                     if gender in ["male", "female", "other"]:
                          break
                     print("Invalid Gender. Enter Male, Female, or Other.")

                while True:
                     diagnosis = input("Enter Diagnosis : ").strip()
                     if diagnosis != "":
                          break
                     print("Diagnosis cannot be empty. Please enter a diagnosis.")

                available_beds = show_bed_status()
                while True:
                    bed_number = input("Enter Bed Number : ")
                    if bed_number.isdigit() and 1 <= int(bed_number) <= 50:
                        if int(bed_number) in available_beds:
                            break
                        else:
                             print("Bed", bed_number, "is already occupied.")
                             print("Please choose an available bed.")
                    else:
                        print("Invalid Bed Number. Enter a valid number.")

                file = open("patients.csv", "r")
                duplicate = False
                existing_id = ""
                for line in file:
                     patient_data = line.strip().split(",")
                     if len(patient_data) == 6:
                         if (patient_data[1].lower() == patient_name.lower()
                         and int(patient_data[2]) == age and patient_data[3].lower() == gender.lower()
                         and patient_data[5] == bed_number):

                          duplicate = True
                          existing_id = patient_data[0]
                          break
                file.close()
                if duplicate:
                    print("Patient already exists.")
                    print("Existing Patient ID :", existing_id)
                    return

                print("Done Sucessful")
                print("_"*20)
                print("\nPatient Details")
                file = open("patients.csv", "a")
                file.write(f"{patient_id},{patient_name},{age},{gender},{diagnosis},{bed_number}\n")
                file.close()
                print("Patient ID : ", patient_id )
                print("Patient name :", patient_name)
                print("Age : ", age)
                print("Gender : ", gender)
                print("Diagnosis : ", diagnosis)
                print("Bed Number : ", bed_number)
                return menu()  
def view_patient():
    print("---View Patient Details---")
    print("_" * 40)
    file = open("patients.csv", "r")
    patients =[]
    for line in file:
            patient = line.strip().split(",")
            if len(patient) == 6  :
                patients.append(patient)
    file.close()
    print ("Total Patients : ", len(patients))
    print("\nPatient Details")
    for patient in patients:
                print("-"* 20)
                print("Patient ID -", patient[0])
                print("Patient Name -", patient[1])
                print("Age -", patient[2])
                print("Gender -", patient[3])
                print("Diagnosis -", patient[4])
                print("Bed Number -", patient[5])
                print("-"*20)

def search_patient():
    print("---Search Patient---")
    print("_" * 40)
    while True:
        print("\n1. Search by Patient ID")
        print("2. Search by Patient Name")
        print("3. Search by Diagnosis")
        print("4. Search by Bed Number")
        print("5. Exit")
        choice = input("Enter your choice : ")
        if choice == "5":
            break
        if choice == "1":
            search_value = input("Enter Patient ID : ").strip().upper()
            search_index = 0
        elif choice == "2":
            search_value = input("Enter Patient Name : ").strip().lower()
            search_index = 1
        elif choice == "3":
            search_value = input("Enter Diagnosis : ").strip().lower()
            search_index = 4
        elif choice == "4":
            search_value = input("Enter Bed Number : ").strip()
            search_index = 5
        else:
            print("Invalid choice.")
            continue

        file = open("patients.csv", "r")
        found = False
        for line in file:
            patient = line.strip().split(",")
            if len(patient) != 6:
                 continue
            if patient[search_index].strip().lower() == search_value.lower():
                found = True
                print("\nPatient Details")
                print("Patient ID -", patient[0])
                print("Patient Name -", patient[1])
                print("Age -", patient[2])
                print("Gender -", patient[3])
                print("Diagnosis -", patient[4])
                print("Bed Number -", patient[5])
                print("-" * 30)
        file.close()

        if found == False:
            print("Patient Not Found")

def edit_patient():
      print("\nEdit Patient Details")
      patient_id = input("Enter Patient ID : ").strip().upper()
      patients = []
      found = False
      file = open("patients.csv", "r")
      for line in file:
             patient = line.strip().split(",")
             if len(patient) !=6:
                  continue
             if patient[0]==patient_id:
              found = True
              print("\nFound")
              print("Patient ID - ", patient[0])
              print("Patient Name - ", patient[1])
              print("Age - ", patient[2])
              print("Gender - ", patient[3])
              print("Diagnosis - ", patient[4])
              print("Bed Number - ", patient[5])

              print("1. Edit Name")
              print("2. Edit Age")
              print("3. Edit Diagnosis")
              print("4. Edit Bed Number")
              while True:
                   try:
                        choice = int(input("Enter Your Choice : "))
                        if 1 <= choice <= 4:
                             break
                        print("Invalid choice. Enter a number between 1 and 4.")
                   except ValueError:
                        print("Invalid input. Enter numbers only.")
              if choice == 1:
                    print("Edit Name")
                    new_name = input("New Name : ").strip()
                    patient[1] = new_name
                    print("Updated")
              elif choice == 2:
                   while True:
                        try:
                             new_age = int(input("Enter New Age : "))
                             if 0 <= new_age <= 120:
                                  break
                             print("Invalid Age. Enter a value between 0 and 120.")
                        except ValueError:
                             print("Invalid Age. Enter numbers only.")
                   patient[2] = str(new_age)
                   print("Updated")

              elif choice == 3:
                    new_diagnosis = input("Enter New Diagnosis : ").strip()
                    patient[4] = new_diagnosis
                    print("Updated")

              elif choice == 4:
                   available_beds = show_bed_status()
                   current_bed = patient[5]
                   if current_bed not in available_beds:
                        available_beds.append(current_bed)
                   while True:
                             new_bed = input("Enter New Bed Number : ")
                             if new_bed.isdigit() and 1<= int(new_bed) <= 50:
                                  if int(new_bed) in available_beds:
                                       patient[5] = new_bed 
                                       print("Updated")
                                       break
                                  else:
                                    print("Bed", new_bed, "is already occupied.")
                                    print("Please choose an available bed.")
                             else:
                                 print("Invalid Bed Number. Enter a valid number between 1 to 50.")
              else:
                    print("Invalid choice")
                     
              if found:
                 print("\nPatient Details Updated Successfully")
                 print("-" * 30)
                 print("Patient ID - ", patient[0])
                 print("Patient Name - ", patient[1])
                 print("Age - ", patient[2])
                 print("Gender - ", patient[3])
                 print("Diagnosis - ", patient[4])
                 print("Bed Number - ", patient[5])
                 print("-" * 30)
             patients.append(patient)
      if found == False:
                 print("Patient Not Found")
                 return
      file = open("patients.csv", "w")

      for patient in patients:
             file.write(",".join(patient) + "\n")
      file.close()
      print("Successfully updated")
      return menu()
      
   
def delete_patient():
      print("\n---Delete Patient---")
      patient_id = input("Enter Patient ID : ").strip().upper()
      patients = []
      file = open("patients.csv", "r")
      found = False
      for line in file:
        patient = line.strip().split(",")
        if len(patient) != 6:
             continue
        if patient[0] == patient_id:
            found = True
            print("\nPatient Found")
            print("Patient ID - ", patient[0])
            print("Patient Name - ", patient[1])
            print("Age - ", patient[2])
            print("Gender - ", patient[3])
            print("Diagnosis - ", patient[4])
            print("Bed Number - ", patient[5])

            print("1. Delete")
            print("2. Ignore")
            while True:
                 try:
                      confirm = int(input("\nEnter Your Choice : "))
                      if confirm in [1, 2]:
                           break
                      print("Invalid choice. Enter 1 or 2.")
                 except ValueError:
                      print("Invalid input. Enter numbers only.")
            if confirm == 1:
                print("Patient Selected for Deletion")
                continue
            elif confirm == 2:
                patients.append(patient)
                print("deletion cancelled")
            else:
                  patients.append(patient)
        else:
              patients.append(patient)
              
      file.close()
                 
      if found == False:
            print("patient not found")
            return
      file = open("patients.csv", "w")

      for patient in patients:
        file.write(",".join(patient) + "\n")

      file.close()
      print("Patient details done sucesfully")
      return menu()

def assess_blood_pressure(systolic, diastolic):

    print("\n--- Blood Pressure Assessment ---")

    if systolic < 100 or diastolic < 60:
        return "LOW"

    elif systolic >=130 or diastolic >=90:
        return "HIGH"

    else:
        return "NORMAL"

def assess_spo2(spO2):
    print("\n--- SpO2 Assessment ---")

    if spO2 < 90:
        return "VERY LOW"

    elif spO2 < 95:
        return "LOW"

    else:
        return "NORMAL"

def assess_heart_rate(heart_rate):

    print("\n--- Heart Rate Assessment ---")

    if heart_rate < 60:
        return "LOW"

    elif heart_rate > 100:
        return "HIGH"

    else:
        return "NORMAL"

def assess_temperature(temperature):

    print("\n--- Temperature Assessment ---")

    if temperature < 36:
        return "LOW"

    elif temperature >= 38:
        return "HIGH"

    else:
        return "NORMAL"

def assess_respiratory_rate(respiratory_rate):

    print("\n--- Respiratory Rate Assessment ---")

    if respiratory_rate < 12:
        return "LOW"

    elif respiratory_rate > 20:
        return "HIGH"

    else:
        return "NORMAL"

def assess_patient():
    print("---Patient Assessment---")
    print("-" * 40)
    patient_id = input("Enter Patient ID : ").strip().upper()
    file = open("patients.csv", "r")
    patient_found = False
    patient_name = ""
    bed_number = ""
    for line in file:
        patient = line.strip().split(",")
        if len(patient) != 6:
            continue
        if patient[0].upper() == patient_id:
            patient_found = True
            patient_name = patient[1]
            bed_number = patient[5]
            break
    file.close()
    if patient_found == False:
        print("Patient Not Found.")
        return
    print("\nPatient Details")
    print("-"*20)
    print("Patient ID   :", patient_id)
    print("Patient Name :", patient_name)
    print("Bed Number   :", bed_number)
    print("-"*20)

    file = open("assessments.csv", "r")
    already_assessed = False
    for line in file:
        assessment = line.strip().split(",")
        if len(assessment) > 0:
            if assessment[0].upper() == patient_id:
                already_assessed = True
                break
    file.close()

    if already_assessed:
        print("\nPatient", patient_id, "has already been assessed.")
        print("Duplicate assessment is not allowed.")
        return
    print("\nEnter Clinical Parameters")
    print("-"*20)
    while True:
        try:
             systolic = int(input("Enter Systolic BP : "))
             if systolic > 0:
                      break
             print("Invalid Systolic BP.")
        except ValueError:
             print("Invalid Systolic BP. Enter numbers only.")

    while True:
        try:
             diastolic = int(input("Enter Diastolic BP : "))
             if diastolic > 0:
                    break
             print("Invalid Diastolic BP.")
        except ValueError:
             print("Invalid Diastolic BP. Enter numbers only.")

    while True:
        try:
             spo2 = int(input("Enter SpO2 (%) : "))
             if 0 <= spo2 <= 100:
                  break
             print("Invalid SpO2. Enter a value between 0 and 100.")
        except ValueError:
             print("Invalid SpO2. Enter numbers only.")
    while True:
        try:
             heart_rate = int(input("Enter Heart Rate : "))
             if heart_rate > 0:
                  break
             print("Invalid Heart Rate.")
        except ValueError:
             print("Invalid Heart Rate. Enter numbers only.")

    while True:
        try:
             respiratory_rate = int(input("Enter Respiratory Rate : "))
             if respiratory_rate > 0:
                  break
             print("Invalid Respiratory Rate. Enter numbers only.")
        except ValueError:
             print("Invalid Respiratory Rate. Enter numbers only.")

    while True:
        temperature = float(input("Enter Temperature (°C) : "))
        try:
            if 25 <= temperature <= 45:
                break
            print("Invalid Temperature.")
        except ValueError:
            print("Enter a valid temperature.")
    bp_status = assess_blood_pressure(systolic, diastolic)
    spo2_status = assess_spo2(spo2)
    heart_rate_status = assess_heart_rate(heart_rate)
    temperature_status = assess_temperature(temperature)
    respiratory_rate_status = assess_respiratory_rate(respiratory_rate)

    risk_score = 0
    if bp_status != "NORMAL":
        risk_score = risk_score + 1
    if spo2_status != "NORMAL":
        risk_score = risk_score + 1
    if heart_rate_status != "NORMAL":
        risk_score = risk_score + 1
    if respiratory_rate_status != "NORMAL":
         risk_score = risk_score + 1
    if temperature_status != "NORMAL":
        risk_score = risk_score + 1

    if risk_score >= 3:
        overall_status = "CRITICAL"
    elif risk_score >= 1:
        overall_status = "NEEDS ATTENTION"
    else:
        overall_status = "NORMAL"

    print("\n--- Clinical Assessment Results ---")
    print("-" * 40)
    print("Blood Pressure   :", bp_status)
    print("SpO2             :", spo2_status)
    print("Heart Rate       :", heart_rate_status)
    print("Respiratory Rate :", respiratory_rate_status)
    print("Temperature      :", temperature_status)
    print("-" * 40)
    print("Risk Score       :", risk_score)
    print("Overall Status   :", overall_status)
    print("-" * 40)



    file = open("assessments.csv", "a")
    file.write(
        patient_id + "," + patient_name + "," +
        str(bed_number) + "," + str(systolic) + "," + str(diastolic) + "," + str(spo2) + "," + str(heart_rate)+ ","+
        str(respiratory_rate) + "," + str(temperature) +","+ bp_status + "," + spo2_status + "," +
        heart_rate_status + "," + respiratory_rate_status + "," + temperature_status + "," +
        str(risk_score) + "," + overall_status +"\n")
    file.close()
    print("\nAssessment Saved Successfully.")
    
def view_assessments():
    print("\nView Assessment")
    print("_" * 20)
    patient_id = input("Enter Patient ID : ").strip().upper()
    file = open("assessments.csv", "r")
    found = False
    for line in file:
        patient_assess = line.strip().split(",")
        if len(patient_assess) != 16:
            continue
        if patient_assess[0].upper() == patient_id: 
            found = True
            print("\n  Patient Details")
            print("-" * 30)
            print("Patient ID       :", patient_assess[0])
            print("Patient Name     :", patient_assess[1])
            print("Bed Number       :", patient_assess[2])
            print("-"* 30)

            print("\n  Clinical Parameters")
            print("Systolic BP      :", patient_assess[3])
            print("Diastolic BP     :", patient_assess[4])
            print("SpO2             :", patient_assess[5])
            print("Heart Rate       :", patient_assess[6])
            print("Respiratory Rate :", patient_assess[7])
            print("Temperature      :", patient_assess[8])
            print("-" * 30)

            print("\n  Assessment Results")
            print("Blood Pressure      :", patient_assess[9])
            print("SpO2 Status         :", patient_assess[10])
            print("Heart Rate Status   :", patient_assess[11])
            print("Respiratory Status  :", patient_assess[12])
            print("Temperature Status  :", patient_assess[13])
            print("Risk Score          :", patient_assess[14])
            print("Overall Status      :", patient_assess[15])
            print("-" *40)
            break
    file.close()
    if found == False:
        print("Patient Assessment Not Found.")
        return
    
def patient_priority():
    print("\n--- ICU Patient Priority ---")
    file = open("assessments.csv", "r")
    patients = []
    for line in file:
        patient_assess = line.strip().split(",")
        if len(patient_assess) != 16:
            continue
        patient_id = patient_assess[0]
        patient_name = patient_assess[1]
        bed_number = patient_assess[2]
        bp_status = patient_assess[9]
        spo2_status = patient_assess[10]
        heart_rate_status = patient_assess[11]
        respiratory_rate_status = patient_assess[12]
        temperature_status = patient_assess[13]

        risk_score = int(patient_assess[14])
        overall_status = patient_assess[15]

        focus = []

        if bp_status != "NORMAL":
            focus.append("BP")
        if spo2_status != "NORMAL":
            focus.append("SpO2")
        if heart_rate_status != "NORMAL":
            focus.append("Heart Rate")
        if respiratory_rate_status != "NORMAL":
            focus.append("Respiratory Rate")
        if temperature_status != "NORMAL":
            focus.append("Temperature")
        if len(focus) == 0:
            focus_on = "None"
        else:
            focus_on = ", ".join(focus)

        patients.append([ patient_id, patient_name, bed_number, risk_score, focus_on,overall_status ])
    file.close()
    patients.sort(key=lambda x: x[3], reverse=True)
    print("\n   Priority Order")
    print("-" * 50)

    priority = 1
    for patient in patients:
        print("\n   Priority", priority)
        print("Patient ID   :", patient[0])
        print("Patient Name :", patient[1])
        print("Bed Number   :", patient[2])
        print("Risk Score   :", patient[3])
        print("Focus On     :", patient[4])
        print("Status       :", patient[5])
        print("-" * 50)
        priority = priority + 1

menu()
 





