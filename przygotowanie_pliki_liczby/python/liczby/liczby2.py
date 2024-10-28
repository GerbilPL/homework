"""
 Przykłady z liczbami bez użycia funckji wbudowanych.

 Każdy przykład ma osobne funkcje.
 
 Kod jest też w miarę samodokumentujący i jest napisany zgodnie z formatowaniem python.
 niektórych rzeczy takich jak ': int' czy '-> int' nie trzeba pisać ale kij.
"""

def dec_to_bin(liczba: int) -> None:
    """
     Zamienia liczbę dziesiętną na liczbę dwójkową (binarną).
    """

    # Tutaj z listą (czyli takim vectorem lub dynamicznym arrayem)
    binarka: list = []

    if liczba==0:
        print(0)

    while liczba!=0:
        binarka+=[liczba%2]
        liczba//=2
    
    # Musimy pamiętać że czytamy od końca
    # Można zamienić (funckja wbudowana!)
    binarka.reverse()
    print(binarka)
    # reset
    binarka.reverse()

    # Lub można iterować od tyłu
    print(binarka[::-1])
    """
     Jak nie wiesz o co biega z [::-1] to zapraszam do liczby.py
    """
    # z ładniejszym printem
    [print(x, end="") for x in binarka[::-1]]
    print()


def dec_to_oct(liczba: int) -> None:
    """
     Zamienia liczbę dziesiętną na liczbę ósemkową (oktalną).
    """
    
    # Można też zamiast listy użyć stringa, też trzeba od tyłu
    oktalka: str = ""

    if liczba==0:
        print(0)

    while liczba!=0:
        oktalka+=str(liczba%8)
        liczba//=8
    
    # Tak samo można użyć [::-1] jak z listą
    print(oktalka[::-1])


def dec_to_hex(liczba: int) -> None:
    """
     Zamienia liczbę dziesiętną na liczbę szesnastkową (heksadecymalną).
    """

    hexalka: str = ""

    if liczba==0:
        print(0)

    while liczba!=0:
        hexalka+=str(liczba%8)
        liczba//=8
    
    print(hexalka[::-1])


def bin_to_dec(liczba_bin: list) -> None:
    """
     Zamienia liczbę dwójkową na liczbę dziesiętną.
    """

    """
     Ten algorytm jest napisany z użyciem list int
     Jeżeli chcemy stringa to wystaczy zmienić:
     decymalka = decymalka*2+int(x)
    """

    decymalka = 0
    for x in liczba_bin:
        decymalka = decymalka*2+x
    print(decymalka)

def oct_to_dec(liczba_oct: list) -> None:
    """
     Zamienia liczbę ósemkową na liczbę dziesiętną.
    """

    decymalka = 0
    for x in liczba_oct:
        decymalka = decymalka*8+x
    print(decymalka)


def hex_to_dec(liczba_hex: list) -> None:
    """
     Zamienia liczbę szesnastkową na liczbę dziesiętną.
     Tego przykładu raczej nie powinno być nawet na maturze, ale i tak tutaj jest, jeśli się mylę
    """

    decymalka = 0
    for x in liczba_hex:
        match str(x).capitalize():
            case 'A':
                x = 10
            
            case 'B':
                x = 11
            
            case 'C':
                x = 12
            
            case 'D':
                x = 13
            
            case 'E':
                x = 14
            
            case 'F':
                x = 15
            
            case _:
                x = int(x)
        
        decymalka = decymalka*16+x

    print(decymalka)


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
    inp: list = [int(x) for x in input()] # Tak trzeba zrobić jeżeli chcemy użyć tablicy i wpisywać sobie różne liczby
    bin_to_dec(inp)

    # Liczba oktalna
    inp = [1,4] # Lub samemu ustawić wartość
    oct_to_dec(inp)

    # Liczba heksadecymalna
    print("Podaj liczbę heksalną (np. ABCDF)")
    inp = input()
    hex_to_dec(inp)


"""
 Nie polecam zostawiać kodu luzem poza funkcjami, zwłaszcza w większych projektach
"""
if __name__ == "__main__":
    main()
