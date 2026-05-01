def filter_project(score, activity):
    if score > 5 and activity == "high":
        return "high priority"
    return "low priority"
