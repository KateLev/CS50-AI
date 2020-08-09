from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# common rules
rules = And()   

def gameRules(symbols):
    n = len(symbols)
    i = 0
    
    # person can be only a knight or a knave   
    while i < n:
        a = symbols[i]
        b = symbols[i+1]
        rules.add(Or(a, b))
        rules.add(Not(And(a, b)))
        i += 2    
   

# Puzzle 0
# A says "I am both a knight and a knave."

SentensesA = And(AKnight, AKnave)
knowledge0 = And( 
    rules,
    Or(SentensesA, Not(SentensesA)),
    Biconditional(SentensesA, AKnight),
    Biconditional(Not(SentensesA), AKnave))  


# Puzzle 1
# A says "We are both knaves."
# B says nothing.

SentensesA = And(AKnave, BKnave)

knowledge1 = And(
    rules,
    Or(SentensesA, Not(SentensesA)),  
    Biconditional(SentensesA, AKnight),
    Biconditional(Not(SentensesA), AKnave)    
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
SentensesA = Or(
    And(AKnave, BKnave), 
    And(AKnight, BKnight))
SentensesB = Or(
    And(AKnave, BKnight),
    And(AKnight, BKnave))
knowledge2 = And(
    rules,
    Or(SentensesA, Not(SentensesA)),  
    Biconditional(SentensesA, AKnight),
    Biconditional(Not(SentensesA), AKnave),
    Or(SentensesB, Not(SentensesB)),  
    Biconditional(SentensesB, BKnight),
    Biconditional(Not(SentensesB), BKnave)        
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
SentensesA = Or(AKnave,AKnight)
SentensesB = And(
    CKnave,
    Implication(SentensesA, BKnave))
SentensesC = (AKnight)
knowledge3 = And(
    rules,
    Or(SentensesA, Not(SentensesA)),  
    Biconditional(SentensesA, AKnight),
    Biconditional(Not(SentensesA), AKnave),
    Or(SentensesB, Not(SentensesB)),  
    Biconditional(SentensesB, BKnight),
    Biconditional(Not(SentensesB), BKnave),
    Or(SentensesC, Not(SentensesC)),  
    Biconditional(SentensesC, CKnight),
    Biconditional(Not(SentensesC), CKnave)  
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    gameRules(symbols)
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")        


if __name__ == "__main__":
    main()
