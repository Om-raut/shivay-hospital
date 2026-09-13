import json
from datetime import date


# ----------------------------------------
# LOAD VACCINE REMINDERS
# ----------------------------------------

file_name = "vaccine-reminders.json"

try:
    with open(file_name, "r", encoding="utf-8") as file:
        reminders = json.load(file)

except FileNotFoundError:
    print("ERROR: vaccine-reminders.json not found!")
    exit()

except json.JSONDecodeError:
    print("ERROR: vaccine-reminders.json contains invalid JSON!")
    exit()


# ----------------------------------------
# TODAY'S DATE
# ----------------------------------------

today = date.today().isoformat()

print("----------------------------------")
print("VACCINE REMINDER CHECKER")
print("----------------------------------")
print("Today's date:", today)
print()


# ----------------------------------------
# CHECK VACCINE DATES
# ----------------------------------------

due_count = 0

for reminder in reminders:

    next_dose_date = reminder.get("nextDoseDate")

    if next_dose_date == today:

        due_count += 1

        patient = reminder.get("patientName")
        parent = reminder.get("parentName")
        mobile = reminder.get("mobileNumber")
        vaccine = reminder.get("vaccineName")

        # --------------------------------
        # CHILD MESSAGE
        # --------------------------------

        child_message = f"""
Hello {patient},

Your {vaccine} vaccine dose is due today ({today}).

Please contact Shivay Mother and Child Health Clinic.
"""

        # --------------------------------
        # PARENT MESSAGE
        # --------------------------------

        parent_message = f"""
Dear {parent},

Your child's {vaccine} vaccine dose is due today ({today}).

Please contact Shivay Mother and Child Health Clinic.
"""

        # --------------------------------
        # DOCTOR MESSAGE
        # --------------------------------

        doctor_message = f"""
Doctor Reminder:

Patient: {patient}
Vaccine: {vaccine}
Dose Date: {today}

The patient's vaccine dose is due today.
"""


        print("🔔 VACCINE DUE TODAY")
        print("----------------------------------")

        print("Patient:", patient)
        print("Parent:", parent)
        print("Mobile:", mobile)
        print("Vaccine:", vaccine)
        print("Next Dose:", next_dose_date)

        print()
        print("👶 CHILD REMINDER")
        print(child_message)

        print("👨‍👩‍👧 PARENT REMINDER")
        print(parent_message)

        print("👨‍⚕️ DOCTOR REMINDER")
        print(doctor_message)

        print("----------------------------------")


# ----------------------------------------
# NO REMINDERS
# ----------------------------------------

if due_count == 0:
    print("No vaccine doses are due today.")


print()
print("VACCINE CHECKER FINISHED")
