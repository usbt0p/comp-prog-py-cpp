#include <iostream>
using namespace std;

void func(){
    int n, up, down, updown; 
    cin >> n; 

    int data[4] = {0,0,0,0};

    for (int i = 0; i < n; i++) {
         // there must be some better way to do this in c++
        for (int j = 0; j < 4; j++) {
            cin >> data[j];
        }
        
        up = data[0] * data[1];
        down = data[2] * data[1] + data[3];
        updown = up +  down;
        
        cout << down << " " << updown << "\n";

    }   
}

int main(){
    func();
    return 0;
}


