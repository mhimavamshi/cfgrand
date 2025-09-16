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

def check_vowels(words):
    # NOTE: hack around context sensitive grammar
    # of course doesnt consider phonetics
    vowels = {"a", "e", "i", "o", "u"}
    for i in range(len(words)-1):
        if words[i].lower() == "a" and words[i+1][0] in vowels:
            words[i] = "an"

def format_commas(words):
    for i in range(len(words)-1):
        if words[i+1] == ",":
            words[i] += ","
    words[:] = [word for word in words if word != ","]


def add_period(words):
    words[-1] += "."

def post_process(words):
    check_vowels(words)
    add_period(words)
    format_commas(words)

def generate_full_sentence(rules):
    words = generate_sentence(rules)
    post_process(words)
    sentence = " ".join(words)
    return sentence
    
def main():

    parser = argparse.ArgumentParser(description="Generate random sentences from a defined Context-Free Grammar.")
    parser.add_argument("-r", "--rules", type=str, required=True, help="rulesfile that contains the grammar")
    parser.add_argument("-n", "--number", type=int, required=True, help="number of sentences to generate")
    parser.add_argument("-a", "--attempts", type=int, default=1, help="number of times to look for unique sentences")

    args = parser.parse_args()

    rules = extract_rules(args.rules)

    sentences = set()

    for _ in range(args.number):
        sentence = generate_full_sentence(rules)
        attempts = 0
        while sentence in sentences and attempts < args.attempts:
            sentence = generate_full_sentence(rules)
            attempts += 1
        sentences.add(sentence)
        print(sentence)


if __name__ == "__main__":
    main()
