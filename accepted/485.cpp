#include <iostream>
#include <vector>
#include <numeric>

int main() {
    int n_etapas;
    while (std::cin >> n_etapas && n_etapas != 0) {
        std::vector<int> etps(n_etapas);
        for (int i = 0; i < n_etapas; ++i) {
            std::cin >> etps[i];
        }

        std::vector<int> result(n_etapas);
        for (int e = 0; e < n_etapas; ++e) {
            result[e] = std::accumulate(etps.begin() + e, etps.end(), 0);
        }

        
        for (int i = 0; i < n_etapas; ++i) {
            std::cout << result[i];
            if (i != n_etapas - 1) std::cout << " ";
        }
        std::cout << std::endl;
    }
    return 0;
}