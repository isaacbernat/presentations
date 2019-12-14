#include <stdio.h>
#include <emmintrin.h>
#include <pthread.h>
#include <numeric>
#include <chrono>

#define NUMIO 128
#define READLINES (100000/NUMIO)/2 // NOTE: adjust the size to that of the input to be read. A smaller size will be slower, but a bigger will just not work.
#define MAXN 1048576
#define MAX_ITERS 726


#define read(R) scanf("%u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u",\
       &inputBuffer[R][0], &inputBuffer[R][1], &inputBuffer[R][2], &inputBuffer[R][3], &inputBuffer[R][4], &inputBuffer[R][5], &inputBuffer[R][6], &inputBuffer[R][7], &inputBuffer[R][8], &inputBuffer[R][9],\
       &inputBuffer[R][10], &inputBuffer[R][11], &inputBuffer[R][12], &inputBuffer[R][13], &inputBuffer[R][14], &inputBuffer[R][15], &inputBuffer[R][16], &inputBuffer[R][17], &inputBuffer[R][18], &inputBuffer[R][19],\
       &inputBuffer[R][20], &inputBuffer[R][21], &inputBuffer[R][22], &inputBuffer[R][23], &inputBuffer[R][24], &inputBuffer[R][25], &inputBuffer[R][26], &inputBuffer[R][27], &inputBuffer[R][28], &inputBuffer[R][29],\
       &inputBuffer[R][30], &inputBuffer[R][31], &inputBuffer[R][32], &inputBuffer[R][33], &inputBuffer[R][34], &inputBuffer[R][35], &inputBuffer[R][36], &inputBuffer[R][37], &inputBuffer[R][38], &inputBuffer[R][39],\
       &inputBuffer[R][40], &inputBuffer[R][41], &inputBuffer[R][42], &inputBuffer[R][43], &inputBuffer[R][44], &inputBuffer[R][45], &inputBuffer[R][46], &inputBuffer[R][47], &inputBuffer[R][48], &inputBuffer[R][49],\
       &inputBuffer[R][50], &inputBuffer[R][51], &inputBuffer[R][52], &inputBuffer[R][53], &inputBuffer[R][54], &inputBuffer[R][55], &inputBuffer[R][56], &inputBuffer[R][57], &inputBuffer[R][58], &inputBuffer[R][59],\
       &inputBuffer[R][60], &inputBuffer[R][61], &inputBuffer[R][62], &inputBuffer[R][63], &inputBuffer[R][64], &inputBuffer[R][65], &inputBuffer[R][66], &inputBuffer[R][67], &inputBuffer[R][68], &inputBuffer[R][69],\
       &inputBuffer[R][70], &inputBuffer[R][71], &inputBuffer[R][72], &inputBuffer[R][73], &inputBuffer[R][74], &inputBuffer[R][75], &inputBuffer[R][76], &inputBuffer[R][77], &inputBuffer[R][78], &inputBuffer[R][79],\
       &inputBuffer[R][80], &inputBuffer[R][81], &inputBuffer[R][82], &inputBuffer[R][83], &inputBuffer[R][84], &inputBuffer[R][85], &inputBuffer[R][86], &inputBuffer[R][87], &inputBuffer[R][88], &inputBuffer[R][89],\
       &inputBuffer[R][90], &inputBuffer[R][91], &inputBuffer[R][92], &inputBuffer[R][93], &inputBuffer[R][94], &inputBuffer[R][95], &inputBuffer[R][96], &inputBuffer[R][97], &inputBuffer[R][98], &inputBuffer[R][99],\
       &inputBuffer[R][100], &inputBuffer[R][101], &inputBuffer[R][102], &inputBuffer[R][103], &inputBuffer[R][104], &inputBuffer[R][105], &inputBuffer[R][106], &inputBuffer[R][107], &inputBuffer[R][108], &inputBuffer[R][109],\
       &inputBuffer[R][110], &inputBuffer[R][111], &inputBuffer[R][112], &inputBuffer[R][113], &inputBuffer[R][114], &inputBuffer[R][115], &inputBuffer[R][116], &inputBuffer[R][117], &inputBuffer[R][118], &inputBuffer[R][119],\
       &inputBuffer[R][120], &inputBuffer[R][121], &inputBuffer[R][122], &inputBuffer[R][123], &inputBuffer[R][124], &inputBuffer[R][125], &inputBuffer[R][126], &inputBuffer[R][127]);

