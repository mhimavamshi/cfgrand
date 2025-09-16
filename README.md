# Working

## Rulefile Format
CFGs are defined in .rulefile:
```
LHS -> RHS
# comment
# expands the words in lines as unique substitutions
# for now only terminals
*LHS -> file.txt 
```
## Program flow
procedural style is followed

### program `make_rules.py`:
1. reads the .rulefile
2. builds dictionary of rules for example:
```
"NP": [["Article", "Noun"]],
"Noun": [["*dog"], ["*cat"], ...]
```
3. verifies if each non-terminal has an expansion

### program `generate_sentences.py`:
1. generates the sentence from symbol S
2. randomly picks one substitution
3. for each symbol in the RHS:
    1. if it's a non-terminal -> recursively expand
    2. if it's a terminal (for now, starts with `"*"`) -> pick one from file
4. repeat until only terminals remain
5. post process the sentence:
    1. as a/an is phonetic and other stuff and hence needs context-sensitive grammar, for now, replace "a" with "an" if next word is a vowel
    2. format the commas properly
    3. add a period to end of sentence
6. repeats this for n sentences

# Usage

run the program, for eg. using sample.rulefile and generating 10 sentences:
```
$ python generate_sentences.py -r sample.rulefile -n 10
```

sample outputs:
```
the laurelled fumblers spancels a manic beyond a clinker.
a ghastly fulmar perplex gelded rami, staggers the spying, redates, predoom, strippings during a spearheads.
an aldrin affects a buzzers across a thrifty temper, past a qualmish terrain, for roily nightgowns, past the anile tushy, except a squirmy fervour, with only wailers, down a southmost mammoth, admit the seesaws by severe arpent, outside fatigue pubis, around the chastised kheda, beneath the kneeling whinstone, by an udder, of the segments with stateside shames.
senseless rivals tottings forthwith around lossy biomes, underneath a sulcate earthworks.
a sneerers dodder the viewy rasper crudely daylong, grave, ajee, singly, slantly, hereby.
```

# Future
- [ ] Handle recursion depth and limit it

# Random Thoughts
## vague ideas, ignore safely
- basically "Colorless green ideas sleep furiously" like sentences generator
- what if we could generate random sentences, train a ML model for eg. contrastive learning to see if semantically meaningful (trained on books etc.,) or not, and then just let it run? 
- or, the other way around, use a grammar to restrict tokens in the first place and train the model for semanticity and also grammar? then generate a response statement from a 'semantic vector' 
