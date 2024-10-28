// Z funckjami wbudowanymi

#include <iostream>
#include <string>
#include <bitset>
#include <sstream>

void dec_to_bin(int liczba) {
    // Zamienia liczbę dziesiętną na liczbę dwójkową (binarną).
    std::cout << std::bitset<32>(liczba) << std::endl; // 32-bitowa reprezentacja binarna
}

void dec_to_oct(int liczba) {
    // Zamienia liczbę dziesiętną na liczbę ósemkową (oktalną).
    std::cout << std::oct << liczba << std::dec << std::endl; // Wyświetl jako ósemkową
}

void dec_to_hex(int liczba) {
    // Zamienia liczbę dziesiętną na liczbę szesnastkową (heksadecymalną).
    std::cout << std::hex << liczba << std::dec << std::endl; // Wyświetl jako heksadecymalną
}

void bin_to_dec(const std::string& liczba_bin) {
    // Zamienia liczbę dwójkową na liczbę dziesiętną.
    std::cout << std::stoi(liczba_bin, nullptr, 2) << std::endl;
}

void oct_to_dec(const std::string& liczba_oct) {
    // Zamienia liczbę ósemkową na liczbę dziesiętną.
    std::cout << std::stoi(liczba_oct, nullptr, 8) << std::endl;
}

void hex_to_dec(const std::string& liczba_hex) {
    // Zamienia liczbę szesnastkową na liczbę dziesiętną.
    std::cout << std::stoi(liczba_hex, nullptr, 16) << std::endl;
}

void x_to_dec(const std::string& liczba_x, int system) {
    // Zamienia liczbę z dowolnego systemu na liczbę dziesiętną.
    std::cout << std::stoi(liczba_x, nullptr, system) << std::endl;
}

int main() {
    // Deklaracja main =/= uruchomienie go

    // Liczby dziesiętne
    std::cout << "Podaj liczbę dziesiętną: ";
    int inp;
    std::cin >> inp;

    dec_to_bin(inp);
    dec_to_oct(inp);
    dec_to_hex(inp);

    // Liczba binarna
    std::cout << "Podaj liczbę binarną (np. 10101): ";
    std::string inp_bin;
    std::cin >> inp_bin;
    bin_to_dec(inp_bin);

    // Liczba oktalna
    std::cout << "Podaj liczbę octalną (np. 17171): ";
    std::string inp_oct;
    std::cin >> inp_oct;
    oct_to_dec(inp_oct);

    // Liczba heksadecymalna
    std::cout << "Podaj liczbę heksadecymalną (np. ABCDF): ";
    std::string inp_hex;
    std::cin >> inp_hex;
    hex_to_dec(inp_hex);

    // Liczba w dowolnym systemie
    std::cout << "Podaj liczbę w dowolnym systemie: ";
    std::string inp_x;
    std::cin >> inp_x;
    std::cout << "Podaj system liczbowy (np. 3 to trójkowy): ";
    int base;
    std::cin >> base;
    x_to_dec(inp_x, base);

    return 0;
}