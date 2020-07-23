#determine type of trait
dice = randint (1,3)
if dice == 1: trait_category = "personality"
if dice == 2: trait_category = "general"
if dice == 3: trait_category = "blackmail"

if trait_category == "personality":
    dice = randint (1,9)
    if dice == 1: trait_name = "greedy"
    if dice == 2: trait_name = "austere"
    if dice == 3: trait_name = "melodramatic"
    if dice == 4: trait_name = "calm"
    if dice == 5: trait_name = "charming"
    if dice == 6: trait_name = "awkward"
    if dice == 7: trait_name = "ambitious"
    if dice == 8: trait_name = "lazy"
    if dice == 9: trait_name = "lustful"

if trait_category == "general":
    dice = randint (1,4)
    if dice == 1: trait_name = "attractive"
    if dice == 2: trait_name = "unattractive"
    if dice == 3: trait_name = "smart"
    if dice == 4: trait_name = "unintelligent"

if trait_category == "blackmail":
    dice = randint (1,8)
    if dice == 1: trait_name = "sex addict"
    if dice == 2: trait_name = "gambler"
    if dice == 3: trait_name = "alcoholic"
    if dice == 4: trait_name = "drug addict"
    if dice == 5: trait_name = "in debt"
    if dice == 6: trait_name = "having an affair"
    if dice == 7: trait_name = "stealing from employer"
    if dice == 8: trait_name = "secret criminal past"

#check for conflicts
this_subject = Subject.query.filter_by(id = subject_id).first_or_404()

if this_subject.has_trait (trait_name):
    print ("Already has trait")
    return ("#alreadyhas")

incompatible_trait = False
if trait_name == "greedy" and this_subject.has_trait ("austere"): incompatible_trait = True
if trait_name == "austere" and this_subject.has_trait ("greedy"): incompatible_trait = True
if trait_name == "melodramatic" and this_subject.has_trait ("calm"): incompatible_trait = True
if trait_name == "calm" and this_subject.has_trait ("melodramatic"): incompatible_trait = True
if trait_name == "charming" and this_subject.has_trait ("awkward"): incompatible_trait = True
if trait_name == "awkward" and this_subject.has_trait ("charming"): incompatible_trait = True
if trait_name == "ambitious" and this_subject.has_trait ("lazy"): incompatible_trait = True
if trait_name == "lazy" and this_subject.has_trait ("ambitious"): incompatible_trait = True
if trait_name == "attractive" and this_subject.has_trait ("unattractive"): incompatible_trait = True
if trait_name == "unattractive" and this_subject.has_trait ("attractive"): incompatible_trait = True
if trait_name == "smart" and this_subject.has_trait ("unintelligent"): incompatible_trait = True
if trait_name == "unintelligent" and this_subject.has_trait ("smart"): incompatible_trait = True
