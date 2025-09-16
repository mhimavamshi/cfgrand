CFGs are defined in .rulefile:
```
LHS -> RHS
# comment
# expands the words in lines as unique substitutions
# for now only terminals
*LHS -> file.txt 
```

run the program, for eg. using sample.rulefile and generating 10 sentences:
```
$ python generate_sentences.py -r sample.rulefile -n 10
```




