//https://aceptaelreto.com/problem/statement.php?id=114&potw=1

#include <cstdio>

// Array precomputado con los resultados de los últimos dígitos de los factoriales del 1 al 4
const char last_digits[] = {'1', '1', '2', '6', '4', '0'};

int main() {
    int n_casos;
    std::scanf("%d", &n_casos);

    char output[1000000]; // Buffer para salida masiva
    char* pos = output;

    while (n_casos--) {
        int n;
        std::scanf("%d", &n);
        *pos++ = last_digits[n >= 5 ? 5 : n];
        *pos++ = '\n';
    }

    std::fwrite(output, 1, pos - output, stdout); // Escribe todo el buffer de salida de una sola vez

    return 0;
}