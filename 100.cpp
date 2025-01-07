//https://aceptaelreto.com/problem/statement.php?id=100

/*
5
3524
1111
1121
6174
1893

*/

#include <iostream>
#include <string>
#include <algorithm>
#include <set>

#include <cstdio>

using namespace std;

int recursive_kaprekar(string k_in, int n_iter) {
    
    // Añadir ceros a la izquierda si el número tiene menos de 4 dígitos
    while (k_in.length() < 4) 
        k_in += '0';
    
    set<char> unique_digits(k_in.begin(), k_in.end());
    
    // Condición de parada: todos los dígitos son iguales
    if (unique_digits.size() <= 1) 
        return 8;
    // Condición de parada: se llega a 6174
    if (k_in == "6174") 
        return n_iter;


    // Ordenar los dígitos y calcular diferencia ascendente-descendente
    sort(k_in.begin(), k_in.end());
    string asc = k_in;
    string desc = k_in;
    reverse(desc.begin(), desc.end());
    int asc_val = stoi(asc);
    int desc_val = stoi(desc);
    int res = desc_val - asc_val;

    //cout << desc_val << " - " << asc_val << " = " << res << endl;

    // Llamada recursiva
    return recursive_kaprekar(to_string(res), n_iter + 1);
}

int iterative_kaprekar(string k) {
    int res = -1, n_iter = 0;

    set<char> unique_digits(k.begin(), k.end());
    // Condición de parada: todos los dígitos son iguales
    if (unique_digits.size() <= 1) 
        return 8;

    while (res != 6174 && n_iter <= 7 && k != "6174") {
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
        printf("k = %s\n", k.c_str());

        // Llamada a la función iterativa
        int result = iterative_kaprekar(k_in);
        //int result = recursive_kaprekar(k_in, 0);

        printf("%d\n", result);
    }

    return 0;
}

// TODO: caso de error: 3 VS. 10
// TODO comprobar si en vez de k += '0' es k = '0' + k