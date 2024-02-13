import random

# Define team names and their points
teams = {
    "ANC": 67, "AUG": 65, "FAR": 63, "JAC": 61, "LAR": 60, "PRO": 56, "SFS": 55,
    "LRO": 53, "OAK": 53, "SPR": 51, "DOV": 50, "SAS": 50, "LEX": 48, "TOL": 48,
    "DES": 47, "REN": 45, "BOI": 44, "EUG": 43, "BAK": 42, "FOR": 42, "CHM": 40,
    "MOB": 40, "ALB": 37, "MAN": 35, "WIC": 35, "TUC": 33, "SJU": 26, "TAC": 25
}

# Simulate a match
def simulate_match(home, away):
    home_score = random.gauss(home, 3)
    away_score = random.gauss(away, 3)
    if home_score > away_score:
        return 1  # Home team wins
    elif home_score < away_score:
        return -1  # Away team wins
    else:
        return 0  # Draw

# Function to calculate the probability of the stronger team winning
def calculate_probability(team_a, team_b):
    total_points = teams[team_a] + teams[team_b]
    probability_a = teams[team_a] / total_points
    return probability_a

# Define the matchups for the knockout stage (semi-finals and finals)
knockout_stage = [
    ("Semifinals_A", "DOV", "OAK"),
    ("Semifinals_B", "FOR", "AUG"),
    ("Finals_A", "DOV", "FOR"),
    ("Finals_B", "DOV", "AUG"),
    ("Finals_C", "OAK", "FOR"),
    ("Finals_D", "OAK", "AUG")
]

# Simulate the knockout stage
for match_id, team_a, team_b in knockout_stage:
    team_a_points = teams[team_a]
    team_b_points = teams[team_b]
    result = simulate_match(team_a_points, team_b_points)
    if result == 1:
        print(f"{team_a} defeats {team_b} in {match_id}")
    elif result == -1:
        print(f"{team_b} defeats {team_a} in {match_id}")
    else:
        print(f"{team_a} and {team_b} draw in {match_id}")

    # Calculate probability of stronger team (team_a) winning
    probability_a = calculate_probability(team_a, team_b)
    print(f"Probability of {team_a} winning: {probability_a:.2f}")
