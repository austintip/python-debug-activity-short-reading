offense = False
defense = False
rule_changes = False

print("How are the Jags doing?\n")

def get_offense():
    global offense
    offense = True
    print("We have offense:", offense)

def get_defense():
    global defense
    defense = True
    print("We have defense:", defense)

def get_rule_changes():
    global rule_changes
    rule_changes = True
    print("We have some rule changes:", rule_changes)

get_offense()
get_defense()
get_rule_changes()
if offense and defense and rule_changes:
    print("We're going to the Super Bowl!")
else:
    print("I can't predict the future, but no, the Jaguars will never win the Super Bowl.")
    
# if offense and defense




