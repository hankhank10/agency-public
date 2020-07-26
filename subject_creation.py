#employment industry
dice = randint(1,6)
if dice == 1: employment_industry = "Politics"
if dice == 2: employment_industry = "Finance"
if dice == 3: employment_industry = "Military Manufacturing"
if dice == 4: employment_industry = "Civil Service"
if dice == 5: employment_industry = "Technology"
if dice == 6: employment_industry = "Journalism"

#employment level
dice = randint(1,100)
employment_job_level = 1
if dice <= 25: employment_job_level = 2
if dice <= 10: employment_job_level = 3
if dice <= 3: employment_job_level = 4
if dice <= 1: employment_job_level = 5

#job title
if employment_industry == "Politics":
    if employment_job_level == 1:
        dice = randint(1,2)
        if dice == 1: employment_job_title = "Intern"
        if dice == 2: employment_job_title = "Admin Assistant"
    if employment_job_level == 2:
        dice = randint(1,5)
        if dice == 1: employment_job_title = "Advisor"
        if dice == 2: employment_job_title = "Researcher"
        if dice == 3: employment_job_title = "Think Tank Researcher"
        if dice == 4: employment_job_title = "Speech Writer"
        if dice == 5: employment_job_title = "Spokesperson"
    if employment_job_level == 3:
        dice = randint(1,2)
        if dice == 1: employment_job_title = "Senior Advisor"
        if dice == 2: employment_job_title = "Member of Legislature"
    if employment_job_level == 4:
        dice = randint(1,2)
        if dice == 1: employment_job_title = "Presidential Advisor"
        if dice == 2: employment_job_title = "Head of Legislative Affairs"
    if employment_job_level == 5:
        employment_job_title = "Cabinet Member"

if employment_industry == "Finance":
    if employment_job_level == 1:
        dice = randint(1,3)
        #dice = randint(1,4) # Proposed adding 1 new job
        if dice == 1: employment_job_title = "Analyst"
        if dice == 2: employment_job_title = "Bank Clerk"
        if dice == 3: employment_job_title = "Admin Assistant"
        #if dice == 4: employment_job_title = "Junior Accountant"
    if employment_job_level == 2:
        dice = randint(1,2)
        #dice = randint(1,3) # Proposed adding 1 new job
        if dice == 1: employment_job_title = "Senior Financial Analyst"
        if dice == 2: employment_job_title = "Branch Manager"
        #if dice == 3: employment_job_title = "Senior Accountant"
    if employment_job_level == 3:
        dice = randint(1,2) # Proposed changing "Department Head" into "Internal Auditor"
        if dice == 1: employment_job_title = "Department Head"
        #if dice == 1: employment_job_title = "Internal Auditor"
        if dice == 2: employment_job_title = "Manager"
    if employment_job_level == 4:
        #dice = randint(1,2)    # Proposed moving "Department Head" into level 4
        employment_job_title = "Senior Manager"
        #if dice == 1: employment_job_title = "Senior Manager"
        #if dice == 2: employment_job_title = "Department Head"
    if employment_job_level == 5:
        dice = randint(1,3)
        if dice == 1: employment_job_title = "Chief Executive Officer"
        if dice == 2: employment_job_title = "Chief Financial Officer"
        if dice == 3: employment_job_title = "Chief Technology Officer"
        #if dice == 4: employment_job_title = "Chief Operational Officer"

if employment_industry == "Military Manufacturing":
    if employment_job_level == 1:
        dice = randint(1,5)
        if dice == 1: employment_job_title = "R&D Assistant"
        if dice == 2: employment_job_title = "Junior Engineer"
        if dice == 3: employment_job_title = "Assistant Engineer"
        if dice == 4: employment_job_title = "Research Assistant"
        if dice == 5: employment_job_title = "Security Guard"
    if employment_job_level == 2:
        dice = randint(1,2)
        if dice == 1: employment_job_title = "Scientist"
        if dice == 2: employment_job_title = "Research Scientist"
    if employment_job_level == 3:
        dice = randint(1,3)
        if dice == 1: employment_job_title = "Senior Enginner"
        if dice == 2: employment_job_title = "Research Lab Chief"
        if dice == 3: employment_job_title = "Manufaturing Manager" # I think this is supposed to be "Manufacturing Manager"?
    if employment_job_level == 4:
        dice = randint(1,3)
        if dice == 1: employment_job_title = "Department Chief"
        if dice == 2: employment_job_title = "Research Lab Chief"
        if dice == 3: employment_job_title = "Manufaturing Manager"
    if employment_job_level == 5:
        dice = randint(1,3)
        if dice == 1: employment_job_title = "Chief Executive Officer"
        if dice == 2: employment_job_title = "Chief Financial Officer"
        if dice == 3: employment_job_title = "Chief Engineer"

