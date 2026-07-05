from langchain.tools import tool

@tool
def budget_calculator(level: str) -> str:
    """Returns estimated daily travel budget in Nepalese Rupees (NPR)."""

    level = level.lower().strip()

    if level == "budget":
        return "NPR 3,000 - NPR 7,000 per day"

    elif level == "mid":
        return "NPR 7,000 - NPR 15,000 per day"

    elif level == "luxury":
        return "NPR 15,000+ per day"

    else:
        return "Please choose one of: Budget, Mid, or Luxury."