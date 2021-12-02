#include <iostream>
#include <fstream>
#include <vector>
#include <numeric>


int main()
{
    // Part 1
    std::ifstream infile("input.txt");
    std::vector<int> depths;
    int num_inc = 0;
    int d;
    while (infile >> d) {
        depths.push_back(d);
    }
    for (int i = 1; i < depths.size(); i++) {
        if (depths.at(i) > depths.at(i - 1)) {
            num_inc++;
        }
    }
    std::cout << num_inc << std::endl;

    // Part 2
    std::vector<int> slidingDepths;
    for (int i = 2; i < depths.size(); i++) {
        slidingDepths.push_back(std::accumulate(depths.begin() + i - 2, depths.begin() + i + 1, 0));
    }

    int num_sliding_inc = 0;
    for (int i = 1; i < slidingDepths.size(); i++) {
        if (slidingDepths.at(i) > slidingDepths.at(i - 1)) {
            num_sliding_inc++;
        }
    }
    std::cout << num_sliding_inc << std::endl;
    return 0;
}
