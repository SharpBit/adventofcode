module Utils (
    readLines,
    readWords,
    slice,
    splitStr,
    strip,
    pair,
    triple,
    addPairs,
    validCoord
) where

import System.IO
import Control.Monad
import Data.List (dropWhile, dropWhileEnd)

whitespace :: [Char]
whitespace = [' ', '\t', '\n']

readLines :: String -> IO [String]
readLines fname = fmap lines (readFile fname)

readWords :: String -> IO [String]
readWords fname = fmap words (readFile fname)

slice :: Int -> Int -> String -> String
slice start end str = take (end - start) (drop start str)

splitStr :: Char -> String -> [String]
splitStr delim str = case break (== delim) str of
    (a, "") -> [a]
    (a, _ : b) -> a : splitStr delim b

-- Strip whitespace from the beginning and end of str
strip :: String -> String
strip str = dropWhileEnd (`elem` whitespace) (dropWhile (`elem` whitespace) str)

pair :: [a] -> (a, a)
pair [x, y] = (x, y)

triple :: [a] -> (a, a, a)
triple [x, y, z] = (x, y, z)

-- Add the numbers of two pairs together
addPairs :: Num a => (a, a) -> (a, a) -> (a, a)
addPairs (a, b) (c, d) = (a + c, b + d)

-- Checks if coordinate (r, c) is valid in an m x n grid with m rows and n cols
validCoord :: Int -> Int -> (Int, Int) ->  Bool
validCoord m n (r, c) = if r >= 0 && r < m && c >= 0 && c < n then True else False
