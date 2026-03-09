def recommend_by_branch(branch):

    branch = branch.lower()

    if "cse" in branch or "computer" in branch:
        return "Best colleges for Computer Science: VNIT, Ramdeobaba, YCCE"

    elif "ai" in branch or "artificial intelligence" in branch:
        return "Best colleges for Artificial Intelligence: VNIT, SB Jain"

    elif "mechanical" in branch:
        return "Best colleges for Mechanical Engineering: YCCE, GCOE, Raisoni"

    elif "civil" in branch:
        return "Best colleges for Civil Engineering: GCOE, Ramdeobaba"

    elif "electrical" in branch:
        return "Best colleges for Electrical Engineering: VNIT, YCCE"

    else:
        return "Please ask about branches like CSE, AI, Mechanical, Civil or Electrical."