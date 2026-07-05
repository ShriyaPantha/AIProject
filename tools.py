from langchain.tools import tool

@tool
def budget_calculator(level: str) -> str:
    """Returns estimated daily travel budget."""

    level = level.lower()

    if level == "budget":
        return "$50 - $100 per day"

    elif level == "mid":
        return "$100 - $250 per day"

    elif level == "luxury":
        return "$250+ per day"

    else:
        return "Please choose Budget, Mid, or Luxury."