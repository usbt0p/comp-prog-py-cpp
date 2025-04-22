#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

unordered_map<char, string> morse = {
    {'A', ".-"}, {'B', "-..."}, {'C', "-.-."}, {'D', "-.."}, {'E', "."},
    {'F', "..-."}, {'G', "--."}, {'H', "...."}, {'I', ".."}, {'J', ".---"},
    {'K', "-.-"}, {'L', ".-.."}, {'M', "--"}, {'N', "-."}, {'O', "---"},
    {'P', ".--."}, {'Q', "--.-"}, {'R', ".-."}, {'S', "..."}, {'T', "-"},
    {'U', "..-"}, {'V', "...-"}, {'W', ".--"}, {'X', "-..-"}, {'Y', "-.--"},
    {'Z', "--.."}, {'!', "-.-.--"}, {'?', "..--.."}
};

int duration(const string& morse_code) {
    int dur = 0;
    for (size_t i = 0; i < morse_code.size(); ++i) {
        if (morse_code[i] == '-') {
            dur += 3;
        } else {
            dur += 1;
        }
        dur += 1; // Separación entre símbolos
    }
    dur -= 1; // Quitar la última suma
    return dur;
}

int main() {
    int n_casos;
    cin >> n_casos;
    cin.ignore(); // Ignorar el salto de línea después del número de casos

    vector<string> casos(n_casos);
    for (int i = 0; i < n_casos; ++i) {
        getline(cin, casos[i]);
    }

    for (const string& msg : casos) {
        int dur = 0;
        for (size_t i = 0; i < msg.size(); ++i) {
            char letra = msg[i];
            if (letra != ' ') {
                dur += duration(morse[letra]);
                if (i + 1 < msg.size() && msg[i + 1] != ' ') {
                    dur += 3; // Separación entre letras
                }
            } else {
                dur += 5; // Separación entre palabras
            }
        }
        cout << dur << endl;
    }

    return 0;
}