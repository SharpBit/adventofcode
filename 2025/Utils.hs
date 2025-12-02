module Utils (
    readLines,
    readWords,
    slice
) where

import System.IO
import Control.Monad

readLines :: String -> IO [String]
readLines fname = fmap lines (readFile fname)

readWords :: String -> IO [String]
readWords fname = fmap words (readFile fname)

slice :: Int -> Int -> String -> String
slice start end str = take (end - start) (drop start str)
