import io
import sys


def capturer_affichage(f, *args):
    buffer = io.StringIO()
    sys.stdout = buffer
    f(*args)
    sys.stdout = sys.__stdout__
    return buffer.getvalue().strip().split()


out_5 = capturer_affichage(compte_a_rebours, 5)
assert out_5 == ["5", "4", "3", "2", "1", "0"], (
    f"Échec pour n=5. Attendu ['5', '4', '3', '2', '1', '0'], obtenu {out_5}"
)

out_0 = capturer_affichage(compte_a_rebours, 0)
assert out_0 == ["0"], f"Échec pour n=0. Attendu ['0'], obtenu {out_0}"
