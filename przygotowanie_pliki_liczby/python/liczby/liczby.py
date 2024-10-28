"""
 Przykłady z liczbami przy użyciu funckji wbudowanych.

 Każdy przykład ma osobne funkcje.

 Kod jest też w miarę samodokumentujący i jest napisany zgodnie z formatowaniem python.
 niektórych rzeczy takich jak ': int' czy '-> int' nie trzeba pisać ale kij.
"""

def dec_to_bin(liczba: int) -> None:
    """
     Zamienia liczbę dziesiętną na liczbę dwójkową (binarną).
    """

    base_2: str = bin(liczba)
    print(base_2)  # "0bxxxx"
    # Możemy też obciąć "0b"
    print(base_2[2::])

    """
    [x:y:z] oznacza: x - indeks startowy, y: indeks końcowy, z: krok
    [2::] zacznij od drugiego elementu (czyli [1]) i idź do końca
    [::-1] zacznij od zerowego elementu i idź wstecz (czyli od końca do początku)
    """


def dec_to_oct(liczba: int) -> None:
    """
     Zamienia liczbę dziesiętną na liczbę ósemkową (oktalną).
    """

    print(oct(liczba)[2::])


def dec_to_hex(liczba: int) -> None:
    """
     Zamienia liczbę dziesiętną na liczbę szesnastkową (heksadecymalną).
    """

    print(hex(liczba))  # Nie obcinam 0x bo czasem ciężko ogarnąć że to hex.


def bin_to_dec(liczba_bin: str) -> None:
    """
     Zamienia liczbę dwójkową na liczbę dziesiętną.
    """

    print(int(liczba_bin,2))


def oct_to_dec(liczba_oct: str) -> None:
    """
     Zamienia liczbę ósemkową na liczbę dziesiętną.
    """

    print(int(liczba_oct,8))


def hex_to_dec(liczba_hex: str) -> None:
    """
     Zamienia liczbę szesnastkową na liczbę dziesiętną.
    """

    print(int(liczba_hex,16))


def x_to_dec(liczba_x: str, system: int) -> None:
    """
     Zamienia liczbę z dowolnego systemu na liczbę dziesiętną.
    """

    print(int(liczba_x,system))


def main() -> None:
    """
     Deklaracja main =/= uruchomienie go
    """

    # Liczby dziesiętne
    print("Podaj liczbę dziesiętną: ")
    inp: int = int(input())

    dec_to_bin(inp)
    dec_to_oct(inp)
    dec_to_hex(inp)

    # Liczba binarna
    print("Podaj liczbę binarną (np. 10101)")
    inp: str = input()
    bin_to_dec(inp)

    # Liczba oktalna
    print("Podaj liczbę octalną (np. 17171)")
    inp = input()
    oct_to_dec(inp)

    # Liczba heksadecymalna
    print("Podaj liczbę heksadecymalną (np. ABCDF)")
    inp = input()
    hex_to_dec(inp)

    # Liczba w dowolnym systemie
    print("Podaj liczbę w dowolnym systemie")
    inp = input()
    print("Podaj system liczbowy (np. 3 to trójkowy) (czyli najwyższa cyfra/litera + 1)")
    base = int(input())
    x_to_dec(inp, base)



"""
 Nie polecam zostawiać kodu luzem poza funkcjami, zwłaszcza w większych projektach
"""
if __name__ == "__main__":
    main()
