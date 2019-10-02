#include <chrono>
#include <tuple>
#include <vector>

const int N = 1048576;
int cache[N];

void precalc() {
    const int A[3 * 3] = {1, -2, 2, 2, -1, 2, 2, -2, 3};
    const int B[3 * 3] = {1, 2, 2, 2, 1, 2, 2, 2, 3};
    const int C[3 * 3] = {-1, 2, 2, -2, 1, 2, -2, 2, 3};

    int a = 3, b = 4, c = 5;
    std::vector <std::tuple<int, int, int>> queue;
    queue.reserve(166870); // It is known!
    queue.push_back(std::make_tuple(a, b, c));
    cache[5] = 1;

    for (int counter = 0; counter < queue.size(); counter++) {
        std::tie(a, b, c) = queue[counter];
        for (const auto &m : {A, B, C}) {
            int i = m[0 * 3 + 0] * a + m[0 * 3 + 1] * b + m[0 * 3 + 2] * c;
            int j = m[1 * 3 + 0] * a + m[1 * 3 + 1] * b + m[1 * 3 + 2] * c;
            int k = m[2 * 3 + 0] * a + m[2 * 3 + 1] * b + m[2 * 3 + 2] * c;
            if (i <= N && j <= N && k <= N) {
                queue.push_back(std::make_tuple(i, j, k));
                cache[std::max({i, j, k})]++;
            }
        }
    }

    for (int i = 1; i < N; i++) {
        cache[i] += cache[i - 1];
    }
}

void getint_unlocked(int &x) {
    x = 0;
    int c;
    while (c = getchar_unlocked(), c >= '0' && c <= '9')
        x = x * 10 + (c - '0');
}

int main() {
    auto start = std::chrono::steady_clock::now();

    precalc();

    int c;
    while (getint_unlocked(c), c != 0) {
        printf("%u\n", cache[c]);
    }

    auto end = std::chrono::steady_clock::now();
    fprintf(stderr, "%lld\n", std::chrono::duration_cast<std::chrono::microseconds>(end - start).count());
}
