#include <stdio.h>
#include <numeric>


void calculate(int N){
    int combinations = 0;
    for(int x=1; x < N; x++){
        for(int y=1; y < N; y++){
            for(int z=1; z < N; z++){
                if(x < y && y < z &&
                   x * x + y * y == z * z &&
                   std::gcd(std::gcd(x, y), z) == 1){
                        combinations += 1;
                }
            }
        }
    }
    printf("%d\n", combinations);
}

int main(){
    int N;
    while (scanf("%d", &N) && N){
        calculate(N);
    }
    return 0;
}
