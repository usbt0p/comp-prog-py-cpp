#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

int main() {
    int n_cases;
    cin >> n_cases;
    cin.ignore(); // Ignore the newline after the number

    for (int i = 0; i < n_cases; ++i) {
        string time_str;
        getline(cin, time_str);

        int h, m, s;
        sscanf(time_str.c_str(), "%d:%d:%d", &h, &m, &s);

        int total = h * 3600 + m * 60 + s;
        int start = 24 * 3600 - total;
        int sh = start / 3600;
        int sm = (start % 3600) / 60;
        int ss = start % 60;

        cout << setfill('0') << setw(2) << sh << ":"
             << setfill('0') << setw(2) << sm << ":"
             << setfill('0') << setw(2) << ss << endl;
    }
    return 0;
}