#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

int main() {
    int n_etapas;
    while (std::cin >> n_etapas && n_etapas != 0) {
        std::vector<int> out;
        int adder = 0;
        std::string line;
        std::getline(std::cin, line); // consume leftover newline
        std::getline(std::cin, line);

        for (char ch : line) {
            if (ch != ' ' && ch != '\n') {
                adder += ch - '0';
                out.push_back(adder);
            }
        }

        std::reverse(out.begin(), out.end());
        for (size_t i = 0; i < out.size(); ++i) {
            std::cout << out[i];
            if (i + 1 < out.size()) std::cout << " ";
        }
        std::cout << std::endl;
    }
    return 0;
}