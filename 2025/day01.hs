import Utils (readLines)
import Data.List (foldl')

step1 :: (Int, Int) -> String -> (Int, Int)
step1 (pointer, count) rotation =
    case rotation of
        (dir:amt) ->
            let
                num = read amt :: Int
                op = if dir == 'L' then (-) else (+) :: Int -> Int -> Int
                newPointer = (pointer `op` num) `mod` 100
                count' = if newPointer == 0 then count + 1 else count
            in (newPointer, count')
        _ -> (pointer, count)

step2 :: (Int, Int) -> String -> (Int, Int)
step2 (pointer, count) rotation =
    case rotation of
        (dir:amt) ->
            let
                num = read amt :: Int
                op = if dir == 'L' then (-) else (+) :: Int -> Int -> Int
                newPointer = (pointer `op` num)
                add | newPointer > 0 = newPointer `div` 100
                    | pointer == 0 && newPointer <= 0 = (abs newPointer) `div` 100
                    | otherwise = (abs newPointer) `div` 100 + 1
                count' = count + add
            in (newPointer `mod` 100, count')
        _ -> (pointer, count)

part1 :: [String] -> Int
part1 rotations = snd (foldl' step1 (50, 0) rotations)

part2 :: [String] -> Int
part2 rotations = snd (foldl' step2 (50, 0) rotations)

main :: IO ()
main = do
    rotations <- readLines "inputs/day01.txt"
    print (part1 rotations)
    print (part2 rotations)
