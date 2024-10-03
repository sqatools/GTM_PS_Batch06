# Interview process demonstration using nested if conditions
"""
# with elif
tech_score = int(input("Enter technical interview score (out of 100): "))
hr_score = int(input("Enter HR interview score (out of 100): "))

# Step 1: Technical Interview
if tech_score < 70:
    print("Technical Interview: Failed")
    print("Sorry, you did not pass the technical interview.")

# Step 2: HR Interview
elif hr_score < 60:
    print("Technical Interview: Passed")
    print("HR Interview: Failed")
    print("Sorry, you did not pass the HR interview.")

# Final Success Case
else:
    print("Technical Interview: Passed")
    print("HR Interview: Passed")
    print("Congratulations! You have been selected for the job.")
"""


# with nested
rusume_round = int(input("Resume score: "))
tech_score = int(input("Enter technical interview score: "))
hr_score = int(input("Enter HR interview score: "))

# Step 1: Technical Interview
if rusume_round >= 90:  # Passed technical interview
    print("Resume is eligible: Passed")

    # Technical score interview
    if tech_score >= 60:  # Passed HR interview
        print("Technical interview: Passed")
        print("Congratulations! You have been passed .")
    else:
        print("HR Interview: Failed")
        print("Sorry, you did not pass the HR interview.")


    # Nested if for HR interview
    if hr_score >= 60:  # Passed HR interview
        print("HR Interview: Passed")
        print("Congratulations! You have been selected for the job.")
    else:
        print("HR Interview: Failed")
        print("Sorry, you did not pass the HR interview.")
else:
    print("Resume is not eligible: Failed")
    print("Sorry, you did not pass the technical interview.")

