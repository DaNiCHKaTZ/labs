from typing import List, Set

def parse_cnf(cnf_str: str) -> List[Set[str]]:
    clauses = cnf_str.split('*')
    cnf = []
    for clause in clauses:
        literals = clause.strip().replace('(', '').replace(')', '').split('v')
        cnf.append(set(literal.strip() for literal in literals))
    return cnf

def resolve(ci: Set[str], cj: Set[str]) -> Set[str]:
    resolvent = set()
    for di in ci:
        if f"-{di}" in cj:
            resolvent = ci.union(cj)
            resolvent.remove(di)
            resolvent.remove(f"-{di}")
            return resolvent
        if di.startswith("-") and di[1:] in cj:
            resolvent = ci.union(cj)
            resolvent.remove(di)
            resolvent.remove(di[1:])
            return resolvent
    resolvent = set({"1"})    
    return resolvent

def apply_resolution(cnf: List[Set[str]]) -> bool:
    while True:
        new_clauses = []
        for i in range(len(cnf)):
            for j in range(len(cnf)):
                resolvent = resolve(cnf[i], cnf[j])
                if resolvent == set({"1"}):
                    continue
                if not resolvent:
                    for i in new_clauses:
                        cnf.append(i)
                    cnf.append({"0"})
                    print(cnf)    
                    return True  
                if resolvent not in cnf and resolvent not in new_clauses:
                    new_clauses.append((resolvent))  
        if len(new_clauses) == 0:
            print(cnf)
            return False         
        for clause in new_clauses:
            cnf.append(clause)
        print(cnf)    

def main():
    cnf_str = "-XvS*-SvR*-XvR*-XvR*S"
   
    cnf = parse_cnf(cnf_str)
    print(cnf)
    if apply_resolution(cnf):
        print("КНФ невыполнима (обнаружено противоречие).")
    else:
        print("КНФ выполнима.")

if __name__ == "__main__":
    main()
