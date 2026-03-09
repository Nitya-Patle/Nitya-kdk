import json

# load college data
with open("colleges.json") as file:
    colleges_data = json.load(file)

def get_chatbot_response(message):

    message = message.lower()

    for college in colleges_data["colleges"]:

        if college["name"].lower() in message:

            return f"""
College Name: {college['full_name']}
Location: {college['location']}
Courses: {college['courses']}
Placements: {college['placements']}
Hostel: {college['hostel']}
"""

    return "Please ask about YCCE, VNIT, Raisoni or Priyadarshini College."