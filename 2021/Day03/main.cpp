#include <iostream>
#include <fstream>
#include <vector>
#include <string>

int main()
{
    std::ifstream input("input.txt");
    std::string binNum;
    std::vector<int> digitCount;
    int inc;
    while (input >> binNum) {
        for (int i = 0; i < binNum.length(); i++) {
            inc = binNum[i] == '1' ? 1 : -1;
            if (digitCount.size() <= i) {
                digitCount.push_back(inc);
            } else {
                digitCount.at(i) += inc;
            }
        }
    }
    const int bits = 5;
    std::string gamma, epsilon;
    for (int i = 0; i < digitCount.size(); i++) {
        gamma += digitCount.at(i) > 0 ? "1" : "0";
        epsilon += digitCount.at(i) > 0 ? "0" : "1";
    }
    int gammaRate = std::stoi(gamma, nullptr, 2);
    int epsilonRate = std::stoi(epsilon, nullptr, 2);
    
    std::cout << "Part 1: " << gammaRate * epsilonRate << std::endl;
}
