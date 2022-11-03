#include <stdio.h>

int func(int a, int b) { 
    int x;
    x = a + b;
    printf("i%", x);
}
int main() {
    func(2, 3);
 }