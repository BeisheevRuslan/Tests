def vote(votes):
    max_count = 0
    winner = None
    winners_count = 0
    set_votes = set(votes)

    for v in set_votes:
        count = votes.count(v)
        if count > max_count:
            max_count = count
            winner = v

    for c in set_votes:
        if votes.count(c) == max_count:
            winners_count += 1
    if winners_count > 1:
        return 'Нужен второй тур выборов'
    else:
        return winner


if __name__ == '__main__':
    """
    1
    2
    """
    print(vote([1, 1, 1, 2, 3]))
    print(vote([1, 2, 3, 2, 2]))
    print(vote([3, 3, 3, 2, 2, 2]))
