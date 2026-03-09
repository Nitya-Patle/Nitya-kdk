def recommend_course(interest):

    interest = interest.lower()

    if "coding" in interest or "programming" in interest:
        return "Recommended Course: B.Tech Computer Science"

    elif "business" in interest:
        return "Recommended Course: BBA or MBA"

    elif "design" in interest:
        return "Recommended Course: B.Des"

    elif "management" in interest:
        return "Recommended Course: BBA"

    elif "ai" in interest:
        return "Recommended Course: B.Tech Artificial Intelligence"

    else:
        return "Please consult our academic advisor for better guidance."