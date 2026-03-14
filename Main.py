from lead_finder import find_leads
from lead_analyzer import analyze_lead
from outreach_agent import generate_message
import pandas as pd

url = "https://www.python.org"

leads = find_leads(url)

data = []

for lead in leads:

    result = analyze_lead(lead)
    message = generate_message(lead)

    data.append({
        "Lead": lead,
        "Score": result,
        "Message": message
    })

df = pd.DataFrame(data)

df.to_csv("leads.csv", index=False)

print("Leads saved to leads.csv")