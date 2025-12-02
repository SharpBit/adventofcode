import Utils (readLines)
import Debug.Trace

-- I'll refactor this with foldl' later

parsePassword :: [String] -> Int -> Int -> Int
parsePassword rotations i pointer
    | i >= (length rotations) = 0
    | null rotation = parsePassword rotations (i + 1) pointer  -- shouldn't happen
    | otherwise =
        let
            dir = head rotation
            num = read (tail rotation) :: Int
            op = if dir == 'L' then (-) else (+) :: Int -> Int -> Int
            newPointer = (pointer `op` num) `mod` 100
            rest = parsePassword rotations (i + 1) newPointer
            add = if newPointer == 0 then 1 else 0
        in (add + rest)
    where rotation = rotations !! i

parsePassword2 :: [String] -> Int -> Int -> Int
parsePassword2 rotations i pointer
    | i >= (length rotations) = 0
    | null rotation = parsePassword2 rotations (i + 1) pointer  -- shouldn't happen
    | otherwise =
        let
            dir = head rotation
            num = read (tail rotation) :: Int
            op = if dir == 'L' then (-) else (+) :: Int -> Int -> Int
            newPointer = (pointer `op` num)
            rest = parsePassword2 rotations (i + 1) (newPointer `mod` 100)
            add | newPointer > 0 = newPointer `div` 100
                | pointer == 0 && newPointer <= 0 = (abs newPointer) `div` 100
                | otherwise = (abs newPointer) `div` 100 + 1
        in (add + rest)
    where rotation = rotations !! i

part1 :: [String] -> Int
part1 rotations = parsePassword rotations 0 50

part2 :: [String] -> Int
part2 rotations = parsePassword2 rotations 0 50

main :: IO ()
main = do
    rotations <- readLines "inputs/day01.txt"
    print (part1 rotations)
    print (part2 rotations)
