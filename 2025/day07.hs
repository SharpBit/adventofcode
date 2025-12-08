import Utils (readLines)
import Data.List (elemIndex, foldl')
import Data.Maybe
import qualified Data.IntSet as IntSet
import qualified Data.IntMap.Strict as IntMap

step1 :: (IntSet.IntSet, Int) -> Int -> [String] -> Int
step1 (beams, res) i input
    | i >= length input = res
    | otherwise =
        let
            row = input !! i
            (beams', res') = foldl' (\(accSet, accRes) m ->
                    if row !! m == '^'
                    then
                        let acc1 = IntSet.delete m accSet
                            acc2 = if m - 1 >= 0 then IntSet.insert (m - 1) acc1 else acc1
                            acc3 = if m + 1 < length row then IntSet.insert (m + 1) acc2 else acc2
                        in (acc3, accRes + 1)
                    else (accSet, accRes)
                ) (beams, res) (IntSet.toList beams)
        in step1 (beams', res') (i + 1) input

step2 :: (IntMap.IntMap Int, Int) -> Int -> [String] -> Int
step2 (beams, res) i input
    | i >= length input = res
    | otherwise =
        let
            row = input !! i
            keys = IntMap.keys beams
            (beams', res') =
                foldl' (\(accMap, accRes) m ->
                    let n = IntMap.findWithDefault 0 m beams
                    in if n == 0
                       then (accMap, accRes)  -- no beams here, skip
                       else if row !! m == '^'
                            then
                                -- splitter: remove m, add n to neighbors, count splits
                                let acc1 = if m - 1 >= 0 then IntMap.insertWith (+) (m - 1) n accMap else accMap
                                    acc2 = if m + 1 < length row then IntMap.insertWith (+) (m + 1) n acc1 else acc1
                                -- There were n beams at position m.
                                -- Since those n beams split, there are now n beams in m-1 and n beams in m+1. This means there are 2n-n=n new timelines
                                in (acc2, accRes + n)
                            else
                                -- no splitter: carry n down at same column
                                (IntMap.insertWith (+) m n accMap, accRes)
                ) (IntMap.empty, res) keys
        in step2 (beams', res') (i + 1) input

part1 :: [String] -> Int -> Int
part1 input start = step1 (IntSet.fromList [start], 0) 0 input

part2 :: [String] -> Int -> Int
part2 input start = step2 (IntMap.singleton start 1, 0) 0 input + 1  -- + 1 for the initial timeline

main :: IO ()
main = do
    input <- readLines "inputs/day07.txt"
    let start = fromMaybe 0 $ elemIndex 'S' (head input)
    print (part1 (tail input) start)
    print (part2 (tail input) start)
