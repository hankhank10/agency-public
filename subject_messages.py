#bribery outgoing messages
    outgoing_sms_message = "I put a little something in your bank account that I thought you might like. There's plenty more where that came from..."
    # please add others which will be randomised


#bribery response messages

    like_change = 0
    bribe_reaction = "Um, I don't know what you think $" + str(bribe_amount) + " is going to buy you! You think I'm that cheap??"

    if percentage_bribe > valuable_start:  #valuable bribe
        like_change = 5
        bribe_reaction = "Thank you! That really helps. What is it you want me to help you with?"
        # please add others which will be randomised

    if percentage_bribe > hugely_valuable_start:  #hugely valuable bribe
        like_change = 10
        bribe_reaction = "Wow, that's.... insane. Thank you!"
        # please add others which will be randomised

    if subject.has_trait ("in debt"):
        like_change = like_change * 2
        if like_change >0: bribe_reaction = "OMG thank you so much - I'm having a few money troubles at the moment so it really helps"
        # please add others which will be randomised

    if subject.has_trait ("greedy"):
        like_change = like_change * 2
        if like_change >0: bribe_reaction = "Boom. Love it. Keep it coming stranger!"
        # please add others which will be randomised


# send the blackmail messages
    dice = randint(1,3)
    if dice == 1: burner.send_outgoing_burner_sms(current_user.id, subject_id, "We all have secrets... how about if I reveal yours?")
    if dice == 2: burner.send_outgoing_burner_sms(current_user.id, subject_id, "I bet people would be surprised to know what I know about you. You should be more careful how you keep your secrets.")
    if dice == 3: burner.send_outgoing_burner_sms(current_user.id, subject_id, "Funny, you don't seem the kind of person to have dark secrets. If only people knew...")

    dice = randint(1,3)
    if dice == 1: burner.receive_incoming_burner_sms(subject_id, current_user.id, "I don't have any secrets lol", 1) #the 1 here is the delay before they reply in minutes
    if dice == 2: burner.receive_incoming_burner_sms(subject_id, current_user.id, "I don't know what you're talking about", 1)
    if dice == 3: burner.receive_incoming_burner_sms(subject_id, current_user.id, "Who is this?? What secrets do you mean?", 1)

    if trait.name == "sex addict":
        burner.send_outgoing_burner_sms(current_user.id, subject_id, "You thought nobody would find out about your sex addiction? What *will* people at the office say??",1)

    if trait.name == "gambler":
        burner.send_outgoing_burner_sms(current_user.id, subject_id, "How much money have you spent on gambling? In total I mean...",1)

    if trait.name == "alcoholic":
        burner.send_outgoing_burner_sms(current_user.id, subject_id, "You think they let alcoholics have access to the sort of information that you do?",1)

    if trait.name == "drug addict":
        burner.send_outgoing_burner_sms(current_user.id, subject_id, "Drugs are bad for you. Not to mention illegal. Not to mention a sackable offence",1)

    if trait.name == "in debt":
        burner.send_outgoing_burner_sms(current_user.id, subject_id, "Did you think nobody would find out about the debts?",1)

    if trait.name == "having an affair":
        burner.send_outgoing_burner_sms(current_user.id, subject_id, "You're married, right? You don't look married in the photos I have of you on my desk. Is your marriage an open one? Or are you just cheating?",1)

    if trait.name == "stealing from employer":
        burner.send_outgoing_burner_sms(current_user.id, subject_id, "When did you start stealing? Or have you always done it? Doesn't really matter, I supposed. Tell it to the judge.",1)

    if trait.name == "secret criminal past":
        burner.send_outgoing_burner_sms(current_user.id, subject_id, "What, you thought nobody would find out about your past? They don't *have* to I suppose. Not if you cooperate.",1)

    if trait.name == "unsavory family ties":
        burner.send_outgoing_burner_sms(current_user.id, subject_id, "Do they let people with families like yours work in jobs like yours? Or does nobody know? Shame, bet you were good at your job",1)

    if trait.name == "secret extremist sympathies":
        burner.send_outgoing_burner_sms(current_user.id, subject_id, "Does your employer know about all those mailing lists you're on? Some dangerous stuff there. You should be careful",1)

    if trait.name == "tax evasion":
        burner.send_outgoing_burner_sms(current_user.id, subject_id, "I get it. Nobody likes paying taxes. Nobody would blame you. Except a judge, of course.",1)

    if trait.name == "fraudulent past":
        burner.send_outgoing_burner_sms(current_user.id, subject_id, "Are you 100% sure your resume is up to date? Some stuff in there I couldn't track down...",1)

    if trait.name == "fell into honeypot":
        if subject.attracted_to_gender = "male":
            burner.send_outgoing_burner_sms(current_user.id, subject_id, "Nice guy you met at that hotel bar the other night. Hope you two had fun.", 1)
        if subject.attracted_to_gender = "female":
            burner.send_outgoing_burner_sms(current_user.id, subject_id, "Didn't you think it at all strange the way that girl came onto you at the bar the other night?", 1)

    dice = randint(1, 5)
    if dice == 1: burner.receive_incoming_burner_sms(subject_id,current_user.id,"OMG ok, what do you want??", 2, "fears_agent", 6)  #the 2 here is the delay in reply in minutes, the 6 is the impact on agent fear (x10)
    if dice == 2: burner.receive_incoming_burner_sms(subject_id,current_user.id,"Oh I see. What are you after exactly?", 2, "fears_agent", 6)
    if dice == 3: burner.receive_incoming_burner_sms(subject_id,current_user.id,"You wouldn't? Would you? Can you please give me a chance?", 2, "fears_agent", 6)
    if dice == 4: burner.receive_incoming_burner_sms(subject_id,current_user.id,"How do I make this right?", 2, "fears_agent", 6)
    if dice == 5: burner.receive_incoming_burner_sms(subject_id,current_user.id,"You want money? How can I make this go away?", 2, "fears_agent", 6)
