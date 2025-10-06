def xor_gate(statement1, statement2):

    return (statement1 or statement2) and not(statement1 and statement2)

def xnor_gate(statement1, statement2):

    return not((statement1 or statement2) and not(statement1 and statement2))

def or_gate(*statements):

    for i in range(len(statements)):
        if statements[i]:
            return True
        else:
            continue

    return False

def nor_gate(*statements):

    for i in range(len(statements)):
        if statements[i]:
            return False
        else:
            continue

    return True

def and_gate(*statements):

    for i in range(len(statements)):
        if not statements[i]:
            return False
        else:
            continue

    return True

def nand_gate(*statements):

    for i in range(len(statements)):
        if not statements[i]:
            return True
        else:
            continue

    return False

def not_gate(statement):

    return not(statement)
