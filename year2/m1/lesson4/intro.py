# 1. High-quality, seamless code: clean structure, comments, naming
minecraft_players = {
    'Steve': [
        {'SurvivalWorld': {'PlayerKills': 87, 'Level': 92}},
        {'NetherQuest': {'BlazeFarm': 79, 'NetherEntered': 5}}
    ],
    'Alex': [
        {'SurvivalWorld': {'PlayerKills': 91, 'Level': 95}},
        {'NetherQuest': {'BlazeFarm': 85, 'NetherEntered': 8}}
    ]
}

# 2. Nested structures: dict > list > dict > dict

# 3. Access a deep nested object (Alex's score for NetherEntered in NetherQuest)
alex_nether_score = minecraft_players['Alex'][1]['NetherQuest']['NetherEntered']
print('Alex\'s score in NetherEntered:', alex_nether_score)

# 4. Applying methods to nested structures
# Calculate average score for SurvivalWorld builds for each player
for player, worlds in minecraft_players.items():
    for world in worlds:
        if 'SurvivalWorld' in world:
            scores = world['SurvivalWorld'].values()
            avg_score = sum(scores) / len(scores)
            print(f'{player}\'s average in SurvivalWorld: {avg_score:.1f}')

# 5. Solving a more complex problem:
# Find the top Minecraft player based on total score across all builds/challenges
top_player = None
highest_total = 0

for player, worlds in minecraft_players.items():
    total = 0
    count = 0
    for world in worlds:
        for world_name, challenges in world.items():
            total += sum(challenges.values())
            count += len(challenges)
    avg = total / count
    print(f'{player}\'s average across all Minecraft worlds: {avg:.1f}')
    if total > highest_total:
        highest_total = total
        top_player = player

print('🏆 Top Minecraft builder:', top_player, 'with total score:', highest_total)
