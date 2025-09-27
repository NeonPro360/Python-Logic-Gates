def xor_gate(*statements):

    truths = 0

    for i in range(len(statements)):
        if statements[i]:
            truths += 1

    if truths%2 == 1:
        return True
    else:
        return False

def xnor_gate(*statements):

    truths = 0

    for i in range(len(statements)):
        if statements[i]:
            truths += 1

    if truths%2 == 0:
        return True
    else:
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
