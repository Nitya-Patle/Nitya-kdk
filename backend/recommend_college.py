import json

# load college database
with open("colleges.json") as file:
    data = json.load(file)

def recommend_college(marks):

    marks = int(marks)

    if marks >= 90:
        return "Recommended Colleges: VNIT, Ramdeobaba"

    elif marks >= 80:
        return "Recommended Colleges: YCCE, Raisoni"

    elif marks >= 70:
        return "Recommended Colleges: SB Jain, GCOE"

    elif marks >= 60:
        return "Recommended Colleges: JD College, Gurunanak"
    elif marks >= 50:
        return "Recommended Colleges: Wainganga College"

    else:
        return "Recommended Colleges: KDK College, Jhulelal Institute"