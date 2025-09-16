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

## program `generate_sentences.py`:
1. generates the sentence from symbol S
2. randomly picks one substitution
3. for each symbol in the RHS:
    1. if it's a non-terminal -> recursively expand
    2. if it's a terminal (for now, starts with `"*"`) -> pick one from file
4. repeat until only terminals remain
5. as a/an is phonetic and other stuff and hence needs context-sensitive grammar, for now, replace "a" with "an" if next word is a vowel
6. repeats this for n sentences

# Usage

run the program, for eg. using sample.rulefile and generating 10 sentences:
```
$ python generate_sentences.py -r sample.rulefile -n 10
```

sample outputs:
```
flawy shandy outbreeds a lexeme across a sunbows
gamic baddies bobsleds a matchlockthe hagdons deny the buckwheat goldarn sometimes
a breastpin exult nightlong
a freeing crumpet discards the moochers onto the bletting
haemal crosspiece sunder uncleansed smashing
bowing skimming prewarms breadthwise
unspent gargoyles reweigh a tourer against the turfy pigtail
the piney pirog confab jointly out a spireme
the peccant duma congest deafly singly
a gabbles devest the strangest shingle under the burgoos crudely
a jotter outacts strictly without mawkish clearance
a scratches scourging the profaned morceau earthward
the gormless sawyers hiccups at unoiled insert
ungrazed address dislike from the walnuts
undress lichens risen into uncut fattest
hempen pacing cooing lidded baetyls namely kingly
clastic clabbers reword the fodders up a countships widely
the fifteenths foredate the unmet tolu simply
an enarched billows subsoil landwards outboard
a gouty kishke endured loosely straightway until an inby handfast
a cursive achieves barebacked cousin
weekly mercer descants longly rightwards
baric calker backfires inboard offside
the uncured nailers fratches statewide
shawlless bugbane draggle dourly collect bleakly
jutting owlets resiles down a faucial lazar
precast many deplume a custom rushers around the twiggy rhinos
the ungyved thornbacks rapes the lungis above the scratchy lacebark past a daring eucrites
headfirst abele displease above an unfound dirndl
the yonder romaunts provoked a neckings until fretted strickle lichtly
a tightwad remints
fewer prowler farcings the drawers
the chartered turbines instill about
a corban rumours alee
the banjo amerce scarcely meetly awry
a bawdy parlor sensings twinning pilule
direful tourings enswathe the unknelled nursemaid upon a hammy trample
a cissoid holders roupy soli like the podsol
the surging tosspots freewheels a whittling chalkstones above the imports perdie frankly
battered synchro chitchat coaly sharif bluntly
an insides firebug bobble parcel inshore below aloof fallal
the sighers mooing feebly nightly
a burlesque sora twangle
gowaned sideboards bitting a later pastille without the looser waxers over a crinite moonwort
an alone puffball whimper fretty bullocks
a scaler bugles vainly against the pointless hauler
the lobes confide worldly
rearmost baseball befell
pinguid achkans smarten across lacy grandniece
the fubsy ratteen defeat statant quines over the douter
nimble bowknot emplaced
the mangey pogroms differs blackly southwards
a rodless serai arose rhodic shamans d'accord
a sipper captured vasty horseback beneath a beauish pantries
grimmer screamer henna a peavey of the mattock
hither dammar smilings upwards
unscaled draftee perspires onshore nudely barely richly
the dimply tazza nitrates over shifty palsgraves
a warning sadists misruled a calix
the wartlike beeline clappings gladly
hapless bridgework tedding strictly
murrey offside agings the crankshafts down the slippy finos down the mynas
an abysm restart the added scheming through the weer catty
unthought fabrics deplanes strangely troppo over a seamy arbours
doggone gutser resiles despite the runty rone
the earthquaked penance spirals across a rallyes
a caput redding an unproved scribbler aside
the wicked microbe mishits off crownless footpaths
a payer insets offshore pardy assai outdoors
an infirm weirdies misshape nagging missile at a minder
intact spinny parsing the aides onto a tubing agone
a backbone finest thereof
the briny halals lobby past anti blacklist
bomb stompers scruples a scoopful upon barest doorstops of a levee
a nurseling enlarge the razees out a painless jugal
frisky earthworms housels a gamest marquise ajar
a novel pinole caddies
a dolor outsteps upstream homewards atwain
the upthrows foozles dully
unsluiced griever snaffles beyond a spherelike counsels
a blatant encrusts ensconced a choky buyer between the raffish surrounds near audile boggler
histie dousing chapter blasted stownlins afresh
nervine sportscast enroot opposite a monism thimbles
the bises exudes
a centric nametape betroths
peaky derricks derides a sideward floodgate inside the entrants
the slatings emote
the conflict harshen
mordant devils slumming potty critiques above adscript ravens from the ragwort
foggy amah favor ethmoid stammel during the thickness nowhere
a fouters usurp a rumour against the hornstone in a surcoat
the antiques bestows a daffy chigoes along a bombards past the drowners
the dinghies prelect the calcic wastrels along the phrenic tapster
abroad piddocks earwig outside a neglects
a calmy loggia misheard yarely
gelid dobby disbranch a basin fleetly
an unraised fillets ruing
an exits recoup goddamn hellish proudly
the moldy pourer fathom a plangent frotteur despite a pardine timepiece
```
