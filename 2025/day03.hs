import Utils (readLines)
import Data.List (foldl')

-- Given a string, return the max character and its index excluding the last n characters
maxIndexExcluding :: (Char, Int) -> Int -> Int -> String -> (Char, Int)
maxIndexExcluding (currMax, maxIndex) i n str
    | i >= length str - n = (currMax, maxIndex)
    | currMax == '9' = (currMax, maxIndex)
    | otherwise =
        let
            currMax' = max currMax (str !! i)
            maxIndex' = if currMax' > currMax then i else maxIndex
        in maxIndexExcluding (currMax', maxIndex') (i + 1) n str

-- Get the max joltage with n digits
maxJoltage :: Integer -> Int -> String -> Integer
maxJoltage res n batteryBank
    | n <= -1 = res
    | otherwise =
        let
            (maxDigit, i) = maxIndexExcluding ('0', 0) 0 n batteryBank
            digit = read [maxDigit] :: Integer
            res' = res * 10 + digit
        in maxJoltage res' (n - 1) (drop (i + 1) batteryBank)

step1 :: Integer -> String -> Integer
step1 totalJoltage batteryBank =
    let joltage = maxJoltage 0 1 batteryBank
    in totalJoltage + joltage

step2 :: Integer -> String -> Integer
step2 totalJoltage batteryBank =
    let joltage = maxJoltage 0 11 batteryBank
    in totalJoltage + joltage

part1 :: [String] -> Integer
part1 batteryBanks = foldl' step1 0 batteryBanks

part2 :: [String] -> Integer
part2 batteryBanks = foldl' step2 0 batteryBanks

main :: IO ()
main = do
    batteryBanks <- readLines "inputs/day03.txt"
    print (part1 batteryBanks)
    print (part2 batteryBanks)
