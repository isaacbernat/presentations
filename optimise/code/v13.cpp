#include <stdio.h>
#include <numeric>
#include <cmath>

#define MAXN 1048576
#define MAX_ITERS 1024

int RESULT[MAXN];

// int memGCD[MAXN -1][MAX_ITERS];

// int gcd(int x, int y) {
//     if (memGCD[x][y] == 0) {
//         memGCD[x][y] = std::gcd(x, y);
//     }
//     return memGCD[x][y];
// }

void preprocess(int N){
    int combinations = 0;
    int max_iter = std::sqrt(N) + 1;
    for(long int x=1; x < max_iter; x++){
        long int xx = x * x;
        int xxN = std::sqrt(N - xx);
        for(long int y=x+1; y < max_iter+1; y+=2){
            if(std::gcd(x, y) != 1){
                continue;
            }
            if(y > xxN){
                y = N + 1;
                break;
            }
            RESULT[xx + y*y] += 1;
        }
    }
    for(int i=1; i<MAXN+1; i++){
        RESULT[i] += RESULT[i -1];
    }
    return;
}


int main(){
    int N;
    preprocess(MAXN);
    while (scanf("%d", &N) && N){
        printf("%d\n", RESULT[N]);
    }
    return 0;
}