#define write(R) printf("%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n%u\n",\
        results.final[inputBuffer[R][0]/4 + (inputBuffer[R][0]%4 > 0)], results.final[inputBuffer[R][1]/4 + (inputBuffer[R][1]%4 > 0)], results.final[inputBuffer[R][2]/4 + (inputBuffer[R][2]%4 > 0)], results.final[inputBuffer[R][3]/4 + (inputBuffer[R][3]%4 > 0)], results.final[inputBuffer[R][4]/4 + (inputBuffer[R][4]%4 > 0)], results.final[inputBuffer[R][5]/4 + (inputBuffer[R][5]%4 > 0)], results.final[inputBuffer[R][6]/4 + (inputBuffer[R][6]%4 > 0)], results.final[inputBuffer[R][7]/4 + (inputBuffer[R][7]%4 > 0)], results.final[inputBuffer[R][8]/4 + (inputBuffer[R][8]%4 > 0)], results.final[inputBuffer[R][9]/4 + (inputBuffer[R][9]%4 > 0)],\
        results.final[inputBuffer[R][10]/4 + (inputBuffer[R][10]%4 > 0)], results.final[inputBuffer[R][11]/4 + (inputBuffer[R][11]%4 > 0)], results.final[inputBuffer[R][12]/4 + (inputBuffer[R][12]%4 > 0)], results.final[inputBuffer[R][13]/4 + (inputBuffer[R][13]%4 > 0)], results.final[inputBuffer[R][14]/4 + (inputBuffer[R][14]%4 > 0)], results.final[inputBuffer[R][15]/4 + (inputBuffer[R][15]%4 > 0)], results.final[inputBuffer[R][16]/4 + (inputBuffer[R][16]%4 > 0)], results.final[inputBuffer[R][17]/4 + (inputBuffer[R][17]%4 > 0)], results.final[inputBuffer[R][18]/4 + (inputBuffer[R][18]%4 > 0)], results.final[inputBuffer[R][19]/4 + (inputBuffer[R][19]%4 > 0)],\
        results.final[inputBuffer[R][20]/4 + (inputBuffer[R][20]%4 > 0)], results.final[inputBuffer[R][21]/4 + (inputBuffer[R][21]%4 > 0)], results.final[inputBuffer[R][22]/4 + (inputBuffer[R][22]%4 > 0)], results.final[inputBuffer[R][23]/4 + (inputBuffer[R][23]%4 > 0)], results.final[inputBuffer[R][24]/4 + (inputBuffer[R][24]%4 > 0)], results.final[inputBuffer[R][25]/4 + (inputBuffer[R][25]%4 > 0)], results.final[inputBuffer[R][26]/4 + (inputBuffer[R][26]%4 > 0)], results.final[inputBuffer[R][27]/4 + (inputBuffer[R][27]%4 > 0)], results.final[inputBuffer[R][28]/4 + (inputBuffer[R][28]%4 > 0)], results.final[inputBuffer[R][29]/4 + (inputBuffer[R][29]%4 > 0)],\
        results.final[inputBuffer[R][30]/4 + (inputBuffer[R][30]%4 > 0)], results.final[inputBuffer[R][31]/4 + (inputBuffer[R][31]%4 > 0)], results.final[inputBuffer[R][32]/4 + (inputBuffer[R][32]%4 > 0)], results.final[inputBuffer[R][33]/4 + (inputBuffer[R][33]%4 > 0)], results.final[inputBuffer[R][34]/4 + (inputBuffer[R][34]%4 > 0)], results.final[inputBuffer[R][35]/4 + (inputBuffer[R][35]%4 > 0)], results.final[inputBuffer[R][36]/4 + (inputBuffer[R][36]%4 > 0)], results.final[inputBuffer[R][37]/4 + (inputBuffer[R][37]%4 > 0)], results.final[inputBuffer[R][38]/4 + (inputBuffer[R][38]%4 > 0)], results.final[inputBuffer[R][39]/4 + (inputBuffer[R][39]%4 > 0)],\
        results.final[inputBuffer[R][40]/4 + (inputBuffer[R][40]%4 > 0)], results.final[inputBuffer[R][41]/4 + (inputBuffer[R][41]%4 > 0)], results.final[inputBuffer[R][42]/4 + (inputBuffer[R][42]%4 > 0)], results.final[inputBuffer[R][43]/4 + (inputBuffer[R][43]%4 > 0)], results.final[inputBuffer[R][44]/4 + (inputBuffer[R][44]%4 > 0)], results.final[inputBuffer[R][45]/4 + (inputBuffer[R][45]%4 > 0)], results.final[inputBuffer[R][46]/4 + (inputBuffer[R][46]%4 > 0)], results.final[inputBuffer[R][47]/4 + (inputBuffer[R][47]%4 > 0)], results.final[inputBuffer[R][48]/4 + (inputBuffer[R][48]%4 > 0)], results.final[inputBuffer[R][49]/4 + (inputBuffer[R][49]%4 > 0)],\
        results.final[inputBuffer[R][50]/4 + (inputBuffer[R][50]%4 > 0)], results.final[inputBuffer[R][51]/4 + (inputBuffer[R][51]%4 > 0)], results.final[inputBuffer[R][52]/4 + (inputBuffer[R][52]%4 > 0)], results.final[inputBuffer[R][53]/4 + (inputBuffer[R][53]%4 > 0)], results.final[inputBuffer[R][54]/4 + (inputBuffer[R][54]%4 > 0)], results.final[inputBuffer[R][55]/4 + (inputBuffer[R][55]%4 > 0)], results.final[inputBuffer[R][56]/4 + (inputBuffer[R][56]%4 > 0)], results.final[inputBuffer[R][57]/4 + (inputBuffer[R][57]%4 > 0)], results.final[inputBuffer[R][58]/4 + (inputBuffer[R][58]%4 > 0)], results.final[inputBuffer[R][59]/4 + (inputBuffer[R][59]%4 > 0)],\
        results.final[inputBuffer[R][60]/4 + (inputBuffer[R][60]%4 > 0)], results.final[inputBuffer[R][61]/4 + (inputBuffer[R][61]%4 > 0)], results.final[inputBuffer[R][62]/4 + (inputBuffer[R][62]%4 > 0)], results.final[inputBuffer[R][63]/4 + (inputBuffer[R][63]%4 > 0)], results.final[inputBuffer[R][64]/4 + (inputBuffer[R][64]%4 > 0)], results.final[inputBuffer[R][65]/4 + (inputBuffer[R][65]%4 > 0)], results.final[inputBuffer[R][66]/4 + (inputBuffer[R][66]%4 > 0)], results.final[inputBuffer[R][67]/4 + (inputBuffer[R][67]%4 > 0)], results.final[inputBuffer[R][68]/4 + (inputBuffer[R][68]%4 > 0)], results.final[inputBuffer[R][69]/4 + (inputBuffer[R][69]%4 > 0)],\
        results.final[inputBuffer[R][70]/4 + (inputBuffer[R][70]%4 > 0)], results.final[inputBuffer[R][71]/4 + (inputBuffer[R][71]%4 > 0)], results.final[inputBuffer[R][72]/4 + (inputBuffer[R][72]%4 > 0)], results.final[inputBuffer[R][73]/4 + (inputBuffer[R][73]%4 > 0)], results.final[inputBuffer[R][74]/4 + (inputBuffer[R][74]%4 > 0)], results.final[inputBuffer[R][75]/4 + (inputBuffer[R][75]%4 > 0)], results.final[inputBuffer[R][76]/4 + (inputBuffer[R][76]%4 > 0)], results.final[inputBuffer[R][77]/4 + (inputBuffer[R][77]%4 > 0)], results.final[inputBuffer[R][78]/4 + (inputBuffer[R][78]%4 > 0)], results.final[inputBuffer[R][79]/4 + (inputBuffer[R][79]%4 > 0)],\
        results.final[inputBuffer[R][80]/4 + (inputBuffer[R][80]%4 > 0)], results.final[inputBuffer[R][81]/4 + (inputBuffer[R][81]%4 > 0)], results.final[inputBuffer[R][82]/4 + (inputBuffer[R][82]%4 > 0)], results.final[inputBuffer[R][83]/4 + (inputBuffer[R][83]%4 > 0)], results.final[inputBuffer[R][84]/4 + (inputBuffer[R][84]%4 > 0)], results.final[inputBuffer[R][85]/4 + (inputBuffer[R][85]%4 > 0)], results.final[inputBuffer[R][86]/4 + (inputBuffer[R][86]%4 > 0)], results.final[inputBuffer[R][87]/4 + (inputBuffer[R][87]%4 > 0)], results.final[inputBuffer[R][88]/4 + (inputBuffer[R][88]%4 > 0)], results.final[inputBuffer[R][89]/4 + (inputBuffer[R][89]%4 > 0)],\
        results.final[inputBuffer[R][90]/4 + (inputBuffer[R][90]%4 > 0)], results.final[inputBuffer[R][91]/4 + (inputBuffer[R][91]%4 > 0)], results.final[inputBuffer[R][92]/4 + (inputBuffer[R][92]%4 > 0)], results.final[inputBuffer[R][93]/4 + (inputBuffer[R][93]%4 > 0)], results.final[inputBuffer[R][94]/4 + (inputBuffer[R][94]%4 > 0)], results.final[inputBuffer[R][95]/4 + (inputBuffer[R][95]%4 > 0)], results.final[inputBuffer[R][96]/4 + (inputBuffer[R][96]%4 > 0)], results.final[inputBuffer[R][97]/4 + (inputBuffer[R][97]%4 > 0)], results.final[inputBuffer[R][98]/4 + (inputBuffer[R][98]%4 > 0)], results.final[inputBuffer[R][99]/4 + (inputBuffer[R][99]%4 > 0)],\
        results.final[inputBuffer[R][100]/4 + (inputBuffer[R][100]%4 > 0)], results.final[inputBuffer[R][101]/4 + (inputBuffer[R][101]%4 > 0)], results.final[inputBuffer[R][102]/4 + (inputBuffer[R][102]%4 > 0)], results.final[inputBuffer[R][103]/4 + (inputBuffer[R][103]%4 > 0)], results.final[inputBuffer[R][104]/4 + (inputBuffer[R][104]%4 > 0)], results.final[inputBuffer[R][105]/4 + (inputBuffer[R][105]%4 > 0)], results.final[inputBuffer[R][106]/4 + (inputBuffer[R][106]%4 > 0)], results.final[inputBuffer[R][107]/4 + (inputBuffer[R][107]%4 > 0)], results.final[inputBuffer[R][108]/4 + (inputBuffer[R][108]%4 > 0)], results.final[inputBuffer[R][109]/4 + (inputBuffer[R][109]%4 > 0)],\
        results.final[inputBuffer[R][110]/4 + (inputBuffer[R][110]%4 > 0)], results.final[inputBuffer[R][111]/4 + (inputBuffer[R][111]%4 > 0)], results.final[inputBuffer[R][112]/4 + (inputBuffer[R][112]%4 > 0)], results.final[inputBuffer[R][113]/4 + (inputBuffer[R][113]%4 > 0)], results.final[inputBuffer[R][114]/4 + (inputBuffer[R][114]%4 > 0)], results.final[inputBuffer[R][115]/4 + (inputBuffer[R][115]%4 > 0)], results.final[inputBuffer[R][116]/4 + (inputBuffer[R][116]%4 > 0)], results.final[inputBuffer[R][117]/4 + (inputBuffer[R][117]%4 > 0)], results.final[inputBuffer[R][118]/4 + (inputBuffer[R][118]%4 > 0)], results.final[inputBuffer[R][119]/4 + (inputBuffer[R][119]%4 > 0)],\
        results.final[inputBuffer[R][120]/4 + (inputBuffer[R][120]%4 > 0)], results.final[inputBuffer[R][121]/4 + (inputBuffer[R][121]%4 > 0)], results.final[inputBuffer[R][122]/4 + (inputBuffer[R][122]%4 > 0)], results.final[inputBuffer[R][123]/4 + (inputBuffer[R][123]%4 > 0)], results.final[inputBuffer[R][124]/4 + (inputBuffer[R][124]%4 > 0)], results.final[inputBuffer[R][125]/4 + (inputBuffer[R][125]%4 > 0)], results.final[inputBuffer[R][126]/4 + (inputBuffer[R][126]%4 > 0)], results.final[inputBuffer[R][127]/4 + (inputBuffer[R][127]%4 > 0)]);

