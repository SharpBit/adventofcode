#include <iostream>
#include <fstream>
#include <stack>
#include <map>
#include <vector>
#include <algorithm>

int main()
{
    std::ifstream input("input.txt");
    std::string line;

    std::map<char, char> chunkPairs = { {'(', ')'}, {'[', ']'}, {'{', '}'}, {'<', '>'} };
    std::map<char, int> errorTable = { {')', 3}, {']', 57}, {'}', 1197}, {'>', 25137} };
    std::map<char, int> completionTable = { {'(', 1}, {'[', 2}, {'{', 3}, {'<', 4} };
    
    int errorScore = 0;
    std::vector<long long int> completionScores;
    while (input >> line) {
        std::stack<char> chunks;

        bool corrupted = false;
        for (int i = 0; i < line.length(); i++) {
            if (line[i] == '(' || line[i] == '[' || line[i] == '{' || line[i] == '<') {
                chunks.push(line[i]);
            }
            else {
                char openchunk = chunks.top();
                if (chunkPairs[openchunk] == line[i]) {
                    chunks.pop();
                }
                else {
                    errorScore += errorTable[line[i]];
                    corrupted = true;
                    break;
                }
            }
        }

        if (!corrupted) {
            long long int completionScore = 0;
            while (!chunks.empty()) {
                char top = chunks.top();
                completionScore *= 5;
                completionScore += completionTable[top];
                chunks.pop();
            }
            completionScores.push_back(completionScore);
        }
    }

    std::sort(completionScores.begin(), completionScores.end());

    std::cout << "Part 1: " << errorScore << std::endl;
    std::cout << "Part 2: " << completionScores.at(completionScores.size() / 2) << std::endl;
}
