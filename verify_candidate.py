import json
import re
from rapidfuzz import fuzz

# Hardcoded candidate claim
with open("candidate_claim.json", "r", encoding="utf-8") as f:
    candidate = json.load(f)


# Load manually collected LinkedIn data
with open("linkedin_profile.json", "r", encoding="utf-8") as f:
    linkedin = json.load(f)
    verification_result = {
  
}
    with open("verification_result.json", "w", encoding="utf-8") as f:
     json.dump(verification_result, f, indent=4)

print("Verification result saved to verification_result.json")
    
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

start_score, start_status = compare_field(
    candidate["start_date"],
    linkedin["start_date"]
)

end_score, end_status = compare_field(
    candidate["end_date"],
    linkedin["end_date"]
)
statuses = [
    company_status,
    title_status,
    start_status,
    end_status
]

if all(status == "Verified" for status in statuses):
    overall = "VERIFIED"
elif "Mismatch" in statuses:
    overall = "NOT VERIFIED"
else:
    overall = "PARTIALLY VERIFIED"

if company_status == "Verified" and title_status == "Verified":
    overall = "VERIFIED"
else:
    overall = "NOT VERIFIED"

print("\n candidateclaim:")
print(candidate)

print("\nLinkedIn data:")
print(linkedin)

print("\nVerification Results")
print("-" * 20)
print(f"Title       : {title_status} ({title_score:.1f})")
print(f"Company : {company_status} ({company_score:.1f})")
print(f"\nOverall Status: {overall}")
print("=" * 60)