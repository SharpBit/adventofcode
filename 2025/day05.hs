import Utils (readLines, splitStr, pair)
import Data.List (elemIndex, sort, sortBy)
import Data.Function (on)
import Data.Maybe

mergeIntervals :: Int -> [(Int, Int)] -> [(Int, Int)] -> [(Int, Int)]
mergeIntervals i mergedIntervals origIntervals
    | i >= length origIntervals || length mergedIntervals == 0 = mergedIntervals
    | otherwise =
        let
            (start, end) = origIntervals !! i
            (lastStart, lastEnd) = head mergedIntervals
            mergedIntervals' = 
                if start <= lastEnd
                then (lastStart, max end lastEnd) : tail mergedIntervals
                else (start, end) : mergedIntervals
        in mergeIntervals (i + 1) mergedIntervals' origIntervals

-- Assumptions:
-- intervals contains intervals with no overlaps, and is sorted in reverse order
-- ids is sorted ascending order
checkIDs :: Int -> Int -> Int -> [(Int, Int)] -> [Int] -> Int
checkIDs res i j intervals ids
    -- index out of bounds
    | i < 0 || i >= length intervals || j < 0 || j >= length ids = res
    -- found id in this interval, move to the next id
    | start <= id && id <= end = checkIDs (res + 1) i (j + 1) intervals ids
    -- didn't find current id yet, check the next one
    | id > end = checkIDs res (i - 1) j intervals ids
    -- we passed all intervals that could have this id, skip to the next id
    -- id < start
    | otherwise = checkIDs res i (j + 1) intervals ids
    where
        (start, end) = intervals !! i
        id = ids !! j

part1 :: [(Int, Int)] -> [Int] -> Int
part1 intervals available = checkIDs 0 ((length intervals) - 1) 0 intervals available

part2 :: [(Int, Int)] -> Int
part2 intervals = sum (map (\(start, end) -> end - start + 1) intervals)

main :: IO ()
main = do
    input <- readLines "inputs/day05.txt"
    let split = fromMaybe (-1) $ elemIndex "" input
    let intervals' = fmap pair (fmap (splitStr '-') (take split input))
        intervalsInt = map (\(a, b) -> (read a :: Int, read b :: Int)) intervals'
        intervals = sortBy (compare `on` fst) intervalsInt
        mergedIntervals = mergeIntervals 0 [(head intervals)] (tail intervals)
    let available = sort (map (\id -> read id :: Int) (drop (split + 1) input))

    print (part1 mergedIntervals available)
    print (part2 mergedIntervals)
