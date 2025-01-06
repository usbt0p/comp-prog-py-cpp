#include <iostream>
#include <string>
#include <algorithm>
#include <set>

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

    cout << desc_val << " - " << asc_val << " = " << res << endl;

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

        cout << desc_val << " - " << asc_val << " = " << res << endl;

        k = to_string(res);
        n_iter++;
    }

    return n_iter;
}

int main() {
    int n_casos;
    cin >> n_casos;

    for (int i = 0; i < n_casos; ++i) {
        string k_in;
        cin >> k_in;

        // Añadir ceros a la izquierda si el número tiene menos de 4 dígitos
        while (k_in.length() < 4) 
            k_in += '0';

        sort(k_in.begin(), k_in.end());

        // Llamada a la función iterativa
        int result = iterative_kaprekar(k_in);

        cout << result << endl;
    }

    return 0;
}
