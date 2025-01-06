#include <iostream>
#include <string>
#include <algorithm>
#include <set>
#include <cstdio>

using namespace std;

int recursive_kaprekar(string k_in, int n_iter) {
    set<char> unique_digits(k_in.begin(), k_in.end());
    
    // Condición de parada: todos los dígitos son iguales
    if (unique_digits.size() <= 1) 
        return 8;
    // Condición de parada: se llega a 6174
    if (k_in == "6174") 
        return n_iter;

    // Añadir ceros a la izquierda si el número tiene menos de 4 dígitos
    while (k_in.length() < 4) 
        k_in += '0';

    // Ordenar los dígitos y calcular diferencia ascendente-descendente
    sort(k_in.begin(), k_in.end());
    string asc = k_in;
    string desc = k_in;
    reverse(desc.begin(), desc.end());
    int asc_val = stoi(asc);
    int desc_val = stoi(desc);
    int res = desc_val - asc_val;

    printf("%d - %d = %d\n", desc_val, asc_val, res);

    // Llamada recursiva
    return recursive_kaprekar(to_string(res), n_iter + 1);
}

int iterative_kaprekar(string k) {
    int res = -1, n_iter = 0;

    set<char> unique_digits(k.begin(), k.end());
    // Condición de parada: todos los dígitos son iguales
    if (unique_digits.size() <= 1) 
        return 8;

    while (res != 6174 && n_iter <= 7) {
        // Añadir ceros a la izquierda si el número tiene menos de 4 dígitos
        while (k.length() < 4) 
            k += '0';

        // Ordenar los dígitos
        sort(k.begin(), k.end());
        string asc = k;
        string desc = k;
        reverse(desc.begin(), desc.end());

        int asc_val = stoi(asc);
        int desc_val = stoi(desc);
        res = desc_val - asc_val;

        printf("%d - %d = %d\n", desc_val, asc_val, res);

        k = to_string(res);
        n_iter++;
    }

    return n_iter;
}

int main() {
    // Optimización de entrada/salida
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n_casos;
    scanf("%d", &n_casos);

    for (int i = 0; i < n_casos; ++i) {
        char k_in[5]; // Buffer para entrada
        scanf("%s", k_in);

        string k = k_in;
        // Añadir ceros a la izquierda si el número tiene menos de 4 dígitos
        while (k.length() < 4) 
            k += '0';

        sort(k.begin(), k.end());

        // Llamada a la función iterativa
        int result = iterative_kaprekar(k);

        printf("%d\n", result);
    }

    return 0;
}
