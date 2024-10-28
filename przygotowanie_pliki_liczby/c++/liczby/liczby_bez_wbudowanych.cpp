#include <iostream>
#include <vector>
#include <string>

void dec_to_bin(int liczba) {
    std::vector<int> binarka;

    if (liczba == 0) {
        std::cout << 0 << std::endl;
        return;
    }

    while (liczba != 0) {
        binarka.push_back(liczba % 2);
        liczba /= 2;
    }

    // Musimy pamiętać że czytamy od końca
    // Iteracja od tyłu
    for (int i = binarka.size() - 1; i >= 0; --i) {
        std::cout << binarka[i];
    }
    std::cout << std::endl;
}

void dec_to_oct(int liczba) {
    std::string oktalka;

    if (liczba == 0) {
        std::cout << 0 << std::endl;
        return;
    }

    while (liczba != 0) {
        oktalka += std::to_string(liczba % 8);
        liczba /= 8;
    }

    // Wyświetlanie od tyłu
    for (int i = oktalka.size() - 1; i >= 0; --i) {
        std::cout << oktalka[i];
    }
    std::cout << std::endl;
}

void dec_to_hex(int liczba) {
    std::string hexalka;

    if (liczba == 0) {
        std::cout << 0 << std::endl;
        return;
    }

    while (liczba != 0) {
        int res = liczba % 16;
        if (res < 10) {
            hexalka += std::to_string(res);
        } else {
            hexalka += (res - 10) + 'A'; // Zamiana na znak A-F
        }
        liczba /= 16;
    }

    // Wyświetlanie od tyłu
    for (int i = hexalka.size() - 1; i >= 0; --i) {
        std::cout << hexalka[i];
    }
    std::cout << std::endl;
}

void bin_to_dec(const std::vector<int>& liczba_bin) {
    int decymalka = 0;
    for (int x : liczba_bin) {
        decymalka = decymalka * 2 + x;
    }
    std::cout << decymalka << std::endl;
}

void oct_to_dec(const std::vector<int>& liczba_oct) {
    int decymalka = 0;
    for (int x : liczba_oct) {
        decymalka = decymalka * 8 + x;
    }
    std::cout << decymalka << std::endl;
}

void hex_to_dec(const std::string& liczba_hex) {
    int decymalka = 0;
    for (char x : liczba_hex) {
        int value;
        if (x >= '0' && x <= '9') {
            value = x - '0';
        } else if (x >= 'A' && x <= 'F') {
            value = (x - 'A') + 10; // Zamiana A-F na 10-15
        } else if (x >= 'a' && x <= 'f') {
            value = (x - 'a') + 10; // Zamiana a-f na 10-15
        } else {
            std::cerr << "Błędny znak w heksadecymalnej liczbie: " << x << std::endl;
            return;
        }
        decymalka = decymalka * 16 + value;
    }
    std::cout << decymalka << std::endl;
}

int main() {
    int inp;
    std::cout << "Podaj liczbę dziesiętną: ";
    std::cin >> inp;

    dec_to_bin(inp);
    dec_to_oct(inp);
    dec_to_hex(inp);

    std::cout << "Podaj liczbę binarną (np. 10101): ";
    std::vector<int> bin_input;
    std::string bin_str;
    std::cin >> bin_str;
    for (char c : bin_str) {
        bin_input.push_back(c - '0');
    }
    bin_to_dec(bin_input);

    std::cout << "Podaj liczbę oktalną (np. 14): ";
    std::vector<int> oct_input;
    oct_input.push_back(1);
    oct_input.push_back(4); // Można również ustawić manualnie
    oct_to_dec(oct_input);

    std::cout << "Podaj liczbę heksadecymalną (np. ABCDF): ";
    std::string hex_input;
    std::cin >> hex_input;
    hex_to_dec(hex_input);

    return 0;
}