#include <stdio.h>
#include <numeric>
#include <cmath>


#define MAXN 1048576
#define MAX_ITERS 1024

int memGCD[MAXN -1][MAX_ITERS];

int gcd(int x, int y) {
    if (memGCD[x][y] == 0) {
        memGCD[x][y] = std::gcd(x, y);
    }
    return memGCD[x][y];
}

void process(int N){
    int combinations = 0;
    int max_iter = std::sqrt(N) + 1;
    for(long int x=1; x < max_iter; x++){
        int xxN = std::sqrt(N - x*x);
        for(long int y=x+1; y < max_iter+1; y+=2){
            if(gcd(x, y) != 1){
                continue;
            } 
            if(y > xxN){
                y = N + 1;
                break;
            }
            combinations += 1;
        }
    }
    printf("%d\n", combinations);
    return;
}

int main(){
    int N;
    while (scanf("%d", &N) && N){
        process(N);
    }
    return 0;
}
