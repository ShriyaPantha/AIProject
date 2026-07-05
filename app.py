import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, AgentType

from tools import budget_calculator

# Load .env
load_dotenv()

# Create LLM
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile",
    temperature=0.7
)

# Create Agent
agent = initialize_agent(
    tools=[budget_calculator],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

print("=" * 50)
print("🌍 AI Travel Planner")
print("=" * 50)

# User Input
destination = input("Enter Destination: ")
days = input("Enter Number of Days: ")
budget = input("Enter Budget (Budget/Mid/Luxury): ")
style = input("Enter Travel Style (Adventure/Luxury/Family/Solo): ")
interest = input("Enter Interests: ")

prompt = f"""
Plan a {days}-day trip to {destination}.

Budget: {budget}

Travel Style: {style}

Interests: {interest}

Include:

1. Day-wise itinerary
2. Hotels
3. Food recommendations
4. Local transport
5. Estimated budget
6. Packing list
7. Safety tips
"""

print("\nGenerating your travel plan...\n")

response = agent.run(prompt)

print("\n========== TRAVEL PLAN ==========\n")
print(response)

print("\n========== DAILY BUDGET ==========\n")
print(budget_calculator.invoke(budget))