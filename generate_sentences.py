import argparse 
import random
from make_rules import extract_rules


def generate_sentence(rules, start="S", depth=0):

#    indent = "  " * depth
#    print(f"{indent}Expanding {start}")

    if start.startswith("*"):
        return [start[1:]]

    substitutions = rules[start]
    right = random.choice(substitutions)
    
    result = []

    for others in right:
        result.extend(generate_sentence(rules, start=others, depth=depth+1))

    return result

def post_process(words):
    # NOTE: hack around context sensitive grammar
    # of course doesnt consider phonetics
    vowels = {"a", "e", "i", "o", "u"}
    for i in range(len(words)-1):
        if words[i].lower() == "a" and words[i+1][0] in vowels:
            words[i] = "an"
    return words

def main():
    global sentence
    

    parser = argparse.ArgumentParser(description="Generate random sentences from a defined Context-Free Grammar.")
    parser.add_argument("-r", "--rules", type=str, required=True, help="rulesfile that contains the grammar")
    parser.add_argument("-n", "--number", type=int, required=True, help="number of sentences to generate")

    args = parser.parse_args()

    rules = extract_rules(args.rules)

    for _ in range(args.number):
        words = generate_sentence(rules)
        words = post_process(words)
        print(" ".join(words))
    

if __name__ == "__main__":
    main()
