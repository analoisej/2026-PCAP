/*
 * Disciplina: 2026-PCAP
 * Problema  : beecrowd 1002 - Área do Circulo 
 * Autor     : Ana Loise Jovino Prado

*/

#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double r, area;

    cin >> r;

    area = 3.14159 * r * r;

    cout << fixed << setprecision(4);
    cout << "A=" << area << endl;

    return 0;
}