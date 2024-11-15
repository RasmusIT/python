import turtle

def temp(t, yhik):
    """
    Teisendab temperatuuri Celsiusest Fahrenheitiks ja vastupidi.

    Parameetrid:
    t (int): Esimene arv.
    yhik (String): Teine arv.

    Tagastab:
    int: temperatuuri.

    Näide:
    >>> summa(0, "c")
    -32
    """
    if yhik=="c":
        v = t * 5/9+32
    else:
        v = (t - 32) * 5/9

    return round(v,2)
print(temp.__doc__)
print(temp(30,"c"))



kytus = lambda ktyusekulu, kaugus: (kytusekulu / 100) * kaugus
print(kytus(5,150))
konto = 10

def konto_haldur(algne_saldo,toiming, summa):
    if toiming == "deposiit":
        v = algne_saldo + summa
        konto = v
    else:
        v = summa - algne_saldo
        konto = v
    return v
print(konto_haldur(20, "deposiit", konto))
print(konto_haldur(10, "deposiit", konto))
print(konto_haldur(100, "deposiit", konto))
print(konto_haldur(25, "valjavote", konto))