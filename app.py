from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

from tools import budget_calculator

# Load environment variables from .env
load_dotenv()

# ChatGroq automatically uses GROQ_API_KEY from .env
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
)

print("=" * 50)
print("AI Travel Planner")
print("=" * 50)

destination = input("Enter Destination: ")
days = input("Enter Number of Days: ")
budget = input("Enter Budget (Budget/Mid/Luxury): ")
style = input("Enter Travel Style (Adventure/Luxury/Family/Solo): ")
interest = input("Enter Interests: ")

daily_budget = budget_calculator.invoke(budget)

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

response = llm.invoke([HumanMessage(content=prompt)])
travel_plan = response.content

print("\nTRAVEL PLAN\n")
print(travel_plan)

print("\nDAILY BUDGET\n")
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
  "info": "A paragraph describing the travel plan including itinerary, hotels, food, transport, safety, and budget."
}}

Return ONLY JSON.
"""

json_response = llm.invoke([HumanMessage(content=second_prompt)])

print("\nJSON OUTPUT\n")
print(json_response.content)