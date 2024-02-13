import random

# Define team names and their points
teams = {
    "ANC": 67, "AUG": 65, "FAR": 63, "JAC": 61, "LAR": 60, "PRO": 56, "SFS": 55,
    "LRO": 53, "OAK": 53, "SPR": 51, "DOV": 50, "SAS": 50, "LEX": 48, "TOL": 48,
    "DES": 47, "REN": 45, "BOI": 44, "EUG": 43, "BAK": 42, "FOR": 42, "CHM": 40,
    "MOB": 40, "ALB": 37, "MAN": 35, "WIC": 35, "TUC": 33, "SJU": 26, "TAC": 25
}

# Define group stage matchups
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

# Function to simulate a match
def simulate_match(home, away):
    home_advantage = 1.69  # Adjust this factor for home team advantage
    home_score = random.gauss(home * home_advantage, 3)
    away_score = random.gauss(away, 3)
    if home_score > away_score:
        return 1  # Home team wins
    elif home_score < away_score:
        return -1  # Away team wins
    else:
        return 0  # Draw

# Simulate group stage matches
for match in matches:
    group, home, away = match.split(',')
    group_num = int(group.split('_')[0].replace('Group', ''))
    home_points = teams[home]
    away_points = teams[away]
    result = simulate_match(home_points, away_points)
    if result == 1:
        print(f"{home} defeats {away} in Group {group_num} match")
    elif result == -1:
        print(f"{away} defeats {home} in Group {group_num} match")
    else:
        print(f"{home} and {away} draw in Group {group_num} match")

# No need to calculate standings or print them for individual matchups

# Proceed to calculate overall standings and knockout stages
# Implement this part based on the overall group standings if needed



