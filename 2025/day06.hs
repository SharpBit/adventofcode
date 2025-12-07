import Utils (readLines)
import Data.List (transpose, foldl1)

part1 :: [[Int]] -> [Int -> Int -> Int] -> Int
part1 nums ops =
    let cols = transpose nums
    in sum (zipWith (\op col -> foldl1 op col) ops cols)

main :: IO ()
main = do
    input <- readLines "inputs/day06.txt"
    let nums = map (map (read :: String -> Int) . words) (init input)
    let ops :: [Int -> Int -> Int]
        ops = map (\op -> if op == "+" then (+) else (*)) (words (last input))
    print (part1 nums ops)
    -- I do not feel like doing part 2 in haskell, maybe i'll do it in python
