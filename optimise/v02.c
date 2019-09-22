#include <stdio.h>
#include <numeric>


int main(){
    int N, combinations;
    while (scanf("%d", &N) && N){
        combinations = 0;
        for(int x=1; x < N; x++){
            for(int y=1; y < N; y++){
                for(int z=1; z < N; z++){
                    if(std::gcd(std::gcd(x, y), z) == 1 &&
                       x * x + y * y == z * z &&
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
