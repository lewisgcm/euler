"""
water = 'H2O'
parse_molecule(water)                 # return {H: 2, O: 1}

magnesium_hydroxide = 'Mg(OH)2'
parse_molecule(magnesium_hydroxide)   # return {Mg: 1, O: 2, H: 2}

var fremy_salt = 'K4[ON(SO3)2]2'
parse_molecule(fremySalt)             # return {K: 4, O: 14, N: 2, S: 4}
"""

def parse(molecule):
    node = {}
    current = ""
    index = 0
    while index < len(molecule):
        char = molecule[index]
        if char.isdigit():
            inc = 1 if not char.isdigit() else int(char)
            for i in current:
                node[i] = inc if i not in node else node[i] + inc
            current = ""
        elif char in ["(", "["]:
            if current != "":
                for i in current:
                    node[i] = 1 if i not in node else node[i] + 1
            end = molecule.find("]" if char == "[" else ")", index)
            mult = int(molecule[end+1])
            for key, value in parse(molecule[index+1:end]).iteritems():
                value = int(value) * mult
                node[key] = value if key not in node else node[key] + value
            index = end + 2
        elif index+1 < len(molecule) and not molecule[index+1].isdigit():
            current = current + char
        index = index + 1
    if current != "":
        for i in current:
            node[i] = 1 if i not in node else node[i] + 1
    return node

print parse("H2O")
#print parse("Mg(OH)2")
print parse("K4[ON(SO3)2]2")
