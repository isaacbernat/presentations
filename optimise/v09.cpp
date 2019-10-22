#include <stdio.h>
#include <numeric>
#include <cmath>


void process(int N){
    int combinations = 0;
    int max_iter = std::sqrt(N) + 1;
    for(long int x=1; x < max_iter; x++){
        for(long int y=x+1; y < max_iter+1; y+=2){
            if(std::gcd(x, y) != 1){
                continue;
            } 
            if ((x*x + y*y) > N){
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
