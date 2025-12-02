module Utils (
    readLines,
    readWords,
    slice,
    splitStr,
    strip,
    pair
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
