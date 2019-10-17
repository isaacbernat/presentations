#include <stdio.h>
#include <numeric>


void process(int N){
    int combinations = 0;
    for(long int x=1; x < N; x++){
        for(long int y=x+1; y < N; y+=2){
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
