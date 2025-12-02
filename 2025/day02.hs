import Utils (splitStr, pair, strip, slice)

invalidID :: Int -> Bool
invalidID id =
    let
        idStr = show id
        mid = length idStr `div` 2
        first = slice 0 mid idStr
        second = slice mid (length idStr) idStr
    in first == second

step :: Int -> (Int, Int) -> Int
step res (start, end) =
    let invalidIDs = [id | id <- [start..end + 1], invalidID id]
    in res + sum invalidIDs

part1 :: [(Int, Int)] -> Int
part1 productRanges = foldl' step 0 productRanges

main :: IO ()
main = do
    input <- readFile "inputs/day02.txt"
    let productRanges' = fmap pair (fmap (splitStr '-') (fmap strip (splitStr ',' input)))
        productRanges = map (\(a, b) -> (read a :: Int, read b :: Int)) productRanges'
    print (part1 productRanges)
