#review 
#python-i day2.py
def read_scores():
    scores = []

    while True:
        score = raw_input("Enter a score> ")
        if len(score) == 0:
            return scores
        
        score = int(score)
        if score < 1 or score > 10:
            print("Score must be between 1 and 10")
        else:
            scores.append(score)

def average_score(scores):
    if len(scores) > 2:
        scores.sort()
        del scores[0]
        del scores[-1]

    total = 0
    for score in scores:
        total += score

    return float(total)/len(scores)

scores = read_scores()
print("You entered: %s" % scores)
print(average_score(scores))
print("Now scores is: %s" % scores)
