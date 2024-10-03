# Interview process demonstration using nested if conditions
"""
# with elif
rusume_round = int(input("Resume score: "))
tech_score = int(input("Enter technical interview score: "))
hr_score = int(input("Enter HR interview score: "))

# Step 1: Resume selection
if rusume_round >= 80:
    print("Resume selection: Passed")

elif tech_score > 70:
        print("Technical Interview: Pass")
        print("Sorry, you did not pass the technical interview.")

# Step 2: HR Interview
elif hr_score >= 80:
        print("HR Interview: Failed")
        print("Congratulations! You have been selected for the job.")
# Final Success Case
else:
    print("Resume selection: Failed")
    print("Technical Interview: Failed")
    print("HR Interview: Failed")
"""


# with nested
rusume_round = int(input("Resume score: "))
tech_score = int(input("Enter technical interview score: "))
hr_score = int(input("Enter HR interview score: "))

# Interview
if rusume_round >= 90:  # Passed technical interview
    print("Resume is eligible: Passed")

    # Nested if for Technical Round
    if tech_score >= 70:
        print("Technical interview: Passed")
    else:
        print("Technical Interview: Failed")
        print("Sorry, you did not pass the Technical interview.")


    # Nested if for HR interview
    if hr_score >= 90:
        print("HR Interview: Passed")
        print("Congratulations! You have been selected for the job.")
    else:
        print("HR Interview: Failed")
        print("Sorry, you did not pass the HR interview.")
else:
    print("Resume is not eligible: Failed")
    print("Sorry, you did not pass the technical interview.")

