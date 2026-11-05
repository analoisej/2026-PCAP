/*
 * Disciplina: 2026-PCAP
 * Problema  : beecrowd 2165 - Twitting 
 * Autor     : Ana Loise Jovino Prado

*/

#include <iostream> 
#include <string>
using namespace std;

int main() {
    string texto;

    getline(cin, texto);
    if (texto.size() <= 140) {
        cout << "TWEET" << endl;
    } else {
        cout << "MUTE" << endl;
    }

    return 0;
}