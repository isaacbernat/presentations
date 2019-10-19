#include <stdio.h>
#include <numeric>
#include <cmath>
#include <map>
#include <unordered_map>

#define MAXN 1048576
#define MAX_ITERS 1024

std::unordered_map<int,int> RESULT;
// N.b. this is much slower than `int RESULT[MAXN];` used in v13.c
// In v1337.c struct unions are used to reduce memory footprint.
// But in this example, to have an algorithm as comparable as possible to that
// used in v14.py `map` is used as an analogous datatype do `dict`.

// N.b. memoisation is not used here, even if it provided a speedup, because it
// is also discarded in the python version, and this way is more comparable.
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
            RESULT[(xx + y*y -1)/4] += 1;
        }
    }
    for(int i=1; i<MAXN/4; i++){
        RESULT[i] += RESULT[i -1];
    }
    return;
}


int main(){
    int N;
    preprocess(MAXN);
    while (scanf("%d", &N) && N){
        printf("%d\n", RESULT[(N -1)/4]);
    }
    return 0;
}
