budget_prompt = f"""
You are a travel budget expert.

Estimate the average daily travel cost for the following trip.

Destination: {destination}
Budget Level: {budget}

Rules:
- Use the local currency of the destination.
- Consider accommodation, food, local transportation, and sightseeing.
- Return only the estimated daily budget.
- Example:
  Nepal (Mid): NPR 7,000 - NPR 15,000 per day
  Japan (Luxury): ¥30,000 - ¥60,000 per day
  France (Budget): €60 - €100 per day
"""

daily_budget = llm.invoke(
    [HumanMessage(content=budget_prompt)]
).content