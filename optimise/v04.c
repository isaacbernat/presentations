#include <stdio.h>
#include <numeric>


void calculate(int N){
    int combinations = 0;
    int xx, yy;
    for(int x=2; x < N; x++){
        xx = x*x;
        for(int y=x+1; y < N; y++){
            yy = y*y;
            for(int z=y+1; z < N; z++){
                if(x < y && y < z &&
                   xx + yy == z * z &&
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