volatile unsigned int lines_read = 0;
volatile unsigned int lines_read2 = 0;
volatile unsigned int lines_written = 0;

unsigned char memGCD[MAXN -1][MAX_ITERS];

union {
    unsigned char gcd[MAXN];
    unsigned int final[MAXN / 4];
} __attribute__((__aligned__(16))) results;

unsigned int inputBuffer[READLINES][NUMIO];

// int gcd(int x, int y) {
//     if (memGCD[x][y] == 0) {
//         if (y != 0) memGCD[x][y] = gcd(y, x%y);
//         else memGCD[x][y] = 2 - (x == 1);
//     }
//     return memGCD[x][y];
// }

int gcd_eq1(int x, int y) {
    if (memGCD[x][y] == 0) {
        memGCD[x][y] = std::gcd(x, y) == 1;
    }
    return memGCD[x][y];
}

void* calculate(void* id) {
    unsigned int m, n, m2, n2, f, c1, c2, c3, c4;
    unsigned char next, actual = 1;
    __m128i* pSum;

    c2 = 1;
    do {
        n = c2;
        do {
            n2 = n*n;
            m = n + 1;
            f = MAXN - n2;
            for (m2 = m*m; m2 <= f; m += 2, m2 = m*m) {
                results.gcd[m2 + n2] += (gcd_eq1(m, n));
            }
            n += 2;
        } while (n < MAX_ITERS);

    } while (++c2 <= 2);

    results.final[1] = 0;
    results.final[2] = 1;
    results.final[3] = 1;
    pSum = (__m128i*) &results.final[4];
    n = 13;

    do {
        next = results.gcd[n + 16];
        c1 = results.final[n/4] + actual;
        c2 = c1 + results.gcd[n + 4];
        c3 = c2 + results.gcd[n + 8];
        c4 = c3 + results.gcd[n + 12];
        *pSum = _mm_set_epi32(c4, c3, c2, c1);
        actual = next; ++pSum; n += 16;
    } while (n <= MAXN);


    do {
        while (lines_read <= lines_written);
        write(lines_written);
    } while (++lines_written < READLINES);

    n = 0;
    do {
        while (lines_read2 <= n);
        write(n);
    } while (++n < READLINES);

    scanf("%u", &n);
    do {
        printf("%u\n", results.final[n/4 + (n%4 > 0)]);
        scanf("%u", &n);
    } while (n != 0);

    pthread_exit(NULL);
}

int main() {
    pthread_t thread;
    // auto start = std::chrono::steady_clock::now();
    pthread_create(&thread, NULL, calculate, NULL);

    do {
        read(lines_read);
    } while (++lines_read < READLINES);

    do {
        while (lines_read2 >= lines_written);
        read(lines_read2);
    } while (++lines_read2 < READLINES);

    pthread_join(thread, NULL);
    // auto end = std::chrono::steady_clock::now();

    // fprintf(stderr, "%lld\n", std::chrono::duration_cast<std::chrono::microseconds>(end - start).count());
}
