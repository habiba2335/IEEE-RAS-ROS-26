def analyze_grades(grades_list):
    if len(grades_list) == 0:
        return {}
        
    average = sum(grades_list) / len(grades_list)
    highest = max(grades_list)
    lowest = min(grades_list)
    
    return {"average": average, "highest": highest, "lowest": lowest}