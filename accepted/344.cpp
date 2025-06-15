#include <iostream>
#include <vector>
#include <string>

int main() {
    int n;
    std::cin >> n;

    for (int i = 0; i < n; ++i) {
        int n_cables;
        std::cin >> n_cables;

        std::vector<std::string> cables(n_cables);
        for (int j = 0; j < n_cables; ++j) {
            std::cin >> cables[j];
        }

        int male_ct = 0, female_ct = 0;

        for (const auto& c : cables) {
            if (c[0] == 'M') {
                male_ct++;
            } else {
                female_ct++;
            }
            if (c[1] == 'M') {
                male_ct++;
            } else {
                female_ct++;
            }
        }

        if (male_ct == female_ct) {
            std::cout << "POSIBLE" << std::endl;
        } else {
            std::cout << "IMPOSIBLE" << std::endl;
        }
    }

    return 0;
}
