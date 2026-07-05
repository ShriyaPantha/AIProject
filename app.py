from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",

)

print("AI Travel Planner")

destination = input("Enter Destination: ")
days = input("Enter Number of Days: ")
budget = input("Enter Budget (low Budget/Mid/Luxury): ")
style = input("Enter Travel Style (Adventure/Luxury/Family/Solo): ")
interest = input("Enter Interests: ")


budget_prompt = f"""
You are a travel budget expert.

Estimate the average daily travel cost.

Destination: {destination}
Budget Level: {budget}

Rules:
- Use the local currency of the destination.
- Consider hotel, food, local transport and sightseeing.
- Return ONLY the estimated daily budget.
- Examples:
  Nepal (Mid): NPR 7,000 - NPR 15,000 per day
  Japan (Luxury): ¥30,000 - ¥60,000 per day
  France (Budget): €60 - €100 per day
"""

daily_budget = llm.invoke(
    [HumanMessage(content=budget_prompt)]
).content.strip()


prompt = f"""
You are an expert AI Travel Planner.

Create a detailed travel plan.

Destination: {destination}
Duration: {days} days
Budget Level: {budget}
Estimated Daily Budget: {daily_budget}
Travel Style: {style}
Interests: {interest}

Include:

1. Day-wise itinerary
2. Recommended hotels
3. Food recommendations
4. Local transport
5. Estimated total budget
6. Packing list
7. Safety tips

Return the answer in clean markdown.
"""

print("\nGenerating your travel plan...\n")

response = llm.invoke(
    [HumanMessage(content=prompt)]
)

travel_plan = response.content

print("\n TRAVEL PLAN \n")
print(travel_plan)

print("\n DAILY BUDGET \n")
print(daily_budget)


second_prompt = f"""
Based on the generated travel plan below, generate ONLY valid JSON.

Travel Plan:
{travel_plan}

Return the JSON in this format:

{{
  "destination": "{destination}",
  "duration": "{days} days",
  "budget_level": "{budget}",
  "daily_budget": "{daily_budget}",
  "summary": [
    "Point 1",
    "Point 2",
    "Point 3",
    "Point 4",
    "Point 5"
  ],
  "info": "A paragraph describing the complete travel plan including itinerary, hotels, food, transport, safety and budget."
}}

Return ONLY JSON.
"""

json_response = llm.invoke(
    [HumanMessage(content=second_prompt)]
)

print("\n JSON OUTPUT \n")
print(json_response.content)