# create covert action types
db.session.add(CovertActionType(
    requested_action = "Background check",
    category = "Intel gathering",
    description = "A desktop exercise in which an agent trawls publicly available information on a subject to build a profile of their life, career, motivations and views of the regime",
    approval_level_required = 2,
    work_credits_required = 2))

db.session.add(CovertActionType(
    requested_action = "Tail",
    category = "Intel gathering",
    description = "A Covert Ops team is tasked with following the subject, identifying their behaviour, relationships and travel",
    approval_level_required = 2,
    work_credits_required = 4))

db.session.add(CovertActionType(
    requested_action = "Hack phone",
    category = "Intel gathering",
    description = "Use covert methods to gain access to to the subject's mobile phone calls and texts",
    approval_level_required = 2,
    work_credits_required = 5))

db.session.add(CovertActionType(
    requested_action = "Trawl bank records",
    category = "Intel gathering",
    description = "Gain access to a subject's banking records, allowing identification of spending patterns, wealth and unexplained behaviour",
    approval_level_required = 2,
    work_credits_required = 5))

db.session.add(CovertActionType(
    requested_action = "Kidnap and interrogate",
    category = "Direct action",
    description = "This will yield extensive intelligence on a subject. We will impersonate agents of the regime, so it will also weaken the subject's loyalty to the regime",
    approval_level_required = 5,
    work_credits_required = 15))

db.session.add(CovertActionType(
    requested_action = "Honeypot",
    category = "Establish vulnerability",
    description = "Task a Covert Ops operative with special skills to seduce the target: can lead to information as well as blackmail leverage",
    approval_level_required = 3,
    work_credits_required = 10))

db.session.add(CovertActionType(
    requested_action = "Remove",
    category = "Direct action",
    description = "Remove a threat permanently",
    approval_level_required = 5,
    work_credits_required = 40))