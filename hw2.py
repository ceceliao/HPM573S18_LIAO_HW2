Constant = 0.371
healthscale = {'vision':     [1, 0.98, 0.89, 0.84, 0.75, 0.61],
               'hearing':    [1, 0.95, 0.89, 0.80, 0.74, 0.61],
               'speech':     [1, 0.94, 0.89, 0.81, 0.68],
               'ambulation': [1, 0.93, 0.86, 0.73, 0.65, 0.58],
               'dexterity':  [1, 0.95, 0.88, 0.76, 0.65, 0.56],
               'emotion':    [1, 0.95, 0.88, 0.76, 0.65, 0.58],
               'cognition':  [1, 0.92, 0.95, 0.83, 0.60, 0.42],
               'pain':       [1, 0.96, 0.90, 0.88, 0.55]};


def get_score(vision, hearing, speech, ambulation, dexterity, emotion, cognition, pain):
    if not (vision in [1, 2, 3, 4, 5, 6]):
        raise ValueError ('vision value can only take 1, 2, 3, 4, 5, 6')
    if not (hearing in [1, 2, 3, 4, 5, 6]):
        raise ValueError ('hearing value can only take 1, 2, 3, 4, 5, 6')
    if not (speech in [1, 2, 3, 4, 5, 6]):
        raise ValueError ('speech value can only take 1, 2, 3, 4, 5, 6')
    if not (ambulation in [1, 2, 3, 4, 5, 6]):
        raise ValueError ('ambulation value can only take 1, 2, 3, 4, 5, 6')
    if not (dexterity in [1, 2, 3, 4, 5, 6]):
        raise ValueError ('dexterity value can only take 1, 2, 3, 4, 5, 6')
    if not (emotion in [1, 2, 3, 4, 5, 6]):
        raise ValueError ('emotion value can only take 1, 2, 3, 4, 5, 6')
    if not (cognition in [1, 2, 3, 4, 5, 6]):
        raise ValueError ('cognition value can only take 1, 2, 3, 4, 5, 6')
    if not (pain in [1, 2, 3, 4, 5, 6]):
        raise ValueError ('pain value can only take 1, 2, 3, 4, 5, 6')
    score = 1.371


    score *=healthscale['vision'][vision-1]
    score *=healthscale['hearing'][hearing-1]
    score *=healthscale['speech'][speech-1]
    score *=healthscale['ambulation'][ambulation-1]
    score *=healthscale['dexterity'][dexterity-1]
    score *=healthscale['emotion'][emotion-1]
    score *=healthscale['cognition'][cognition-1]
    score *=healthscale['pain'][pain-1]
    score -= 0.371

    return score


