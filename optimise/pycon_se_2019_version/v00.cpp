#include <stdio.h>
#include <cmath>


int euclidean_gcd(int a, int b){
    int t;
    while (b != 0){
        t = b;
        b = a % b;
        a = t;
    }
    return a;
}


int main(){
    int N, combinations;
    while (scanf("%d", &N) && N){
        combinations = 0;
        for(int x=1; x < N; x++){
            for(int y=1; y < N; y++){
                for(int z=1; z < N; z++){
                    if(euclidean_gcd(euclidean_gcd(x, y), z) == 1 &&
                       std::pow(x, 2) + std::pow(y, 2) == std::pow(z, 2) &&
                       x < y && y < z){
                            combinations += 1;
                    }
                }
            }
        }
        printf("%d\n", combinations);
    }
    return 0;
}
