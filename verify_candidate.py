import json

# Hardcoded candidate claim
candidate = {
    "name": "Oladokun Olaoluwa",
    "employer": "JobsEden",
    "title": "Software Engineering Intern",
    "start_date": "2026-03-09",
    "end_date": "Present"
}

# Load manually collected LinkedIn data
with open("linkedin_profile.json", "r", encoding="utf-8") as f:
    linkedin = json.load(f)

print("Candidate claim:")
print(candidate)

print("\nLinkedIn data:")
print(linkedin)