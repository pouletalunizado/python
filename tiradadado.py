
import random
def random_dice():
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return die1 + die2

print "Sum of two random dice, rolled once:", random_dice()
print "Sum of two random dice, rolled again:", random_dice()
print "Sum of two random dice, rolled again:", random_dice()