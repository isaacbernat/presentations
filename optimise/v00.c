#include <stdio.h>
#include <numeric>
#include <cmath>


int calculate(int N){
    int combinations = 0;
    for(int x=1; x < N; x++){
        for(int y=1; y < N; y++){
            for(int z=1; z < N; z++){
                if(std::gcd(std::gcd(x, y), z) == 1 &&
                   std::pow(x, 2) + std::pow(y, 2) == std::pow(z, 2) &&
                   x < y && y < z){
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
