"""
Zadanie 6 z matury roz czerwiec 2016 cz. 2. plik obok w pdf
"""

def read_numbers_from_file(file_name: str) -> list:
    with open(file_name, 'r') as file:
        # Zwraca listę z liczbami bez whitespace
        return [line.strip() for line in file.readlines()]


def zadanie_6_1(numbers: list) -> None:
    # count = Suma +1 dla każdego numeru w liście kończącego się na 8 (czyli jest w systemie ósemkowym według zadania)
    count = sum(1 for number in numbers if int(number[-1]) == 8)
    # W zasadzie nie trzeba dawać encoding='utf-8' ale trzeba pamiętać jakby się coś sypało
    with open('wyniki_6_1.txt', 'w', encoding='utf-8') as file:
        file.write(str(count))


def zadanie_6_2(numbers: list) -> None:
    """
    [:-1] - wszystkie elementy oprócz ostatniego
    """
    # count = Suma +1 dla każdego numeru w liście kończącego się na 4 i nie zawierającego znaku '0'
    count = sum(1 for number in numbers if int(number[-1]) == 4 and '0' not in number[:-1])
    with open('wyniki_6_2.txt', 'w', encoding='utf-8') as file:
        file.write(str(count))


def zadanie_6_3(numbers: list) -> None:
    # count = Suma +1 dla każdego numeru w liście kończącego się na 2 (czyli to jest binarka, więc żeby była parzysta to 2^0 nie moze byc 1) 
    count = sum(1 for number in numbers if int(number[-1]) == 2 and int(number[-2]) == 0)
    with open('wyniki_6_3.txt', 'w', encoding='utf-8') as file:
        file.write(str(count))


def zadanie_6_4(numbers: list) -> None:
    # sumujemy liczby zamienione z systemu int(..., int(number[-1])) dla każdej liczby w systemie ósemkowym
    total_sum = sum(int(number[:-1], int(number[-1])) for number in numbers if int(number[-1]) == 8)
    with open('wyniki_6_4.txt', 'w', encoding='utf-8') as file:
        file.write(str(total_sum))


def zadanie_6_5(numbers: list) -> None:
    """
     O lambda polecam dokumentacje pythona, ale jest to taka funckja jakby w środku (jak mieliśmy np. w JS),
     a 'key' pobiera funkcję która pozwala zamienić liczbę na dziesiętną (bo min i max przyjmuja tylko dziesiętne domyślnie)
     
     https://realpython.com/python-min-and-max/#calling-min-and-max-with-a-single-iterable-argument

     Poniżej tej funkcji jest ten sam kod, ale bez użycia lambdy
    """
    # pobieramy liczby z listy które są najmniejsze i największe
    # lambda x: int(x[:-1], int(x[-1])) zwraca wartość x w systemie dziesiętnym, jest to tylko używane przes min() i max()
    min_number = min(numbers, key=lambda x: int(x[:-1], int(x[-1])))
    max_number = max(numbers, key=lambda x: int(x[:-1], int(x[-1])))

    # zamieniamy te liczby na dziesiętny
    min_value = int(min_number[:-1], int(min_number[-1]))
    max_value = int(max_number[:-1], int(max_number[-1]))

    with open('wyniki_6_5.txt', 'w', encoding='utf-8') as file:
        file.write(f"Min: {min_number} (Wartość: {min_value})\n")
        file.write(f"Max: {max_number} (Wartość: {max_value})\n")

# zad 6.5 bez lambdy:
def convert_to_decimal(number_str: str) -> int:
    # Pobierz podstawę liczby z ostatniego znaku
    base = int(number_str[-1])
    # Pobierz wartość liczby z pozostałych znaków
    value = number_str[:-1]
    # Zwróć liczbę jako int w systemie dziesiętnym
    return int(value, base)


def zadanie_6_5_bez_lambda(numbers: list) -> None:
    # Znajdź minimalną i maksymalną liczbę, korzystając z funkcji pomocniczej jako klucza
    min_number = min(numbers, key=convert_to_decimal)
    max_number = max(numbers, key=convert_to_decimal)

    # Oblicz wartości liczbowe minimalnej i maksymalnej liczby w systemie dziesiętnym
    min_value = convert_to_decimal(min_number)
    max_value = convert_to_decimal(max_number)

    # Zapisz wyniki do pliku
    with open('wyniki_6_5_bez_lambda.txt', 'w', encoding='utf-8') as file:
        file.write(f"Min: {min_number} (Wartość: {min_value})\n")
        file.write(f"Max: {max_number} (Wartość: {max_value})\n")



def main() -> None:
    numbers = read_numbers_from_file('liczby.txt')
    zadanie_6_1(numbers)
    zadanie_6_2(numbers)
    zadanie_6_3(numbers)
    zadanie_6_4(numbers)
    zadanie_6_5(numbers)
    zadanie_6_5_bez_lambda(numbers)


if __name__ == "__main__":
    main()