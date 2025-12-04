import Utils (splitStr, pair, strip, slice)
import Data.List (nub, foldl')

splitStrEqually :: Int -> String -> [String]
splitStrEqually n str
    | n <= 0 = []
    | otherwise =
        let sep = length str `div` n
        in slice 0 sep str : splitStrEqually (n - 1) (slice sep (length str) str)

-- Check if an ID is invalid, when split into n..max pieces
invalidID :: Int -> Int -> String -> Bool
invalidID n max id
    | n > max = False
    | otherwise = (length id `mod` n == 0 && length (nub (splitStrEqually n id)) == 1) || invalidID (n + 1) max id

step1 :: Int -> (Int, Int) -> Int
step1 res (start, end) =
    let invalidIDs = [id | id <- [start..end], invalidID 2 2 (show id)]
    in res + sum invalidIDs

step2 :: Int -> (Int, Int) -> Int
step2 res (start, end) =
    let invalidIDs = [id | id <- [start..end], invalidID 2 (length (show id)) (show id)]
    in res + sum invalidIDs

part1 :: [(Int, Int)] -> Int
part1 productRanges = foldl' step1 0 productRanges

part2 :: [(Int, Int)] -> Int
part2 productRanges = foldl' step2 0 productRanges

main :: IO ()
main = do
    input <- readFile "inputs/day02.txt"
    let productRanges' = fmap pair (fmap (splitStr '-') (fmap strip (splitStr ',' input)))
        productRanges = map (\(a, b) -> (read a :: Int, read b :: Int)) productRanges'
    print (part1 productRanges)
    print (part2 productRanges)
