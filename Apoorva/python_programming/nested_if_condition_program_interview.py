round1 = "clear1"
round2 = "clear2"
round3 = "not_clear3"

if round1 == "clear1":
    print("Candidate has cleared 1st round")
    if round2 == "clear2":
        print("Candidate has cleared 2nd round")
        if round3 == "clear3":
            print("Candidate has cleared 3rd round. Congratulations,you are hired.")
        else:
            print("Candidate has not cleared 3rd round")
    else:
        print("Candidate has not cleared 2nd round")
else:
    print("Candidate has not cleared 1st round")



