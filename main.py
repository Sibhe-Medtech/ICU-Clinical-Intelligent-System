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
    print("8. Exit")

    choice = int(input("Enter Your Choice "))
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
    elif choice == 8:
         print("Thanks for Visiting")
    else:
          print("Invalid Choice")
def generate_patient_id():
    file = open("patients.csv", "r")
    used_ids = []
    for line in file:
        patient_data = line.strip().split(",")
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
        if patient:
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
                     patient_name = input("Enter Patient Name : ").strip()
                     if patient_name != "":
                          break
                     print("Patient Name cannot be empty. Please enter a name.")
                
                while True:
                     age = int(input("Enter Age : "))
                     if 0 <= age <= 120:
                          break
                     print("Invalid Age. Enter a value between 0 and 120.")

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
def view_patient():
    print("---View Patient Details---")
    print("_" * 40)
    while True:
        patient_id = input("Enter Patient ID (or 0 to go back): ")
        if patient_id == "0":
            return menu()
        found = False
        file = open("patients.csv", "r")
        for line in file:
            patient = line.strip().split(",")
            if patient[0] == patient_id:
                found = True
                print("\nPatient Details")
                print("Patient ID -", patient[0])
                print("Patient Name -", patient[1])
                print("Age -", patient[2])
                print("Gender -", patient[3])
                print("Diagnosis -", patient[4])
                print("Bed Number -", patient[5])
                break
        file.close()
        if found:
            break
        print("Patient not found. Enter a valid Patient ID.",)

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
      patient_id = input("Enter Patient ID : ")
      patients = []
      found = False
      file = open("patients.csv", "r")
      for line in file:
             patient = line.split(",")
             if patient[0]==patient_id:
              found = True
              print("Found")
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
              choice = int(input("Enter Your Choice : "))
              if choice == 1:
                    print("Edit Name")
                    new_name = input("New Name : ")
                    patient[1] = new_name
                    print("Updated")
              elif choice == 2:
                     new_age= input("Enter New Age : ")
                     patient[2] = new_age
                     print("Updated")

              elif choice == 3:
                    new_diagnosis = input("Enter New Diagnosis : ")
                    patient[4] = new_diagnosis
                    print("Updated")

              elif choice == 4:
                    new_bed = input("Enter New Bed Number : ")
                    patient[5] = new_bed  
                    print("Updated")   
              else:
                    print("Invalid choice")
             patients.append(patient)
      if found == False:
                 print("Patient Not Found")
                 return
      file = open("patients.csv", "w")

      for patient in patients:
             file.write(",".join(patient) + "\n")

      file.close()
      print("Patient Details Updated Successfully")
def delete_patient():
      print("\n---Delete Patient---")
      patient_id = input("Enter Patient ID : ").strip().upper()
      patients = []
      file = open("patients.csv", "r")
      found = False
      for line in file:
        patient = line.split(",")
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
            confirm = int(input("\nAre you sure you want to delete? : "))
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
    print("\n--- ICU Patient Assessment ---")

    patient_id = input("Enter Patient ID : ")

    systolic = int(input("Enter Systolic BP : "))
    diastolic = int(input("Enter Diastolic BP : "))
    bp_status = assess_blood_pressure(systolic, diastolic)
    print("Blood Pressure :", bp_status)

    while True:
         spo2 = int(input("Enter SpO2 : "))
         if 0 <= spo2 <= 100:
             break
         print("Invalid SpO2. Enter a value between 0 and 100.")
    spo2_status = assess_spo2(spo2)
    print("SpO2 :", spo2_status)

    while True:
         heart_rate = int(input("Enter Heart Rate : "))

         if 30 <= heart_rate <= 220:
              break
         print("Invalid Heart Rate. Enter a value between 30 and 220.")
    heart_rate_status = assess_heart_rate(heart_rate)
    print("Heart Rate :", heart_rate_status)

    while True:
        temperature = float(input("Enter Temperature (°C) : "))
        if 25 <= temperature <= 45:
             break
    print("Invalid Temperature. Enter a value between 25°C and 45°C.")
    temperature_status = assess_temperature(temperature)
    print("Temperature :", temperature_status)

    while True:
         respiratory_rate = int(input("Enter Respiratory Rate : "))
         if 5 <= respiratory_rate <= 60:
              break
    print("Invalid Respiratory Rate. Enter a value between 5 and 60.")
    respiratory_rate_status = assess_respiratory_rate(respiratory_rate)
    print("Respiratory rate :", respiratory_rate_status)

    risk_score = 0

    if bp_status == "LOW" or bp_status == "HIGH":
        risk_score = risk_score + 1

    if spo2_status == "LOW":
        risk_score = risk_score + 1
    elif spo2_status == "VERY LOW":
        risk_score = risk_score + 2

    if heart_rate_status == "LOW" or heart_rate_status == "HIGH":
        risk_score = risk_score + 1

    if temperature_status == "LOW" or temperature_status == "HIGH":
        risk_score = risk_score + 1

    if respiratory_rate_status == "LOW" or respiratory_rate_status == "HIGH":
        risk_score = risk_score + 1
    print("\nRisk Score :", risk_score)
    if risk_score == 0:
        overall_status = "NORMAL"

    elif risk_score <= 2:
        overall_status = "NEEDS ATTENTION"

    else:
        overall_status = "CRITICAL"

    print("Overall Patient Status :", overall_status)
    file = open("assessments.csv", "a")

    file.write(patient_id + "," + str(systolic) + "," + str(diastolic) + "," + str(spo2) + "," + str(heart_rate) + "," +
    str(temperature) + "," + str(respiratory_rate) + "," + str(risk_score) + "," + overall_status + "\n")

    file.close()

    print("Assessment Saved Successfully")

def view_assessments():
    print("\nView Assessment")
    print("_"* 20)
    file = open("assessments.csv", "r")
    patient_id = input("Enter Patient ID : ")
    found = False
    for line in file:
        patient_assess = line.split(",")
        if patient_assess[0] == patient_id:
            found=True
            print("\nPatient Assessment")
            print("Patient ID       :", patient_assess[0])
            print("Systolic BP      :", patient_assess[1])
            print("Diastolic BP     :", patient_assess[2])
            print("SpO2             :", patient_assess[3])
            print("Heart Rate       :", patient_assess[4])
            print("Temperature      :", patient_assess[5])
            print("Respiratory Rate :", patient_assess[6])
            print("Risk Score       :", patient_assess[7])
            print("Overall Status   :", patient_assess[8])
    file.close()
    if found == False:
         print("Patient not found")
         return
def patient_priority():
         print("\n--- ICU Patient Priority ---")
         file = open("assessments.csv", "r")
         patients = []
         for line in file:
              patient_assess = line.strip().split(",")
              patient_id = patient_assess[0]
              risk_score = int(patient_assess[7])
              overall_status = patient_assess[8]
              patients.append([patient_id, overall_status, risk_score])
         file.close()
         patients.sort(key=lambda x: x[2], reverse=True)
         print("\nPriority Order:")
         priority = 1
         for patient in patients:
              print("Priority", priority, "→", patient[0], "-", patient[1], "-", patient[2])
              priority = priority + 1

menu()
 





