#include <iostream>
#include <fstream>
#include <vector>
#include <string>
// Da się bez algorithm ale większy ból bo sami musimy np. usunąć whitespace
#include <algorithm>

std::vector<std::string> read_numbers_from_file(const std::string& file_name) {
    std::vector<std::string> numbers;
    std::ifstream file(file_name);
    std::string line;
    while (std::getline(file, line)) {
        line.erase(remove_if(line.begin(), line.end(), isspace), line.end()); // Usuwamy whitespace
        if (!line.empty()) {
            numbers.push_back(line);
        }
    }
    return numbers;
}

void zadanie_6_1(const std::vector<std::string>& numbers) {
    int count = 0;
    // Dla każdego numeru w numbers
    for (const auto& number : numbers) {
        if (number.back() == '8') {
            ++count;
        }
    }
    std::ofstream file("wyniki_6_1.txt");
    file << count;
}

void zadanie_6_2(const std::vector<std::string>& numbers) {
    int count = 0;
    for (const auto& number : numbers) {
        if (number.back() == '4' && number.find('0') == std::string::npos) {
            ++count;
        }
    }
    std::ofstream file("wyniki_6_2.txt");
    file << count;
}

void zadanie_6_3(const std::vector<std::string>& numbers) {
    int count = 0;
    for (const auto& number : numbers) {
        if (number.size() >= 2 && number.back() == '2' && number[number.size() - 2] == '0') {
            ++count;
        }
    }
    std::ofstream file("wyniki_6_3.txt");
    file << count;
}

void zadanie_6_4(const std::vector<std::string>& numbers) {
    int total_sum = 0;
    for (const auto& number : numbers) {
        if (number.back() == '8') {
            int base_8_number = std::stoi(number.substr(0, number.size() - 1), nullptr, 8);
            total_sum += base_8_number;
        }
    }
    std::ofstream file("wyniki_6_4.txt");
    file << total_sum;
}

void zadanie_6_5(const std::vector<std::string>& numbers) {
    // lambda jak w pythonie
    auto base_convert = [](const std::string& number) -> int {
        int base = number.back() - '0';
        return std::stoi(number.substr(0, number.size() - 1), nullptr, base);
    };

    auto min_it = std::min_element(numbers.begin(), numbers.end(),
                                   [&](const std::string& a, const std::string& b) {
                                       return base_convert(a) < base_convert(b);
                                   });
    auto max_it = std::max_element(numbers.begin(), numbers.end(),
                                   [&](const std::string& a, const std::string& b) {
                                       return base_convert(a) < base_convert(b);
                                   });

    std::ofstream file("wyniki_6_5.txt");
    if (min_it != numbers.end() && max_it != numbers.end()) {
        file << "Min: " << *min_it << " (Wartość: " << base_convert(*min_it) << ")\n";
        file << "Max: " << *max_it << " (Wartość: " << base_convert(*max_it) << ")\n";
    }
}

// Potrzebne jeżeli chcemy 6_5 bez lambdy
int convert_to_decimal(const std::string& number) {
    int base = number.back() - '0';
    return std::stoi(number.substr(0, number.size() - 1), nullptr, base);
}


void zadanie_6_5_bez_lambda(const std::vector<std::string>& numbers) {
    std::string min_number, max_number;
    int min_value = __INT32_MAX__;
    int max_value = 0;

    for (const auto& number : numbers) {
        int decimal_value = convert_to_decimal(number);

        if (decimal_value < min_value) {
            min_value = decimal_value;
            min_number = number;
        }

        if (decimal_value > max_value) {
            max_value = decimal_value;
            max_number = number;
        }
    }

    std::ofstream file("wyniki_6_5.txt");
    if (file.is_open()) {
        file << "Min: " << min_number << " (Wartość: " << min_value << ")\n";
        file << "Max: " << max_number << " (Wartość: " << max_value << ")\n";
    }
}

int main() {
    std::vector<std::string> numbers = read_numbers_from_file("liczby.txt");
    zadanie_6_1(numbers);
    zadanie_6_2(numbers);
    zadanie_6_3(numbers);
    zadanie_6_4(numbers);
    zadanie_6_5(numbers);
    return 0;
}