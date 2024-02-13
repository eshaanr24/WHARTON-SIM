import random

# Defined team names and their points
teams = {
    "ANC": 67, "AUG": 65, "FAR": 63, "JAC": 61, "LAR": 60, "PRO": 56, "SFS": 55,
    "LRO": 53, "OAK": 53, "SPR": 51, "DOV": 50, "SAS": 50, "LEX": 48, "TOL": 48,
    "DES": 47, "REN": 45, "BOI": 44, "EUG": 43, "BAK": 42, "FOR": 42, "CHM": 40,
    "MOB": 40, "ALB": 37, "MAN": 35, "WIC": 35, "TUC": 33, "SJU": 26, "TAC": 25
}

# Defined home advantages for each team
home_advantages = {
    "ALB": 1.375, "MOB": 1.4285714285714286, "SAS": 1.4864864864864864,
    "FAR": 1.5666666666666667, "PRO": 1.4, "SFS": 1.5294117647058822,
    "SPR": 1.5151515151515151, "ANC": 1.7307692307692308, "TAC": 1.3125,
    "TUC": 1.4444444444444444, "DOV": 1.5384615384615383, "AUG": 1.6538461538461537,
    "EUG": 1.3461538461538463, "JAC": 1.72, "FOR": 1.3333333333333333,
    "BAK": 1.5, "LAR": 1.7096774193548387, "BOI": 1.5769230769230769,
    "CHM": 1.44, "LEX": 1.5517241379310345, "SJU": 1.4666666666666668,
    "DES": 1.5161290322580645, "TOL": 1.3333333333333333, "MAN": 1.3181818181818181,
    "OAK": 1.5925925925925926, "WIC": 1.5, "REN": 1.53125, "LRO": 1.56
}

# Defined group stage matchups
matches = [
    "Group1_Game1,ANC,LEX", "Group1_Game2,DOV,TAC", "Group1_Game3,TAC,ANC",
    "Group1_Game4,DOV,LEX", "Group1_Game5,ANC,DOV", "Group1_Game6,LEX,TAC",
    "Group2_Game1,FAR,TOL", "Group2_Game2,SPR,TUC", "Group2_Game3,TUC,FAR",
    "Group2_Game4,SPR,TOL", "Group2_Game5,FAR,SPR", "Group2_Game6,TOL,TUC",
    "Group3_Game1,SFS,DES", "Group3_Game2,LRO,WIC", "Group3_Game3,WIC,SFS",
    "Group3_Game4,LRO,DES", "Group3_Game5,SFS,LRO", "Group3_Game6,DES,WIC",
    "Group4_Game1,PRO,CHM", "Group4_Game2,OAK,ALB", "Group4_Game3,ALB,PRO",
    "Group4_Game4,OAK,CHM", "Group4_Game5,PRO,OAK", "Group4_Game6,CHM,ALB",
    "Group5_Game1,LAR,FOR", "Group5_Game2,SAS,MOB", "Group5_Game3,MOB,LAR",
    "Group5_Game4,SAS,FOR", "Group5_Game5,LAR,SAS", "Group5_Game6,FOR,MOB",
    "Group6_Game1,JAC,BAK", "Group6_Game2,REN,MAN", "Group6_Game3,MAN,JAC",
    "Group6_Game4,REN,BAK", "Group6_Game5,JAC,REN", "Group6_Game6,BAK,MAN",
    "Group7_Game1,AUG,EUG", "Group7_Game2,BOI,SJU", "Group7_Game3,SJU,AUG",
    "Group7_Game4,BOI,EUG", "Group7_Game5,AUG,BOI", "Group7_Game6,EUG,SJU"
]

# Function to simulate a match with home advantage
def simulate_match(home, away, home_advantage):
    home_score = random.gauss(home * home_advantage, 3)
    away_score = random.gauss(away, 3)
    if home_score > away_score:
        return 1  # Home team wins
    elif home_score < away_score:
        return -1  # Away team wins
    else:
        return 0  # Draw

# Simulated group stage matches
for match in matches:
    group, home, away = match.split(',')
    group_num = int(group.split('_')[0].replace('Group', ''))
    home_points = teams[home]
    away_points = teams[away]
    home_advantage = home_advantages.get(home, 1)
    result = simulate_match(home_points, away_points, home_advantage)
    if result == 1:
        print(f"{home} defeats {away} in Group {group_num} match")
    elif result == -1:
        print(f"{away} defeats {home} in Group {group_num} match")
    else:
        print(f"{home} and {away} draw in Group {group_num} match")
