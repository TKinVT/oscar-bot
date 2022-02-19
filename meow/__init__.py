import random

sayings = {
    # Things Oscar would say, and how often on a scale of 1 - 10
    "Mrrrowwww": 5,
    "Prow?": 7,
    "Prrrrrr": 5,
    "Mrow": 5,
    ":cat:": 1,
    ":pouting_cat:": 1,
    "MrrRrr": 3
}

weighted_sayings = [saying for saying in sayings for occurrence in range(sayings[saying])]


def meow():
    return random.choice(weighted_sayings)
