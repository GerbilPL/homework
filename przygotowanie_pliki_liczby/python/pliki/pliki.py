# importujemy os
import os

"""
 Tutaj są inne rzeczy niż w mat.roz.2016.systemy_liczbowe.py
 Tam jest zapis i odczyt z pliku
"""

def test()->None:
    # sprawdzamy czy plik istnieje
    if os.path.exists("test.txt"):
        print("Plik istnieje!")
        os.rename("test.txt","test_test.txt")
        if not os.path.exists("test"):
            os.mkdir("test")
        # Można też użyć rename i replace to przenoszenia plików.
        # Replace podmienia plik
        try:
            # btw zawsze dajemy ukośnik '/' nawet na windowsie (na windzie tez mozna uzywac tego ukosnika normalnie w cmd)
            # ponieważ '\' ten ukośnik oznaczałby jakiś znak kontrolny np. \n
            os.rename("test_test.txt","test/test.txt")
        except:
            try:
                os.replace("test_test.txt","test/test.txt")
            except:
                print("Nie udało się przenieść pliku.")
        # jeżeli chemy usunąć całe drzewo katalogu test, musimy usunąć wszystkie wpisy w środku
        # można też zaimportować 'shutil' i użyć shutil.rmtree('test')
        os.remove("test/test.txt")
        os.rmdir("test")
        #tworzenie pliku
        with open("test.txt", "w") as file:
            file.write("123")
        # Jeżeli wszystko poszło dobrze to nie powinno być żadnych errorów
    else:
        print("Plik nie istnieje!")
        # tworzymy plik
        with open("test.txt", "w") as file:
            file.write("123")
        # odpalamy test
        test()

if __name__=="__main__":
    test()