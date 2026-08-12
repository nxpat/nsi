def est_palindrome(mot):
    if len(mot) <= 1:
        return True
    if mot[0] != mot[-1]:
        return False
    else:
        return est_palindrome(mot[1:-1])
