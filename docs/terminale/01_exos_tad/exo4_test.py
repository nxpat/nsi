assert verifier_parentheses("(())") is True, "Échec : L'expression '(())' est correcte."
assert verifier_parentheses("()()") is True, "Échec : L'expression '()()' est correcte."
assert verifier_parentheses("())(") is False, (
    "Échec : L'expression '())(' est incorrecte (parenthèse fermante en trop au début)."
)
assert verifier_parentheses("((()") is False, (
    "Échec : L'expression '((()' est incorrecte (il manque une parenthèse fermante)."
)
assert verifier_parentheses("(") is False, "Échec : L'expression '(' est incorrecte."
assert verifier_parentheses("") is True, (
    "Échec : Une chaîne vide est considérée comme bien parenthésée."
)
