#determine type of trait
dice = randint (1,3)
if dice == 1: trait_category = "personality"
if dice == 2: trait_category = "general"
if dice == 3: trait_category = "blackmail"

if trait_category == "personality":
    dice = randint (1,9)
     #dice = randint (1,18)   # Proposed several new personality traits
    if dice == 1: trait_name = "greedy"
    if dice == 2: trait_name = "austere"
    if dice == 3: trait_name = "melodramatic"
    if dice == 4: trait_name = "calm"
    if dice == 5: trait_name = "charming"
    if dice == 6: trait_name = "awkward"
    if dice == 7: trait_name = "ambitious"
    if dice == 8: trait_name = "lazy"
    if dice == 9: trait_name = "lustful"
    #if dice == 10: trait_name = "chaste"
    #if dice == 11: trait_name = "trusting"
    #if dice == 12: trait_name = "skeptic"
    #if dice == 13: trait_name = "optimist"
    #if dice == 14: trait_name = "cynical"
    #if dice == 15: trait_name = "brave"
    #if dice == 16: trait_name = "coward"
    #if dice == 17: trait_name = "kind"
    #if dice == 18: trait_name = "cruel"

if trait_category == "general":
    dice = randint (1,4)
    #dice = randint (1,7)   # Proposed several new general traits
    if dice == 1: trait_name = "attractive"
    if dice == 2: trait_name = "unattractive"
    if dice == 3: trait_name = "smart"
    if dice == 4: trait_name = "unintelligent"
    #if dice == 5: trait_name = "atheist"
    #if dice == 6: trait_name = "religious"
    #if dice == 7: trait_name = "poor health"
        
if trait_category == "blackmail":   
    dice = randint (1,8)
    #dice = randint (1,13) # Proposed several new blackmail
    if dice == 1: trait_name = "sex addict"
    if dice == 2: trait_name = "gambler"
    if dice == 3: trait_name = "alcoholic"
    if dice == 4: trait_name = "drug addict"
    if dice == 5: trait_name = "in debt"
    if dice == 6: trait_name = "having an affair"
    if dice == 7: trait_name = "stealing from employer"
    if dice == 8: trait_name = "secret criminal past"
    #if dice == 9: trait_name = "paraphilia" #(sexual fetishism, e.g. necrophilia, pedophilia, zoophilia, etc.)
    #if dice == 10: trait_name = "unsavory familial ties" #(e.g. family member was a terrorist, war criminal, criminal, etc.)
    #if dice == 11: trait_name = "secret extremist sympathies" #(e.g. fascists/communists sympathies)
    #if dice == 12: trait_name = "tax evasion"
    #if dice == 13: trait_name = "fraudulent past" #(e.g. forged degrees, plagiarism, faked accomplishments, etc.)
    
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
#if trait_name == "lustful" and this_subject.has_trait ("chaste"): incompatible_trait = True
#if trait_name == "chaste" and this_subject.has_trait ("lustful"): incompatible_trait = True
#if trait_name == "trusting" and this_subject.has_trait ("skeptic"): incompatible_trait = True
#if trait_name == "skeptic" and this_subject.has_trait ("trusting"): incompatible_trait = True
#if trait_name == "optimist" and this_subject.has_trait ("cynic"): incompatible_trait = True
#if trait_name == "cynic" and this_subject.has_trait ("optimist"): incompatible_trait = True
#if trait_name == "atheist" and this_subject.has_trait ("religious"): incompatible_trait = True
#if trait_name == "religious" and this_subject.has_trait ("atheist"): incompatible_trait = True
#if trait_name == "brave" and this_subject.has_trait ("coward"): incompatible_trait = True
#if trait_name == "coward" and this_subject.has_trait ("brave"): incompatible_trait = True
#if trait_name == "kind" and this_subject.has_trait ("cruel"): incompatible_trait = True
#if trait_name == "cruel" and this_subject.has_trait ("kind"): incompatible_trait = True
