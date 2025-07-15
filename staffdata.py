import pandas as pd
import json

# Load the full list of staff dictionaries from user (truncated here for demonstration)
# Assuming the variable 'data' contains the full JSON data provided by the user

# Simulate the data loaded from JSON for processing (just showing structure)
with open("staffData.json", "r") as f:
    data = json.load(f)

# Normalize all key names to match the format of Noor Aniza's entry
standardized_data = []

for entry in data:
    standardized_entry = {
        "id": entry.get("ID") or entry.get("id"),
        "name": entry.get("NAME") or entry.get("name"),
        "IC": entry.get("IC"),
        "age": entry.get("AGE") or entry.get("age"),
        "dept": entry.get("DEPT/DIV") or entry.get("dept"),
        "position": entry.get("POSITION") or entry.get("position"),
        "grade": entry.get("GRADE") or entry.get("grade"),
        "email": entry.get("EMAIL") or entry.get("email"),
        "joined": entry.get("JOINED") or entry.get("joined"),
        "level": entry.get("LEVEL") or entry.get("level"),
        "course": entry.get("COURSE") or entry.get("course"),
        "university": entry.get("UNIVERSITY/COLLEGE/SCHOOL") or entry.get("university"),
        "education": entry.get("HIGHEST EDUCATION") or entry.get("education"),
        "score2022": entry.get("Performance Appraisal 2022") or entry.get("score2022"),
        "score2023": entry.get("Performance Appraisal 2023") or entry.get("score2023"),
        "score2024": entry.get("Performance Appraisal 2024") or entry.get("score2024"),
        "promotion": entry.get("DATE OF LATEST PROMOTION") or entry.get("promotion"),
        "photo": entry.get("photo") or ""
    }
    standardized_data.append(standardized_entry)

# Save to a new JSON file
output_path = "staffData2.json"
with open(output_path, "w") as f:
    json.dump(standardized_data, f, indent=2)

output_path
