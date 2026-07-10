import json
import re
from rapidfuzz import fuzz

# Hardcoded candidate claim
with open("candidate_claim.json", "r", encoding="utf-8") as f:
    candidate = json.load(f)


# Load manually collected LinkedIn data
with open("linkedin_profile.json", "r", encoding="utf-8") as f:
    linkedin = json.load(f)
    
def normalize(text: str | None) -> str:
    if text is None:
        return ""
    
    text = text.lower().strip()
    text = re.sub(r"\s+", " ", text)

    replacements = {
        "inc.": "",
        "limited": "ltd",
        "corporation": "corp",
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text


def compare_field(candidate_value: str, linkedin_value: str):
    score = fuzz.token_sort_ratio(
        normalize(candidate_value),
              normalize(linkedin_value)
    )

    if score >= 90:
        status = "Verified"
    elif score >= 70:
        status = "Possible Match"
    else:
        status = "Mismatch"

    return score, status
company_score, company_status = compare_field(
    candidate["employer"],
    linkedin["employer"]
)

title_score, title_status = compare_field(
    candidate["title"],
    linkedin["title"]
)

print("\n claim:")
print(candidate)

print("\nLinkedIn data:")
print(linkedin)

print("\nVerification Results")
print("---------------------")

print(f"Company : {company_status} ({company_score:.1f})")
print(f"Title   : {title_status} ({title_score:.1f})")