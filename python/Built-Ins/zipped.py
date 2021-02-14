"""
www.hackerrank.com/challenges/zipped/
github.com/ander758/HackerRank

Get average of each scores from every person using zip
"""

length, n = 5, 3
arr = [
    ['89', '90', '78', '93', '80'],
    ['90', '91', '85', '88', '86'],
    ['91', '92', '83', '89', '90.5']]

tuple_scores = list(zip(*arr))
for scores in tuple_scores:
    sum_scores = 0
    for score in scores:
        sum_scores += float(score)
    print(sum_scores / n)
