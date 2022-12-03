with open('RockPaperScissors.in') as file:
    rounds = [i.replace(" ", "") for i in file.read().strip().split("\n")]
outcomes = {
    "AX":4, "AY":8, "AZ":3, 
    "BX":1, "BY":5, "BZ":9, 
    "CX":7, "CY":2, "CZ":6 
}
total_score_p1 = 0
for round in rounds:
    total_score_p1 += outcomes[round]    
wanted_outcomes = {
    "AX":3, "AY":4, "AZ":8, 
    "BX":1, "BY":5, "BZ":9, 
    "CX":2, "CY":6, "CZ":7 
}
total_score_p2 = 0
for round in rounds:
    total_score_p2 += wanted_outcomes[round]
print("Part 1 answer: ", total_score_p1)
print("Part 2 answer: ", total_score_p2)
