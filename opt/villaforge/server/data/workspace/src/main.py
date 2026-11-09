import os

def check_token_budget():
    budget = os.getenv('TOKEN_BUDGET', 0)
    if int(budget) <= 0:
        raise Exception('Token budget exceeded')

# Call this function at the start of your CI/CD pipeline
check_token_budget()