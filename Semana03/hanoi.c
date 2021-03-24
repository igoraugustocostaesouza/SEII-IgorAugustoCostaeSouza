/*Igor Augusto 11221EMT008*/
#include <bits/stdc++.h>
using namespace std;

void Hanoi(int n, char from_haste,
                    char to_haste, char aux_haste)
{
    if (n == 1)
    {
        cout << "move disco 1 da haste " << from_haste <<
                            " para a haste " << to_haste<<endl;
        return;
    }
    Hanoi(n - 1, from_haste, aux_haste, to_haste);
    cout << "move disco" << n << " da haste " << from_haste <<
                                " para a haste " << to_haste << endl;
    Hanoi(n - 1, aux_haste, to_haste, from_haste);
}

int main(int argc, char* argv[])
{

    int n= atoi(argv[1]);
    Hanoi(n, 'A', 'C', 'B'); // A B C são as hastes
    return 0;
}
