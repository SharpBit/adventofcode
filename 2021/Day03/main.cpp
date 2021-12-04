#include <iostream>
#include <fstream>
#include <vector>
#include <string>

std::string findMostCommon(std::vector<std::string> &nums) {
    std::vector<int> digitCount;
    int inc;
    for (std::string num : nums) {
        for (int i = 0; i < num.length(); i++) {
            inc = num[i] == '1' ? 1 : -1;
            if (digitCount.size() <= i) {
                digitCount.push_back(inc);
            }
            else {
                digitCount.at(i) += inc;
            }
        }
    }
    std::string mostCommon;
    for (int i = 0; i < digitCount.size(); i++) {
        // Since function is for gamma rate/O2 generator rating, we do >= 0 for the 1 bit
        // This way, when the bits are flipped for the C02 scrubber rating, it gets flipped properly
        mostCommon += digitCount.at(i) >= 0 ? "1" : "0";
    }
    return mostCommon;
}

std::string flipBits(std::string &originalBits) {
    std::string flippedBits;
    for (int i = 0; i < originalBits.length(); i++) {
        flippedBits += originalBits[i] == '1' ? "0" : "1";
    }
    return flippedBits;
}

int main()
{
    std::ifstream input("input.txt");
    std::string binNum;
    std::vector<std::string> nums;
    while (input >> binNum) {
        nums.push_back(binNum);
    }

    std::string gamma = findMostCommon(nums);
    std::string epsilon = flipBits(gamma);
    int gammaRate = std::stoi(gamma, nullptr, 2);
    int epsilonRate = std::stoi(epsilon, nullptr, 2);
    
    std::cout << "Part 1: " << gammaRate * epsilonRate << std::endl;

    std::vector<std::string> oxygenNums(nums);
    std::vector<std::string> CO2Nums(nums);
    int bitIndex = 0;
    while (oxygenNums.size() > 1) {
        std::string mostCommon = findMostCommon(oxygenNums);
        char digitToKeep = mostCommon[bitIndex];
        for (int i = 0; i < oxygenNums.size(); i++) {
            if (oxygenNums.at(i)[bitIndex] != digitToKeep) {
                oxygenNums.erase(oxygenNums.begin() + i);
                i--;  // since we just removed an item, the index stays the same
            }
        }
        bitIndex++;
    }

    int oxygenRating = std::stoi(oxygenNums.at(0), nullptr, 2);

    bitIndex = 0;
    while (CO2Nums.size() > 1) {
        std::string mostCommon = findMostCommon(CO2Nums);
        std::string leastCommon = flipBits(mostCommon);
        char digitToKeep = leastCommon[bitIndex];
        for (int i = 0; i < CO2Nums.size(); i++) {
            if (CO2Nums.at(i)[bitIndex] != digitToKeep) {
                CO2Nums.erase(CO2Nums.begin() + i);
                i--;  // since we just removed an item, the index stays the same
            }
        }
        bitIndex++;
    }

    int CO2Rating = std::stoi(CO2Nums.at(0), nullptr, 2);
    std::cout << "Part 2: " << oxygenRating * CO2Rating << std::endl;
}
