import Utils (readLines, addPairs, validCoord)
import qualified Data.IntSet as IntSet

adj :: [(Int, Int)]
adj = [
    ( 0,  1),
    ( 1,  1),
    ( 1,  0),
    ( 1, -1),
    ( 0, -1),
    (-1, -1),
    (-1,  0),
    (-1,  1) ]

step :: (Int, Int, Int, Int, IntSet.IntSet) -> [[Int]] -> IntSet.IntSet
step (r, c, m, n, removed) grid
    | r < m && c >= n = step (r + 1, 0, m, n, removed) grid
    | r >= m = removed
    | grid !! r !! c == 0 = step (r, c + 1, m, n, removed) grid
    | otherwise =
        let
            coords = [addPairs (r, c) (adj !! i) | i <- [0..7]]
            validCoords = filter (validCoord m n) coords
            num_adj = sum (map (\(r, c) -> if grid !! r !! c == 1 then 1 else 0) validCoords)
            -- Convert (r, c) to a single Int and insert into the IntSet
            removed' = if num_adj < 4 then IntSet.insert (r * n + c) removed else removed
        in step (r, c + 1, m, n, removed') grid

part1 :: [[Int]] -> Int
part1 [] = 0
part1 grid =
    let removed = step (0, 0, length grid, length (head grid), IntSet.empty) grid
    in IntSet.size removed

part2 :: Int -> [[Int]] -> Int
part2 res [] = res
part2 res grid =
    let
        m = length grid
        n = length (head grid)
        removed = step (0, 0, m, n, IntSet.empty) grid
        newGrid :: [[Int]]
        newGrid = [[if grid !! r !! c == 0 || IntSet.member (r * n + c) removed then 0 else 1 | c <- [0..n - 1]] | r <- [0..n - 1]]
    in
        if IntSet.null removed
        then res + (IntSet.size removed)
        else part2 (res + (IntSet.size removed)) newGrid

main :: IO ()
main = do
    grid <- readLines "inputs/day04.txt"
    let intGrid = map (map (\c -> if c == '@' then 1 else 0)) grid
    print (part1 intGrid)
    print (part2 0 intGrid)