if employment_industry == "Civil Service":
    if employment_job_level == 1:
        dice = randint(1,3)
        #dice = randint(1,4) # Proposed adding 1 new job
        if dice == 1: employment_job_title = "Data Entry Clerk"
        if dice == 2: employment_job_title = "Admin Assistant"
        if dice == 3: employment_job_title = "Personal Assistant"
        #if dice == 4: employment_job_title = "Field Officer"
    if employment_job_level == 2:
        dice = randint(1,3)
        #dice = randint(1,4) # Proposed adding 1 new job
        if dice == 1: employment_job_title = "Advisor"
        if dice == 2: employment_job_title = "Policy Advisor"
        if dice == 3: employment_job_title = "Legislative Affairs Director"
        #if dice == 4: employment_job_title = "Senior Field Officer"
    if employment_job_level == 3:
        dice = randint(1,2)
        #dice = randint(1,3) # Proposed adding 1 new job
        if dice == 1: employment_job_title = "Senior Advisor"
        if dice == 2: employment_job_title = "Senior Policy Advisor"
        #if dice == 3: employment_job_title = "Internal Auditor"
    if employment_job_level == 4:
        dice = randint(1,2)
        if dice == 1: employment_job_title = "Deputy Department Head"
        if dice == 2: employment_job_title = "Assistant Department Head"
    if employment_job_level == 5:
        employment_job_title = "Department Head"

if employment_industry == "Technology":
    if employment_job_level == 1:
        dice = randint(1,3)
        if dice == 1: employment_job_title = "Coder"
        if dice == 2: employment_job_title = "Q&A Assistant"
        if dice == 3: employment_job_title = "Developer"
    if employment_job_level == 2:
        dice = randint(1,4)
        if dice == 1: employment_job_title = "Python Developer"
        if dice == 2: employment_job_title = "Flask Developer"
        if dice == 3: employment_job_title = "Bootstrap Developer"
        if dice == 4: employment_job_title = "Q&A Lead"
    if employment_job_level == 3:
        dice = randint(1,2)
        if dice == 1: employment_job_title = "Senior Engineer"
        if dice == 2: employment_job_title = "Big Data Specialist"
    if employment_job_level == 4:
        dice = randint(1,2)
        if dice == 1: employment_job_title = "Ethics and Sustainability Lead"
        if dice == 2: employment_job_title = "Chief Product Evangelist"
    if employment_job_level == 5:
        dice = randint(1,3)
        if dice == 1: employment_job_title = "Chief Executive Officer"
        if dice == 2: employment_job_title = "Chief Financial Officer"
        if dice == 3: employment_job_title = "Chief Technology Officer"

if employment_industry == "Journalism":
    if employment_job_level == 1:
        #dice = randint(1,3) # Suggested Adding 2 more jobs
        employment_job_title = "Intern"
        #if dice == 1: employment_job_title = "Intern"
        #if dice == 2: employment_job_title = "Photographer"
        #if dice == 3: employment_job_title = "Staff Writer"
    if employment_job_level == 2:
        dice = randint(1,4)
        #dice = randint(1,6) # Suggested adding 2 more jobs
        if dice == 1: employment_job_title = "Junior Reporter"
        if dice == 2: employment_job_title = "Home Affairs Reporter"
        if dice == 3: employment_job_title = "Crime Correspondent"
        if dice == 4: employment_job_title = "Gossip Columnist"
        #if dice == 5: employment_job_title = "Foreign Corrsepondent"
        #if dice == 6: employment_job_title = "Business Columnist"
    if employment_job_level == 3:
        dice = randint(1,2) 
        #dice = randint(1,4) # Suggested adding 2 more jobs
        if dice == 1: employment_job_title = "Subedtor" #Is this "Subedtor" (intentional)? Or would it be "Subeditor"?
        if dice == 2: employment_job_title = "Leader Writer"
        #if dice == 3: employment_job_title = "Radio Host"
        #if dice == 4: employment_job_title = "Primetime News Presenter"
    if employment_job_level == 4:
        dice = randint(1,2)
        if dice == 1: employment_job_title = "Section Editor"
        if dice == 2: employment_job_title = "Editor"
    if employment_job_level == 5:
        employment_job_title = "Editor in Chief"

#determine age
if employment_job_level == 1: age = randrange(18,30)
if employment_job_level == 2: age = randrange(23,38)
if employment_job_level == 3: age = randrange(29,50)
if employment_job_level == 4: age = randrange(35,65)
if employment_job_level == 5: age = randrange(45,70)

#determine salary (in thousants)
if employment_job_level == 1: salary = randrange(22,30)
if employment_job_level == 2: salary = randrange(25,33)
if employment_job_level == 3: salary = randrange(30,50)
if employment_job_level == 4: salary = randrange(50,100)
if employment_job_level == 5: 
    if employment_industry == "Politics": salary = randrange (150,250)
    if employment_industry == "Finance": salary = randrange (1500,2000)
    if employment_industry == "Military Manufacturing": salary = randrange (950,1500)
    if employment_industry == "Civil Service": salary = randrange (100,120)
    if employment_industry == "Technology": salary = randrange (1500,4500)
    if employment_industry == "Journalism": salary = randrange (150,250)
