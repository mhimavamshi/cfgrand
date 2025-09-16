import itertools

def build_program_rules(rules, seperation=" -> ", delimiter=" ", file_sign="*"):
    rule_dict = {}
    for rule in rules:
        left, right = rule.split(seperation)
        if left.startswith(file_sign):
            ends = [[file_sign + end] for end in read_file(right)]
            left = left[1:]
        else:
            ends = right.split(delimiter)
            ends = [ends]
        if left in rule_dict: rule_dict[left].extend(ends)
        else: rule_dict[left] = ends
    return rule_dict

def verify_rules(rule_dict):
    # NOTE: for now
    # interesting problem:
    # dict = {"a": ["b", "c", "d"], "b"}
    # for now anything with * is terminal, so don't need to check
    for left, rights in rule_dict.items():
        rights = set(itertools.chain.from_iterable(rights))
        for right in rights:
            if not right.startswith("*") and right not in rule_dict:
                print(f"{right} (non-)terminal doesn't exist.")
                return False
    return True

def read_file(filename):
    with open(filename) as fl:
        lines = fl.read().splitlines()
    return [line for line in lines if line.strip() and not line.strip().startswith("#")]


def extract_rules(file):
    rules = read_file(file)
    rules = build_program_rules(rules)
    success = verify_rules(rules)
    if not success:
        print("Rulefile is not formatted properly.")
        return {}
    return rules

def run_tests():
    # NOTE: for now
    rules = extract_rules("productionrules.rulefile")
    print(rules)

if __name__ == "__main__":
    run_tests()
