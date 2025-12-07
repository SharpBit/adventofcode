import Utils (readLines)
import Data.List (transpose, foldl1, foldl')

parseNumber :: String -> Int -> Int -> [String] -> Int
parseNumber curr i j input
    | j >= length input - 1 = read curr :: Int
    | i < 0 || i >= length (head input) = 0
    | otherwise =
        if input !! j !! i /= ' '
        then parseNumber (curr ++ [(input !! j !! i)]) i (j + 1)  input
        else parseNumber curr i (j + 1) input

part1 :: [[Int]] -> [Int -> Int -> Int] -> Int
part1 nums ops =
    let cols = transpose nums
    in sum (zipWith (\op col -> foldl1 op col) ops cols)

part2 :: Int -> Int -> [Int] -> [String] -> Int
part2 res i curr input
    | i < 0 = res
    | otherwise =
        let
            num = parseNumber "" i 0 input
            curr' = num : curr
            op = input !! (length input - 1) !! i
        in case op of
            '+' -> part2 (res + (foldl' (+) 0 curr')) (i - 2) [] input
            '*' -> part2 (res + (foldl' (*) 1 curr')) (i - 2) [] input
            _ -> part2 res (i - 1) curr' input

main :: IO ()
main = do
    input <- readLines "inputs/day06.txt"
    let nums = map (map (read :: String -> Int) . words) (init input)
    let ops :: [Int -> Int -> Int]
        ops = map (\op -> if op == "+" then (+) else (*)) (words (last input))
    print (part1 nums ops)
    print (part2 0 (length (head input) - 1) [] input)
