# Head-to-Head Voting Algorithm

def head_to_head_voting(results):
    """ Calculate team rankings based on head-to-head match results.
    
    Parameters:
    results (dict): A dictionary where keys are team names and values are lists of tuples (opponent, outcome).
                    Outcome is 1 if the team won the match against the opponent, otherwise 0.

    Returns:
    list: Ranked list of teams based on number of wins.
    """
    win_counts = {team: 0 for team in results.keys()}

    for team, matches in results.items():
        for opponent, outcome in matches:
            if outcome == 1:
                win_counts[team] += 1

    # Sort teams by win counts
    ranked_teams = sorted(win_counts.items(), key=lambda item: item[1], reverse=True)
    return ranked_teams

# Example usage
if __name__ == '__main__':
    # Define results for 30 teams
    match_results = {
        'Team A': [('Team B', 1), ('Team C', 0), ('Team D', 1)],
        'Team B': [('Team A', 0), ('Team C', 1), ('Team D', 1)],
        'Team C': [('Team A', 1), ('Team B', 0), ('Team D', 1)],
        'Team D': [('Team A', 0), ('Team B', 0), ('Team C', 0)],
        # ... add results for remaining teams up to Team Z
    }

    rankings = head_to_head_voting(match_results)
    for team, wins in rankings:
        print(f'{team}: {wins} wins')