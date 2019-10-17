#include <stdio.h>
#include <numeric>


void process(int N){
    int combinations = 0;
    int xx, yy;
    for(int x=2; x < N; x+=2){
        xx = x*x;
        for(int y=x+1; y < N; y+=2){
            yy = y*y;
            for(int z=y+2; z < N; z+=2){
                if(x < y && y < z &&
                   xx + yy == z * z &&
                   std::gcd(std::gcd(x, y), z) == 1){
                        combinations += 1;
                }
            }
        }
    }

    for(int x=3; x < N; x+=2){
        xx = x*x;
        for(int y=x+1; y < N; y+=2){
            yy = y*y;
            for(int z=y+1; z < N; z+=2){
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
        process(N);
    }
    return 0;
}
