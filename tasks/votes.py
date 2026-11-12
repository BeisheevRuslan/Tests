def vote(votes):
    max_count = 0
    winner = None
    set_votes = set(votes)

    for v in set_votes:
        count = votes.count(v)
        if count > max_count:
            max_count = count
            winner = v

    return winner


if __name__ == '__main__':
    """
    1
    2
    """
    print(vote([1, 1, 1, 2, 3]))
    print(vote([1, 2, 3, 2, 2]))
