#include <iostream>
#include <fstream>

int main()
{
    std::ifstream input("input.txt");
    std::string dir;
    int num;
    int pos = 0, depth1 = 0, depth2 = 0, aim = 0;
    while (input >> dir >> num) {
        if (dir == "up") {
            depth1 -= num;
            aim -= num;
        }
        else if (dir == "down") {
            depth1 += num;
            aim += num;
        }
        else {
            pos += num;
            depth2 += aim * num;
        }
    }


    std::cout << "Part 1: " << pos * depth1 << std::endl;
    std::cout << "Part 2: " << pos * depth2 << std::endl;
    return 0;
}
