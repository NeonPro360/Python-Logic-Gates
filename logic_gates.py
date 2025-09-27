def xor_gate(statement1, statement2):

    if statement1 == statement2:
        return False

    else:
        return True

def xnor_gate(statement1, statement2):

    if statement1 != statement2:
        return False

    else:
        return True

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

def not_gate(statement):

    if statement:
        return False

    else:
        return True
