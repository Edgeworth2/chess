from multigiocatore import multigiocatore

print("Benvenuto su scacchi sul terminale.")
print("1. Multigiocatore locale.")
print("2. Contro AI")
print("3. Spiegazione della simbologia")
choise = int(input())
if choise == 1:
    multigiocatore()
elif choise == 3:
    print("due spazi stanno a significare senza pedina.")
    print("B sta per Black e W sta per white.")
    print("R sta per Rook (torre), N sta per Knight (cavallo), B sta per Bishop (alfiere), Q sta per Queen (regina), K sta per King (re).")