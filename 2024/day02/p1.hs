isAscending :: [Int] -> Bool
isAscending (x:y:xs) = x < y && isAscending (y:xs)
isAscending _ = True

isDescending :: [Int] -> Bool
isDescending (x:y:xs) = x > y && isDescending (y:xs)
isDescending _ = True

rule1 :: [Int] -> Bool
rule1 x = isAscending x || isDescending x

rule2 :: [Int] -> Bool
rule2 (x:y:xs)
    | abs (x - y) < 1 = False
    | abs (x - y) > 3 = False
    | otherwise = rule2 (y:xs)
rule2 _ = True

report :: [Int] -> Bool
report x = rule1 x && rule2 x 

parseReport :: String -> [Int]
parseReport = map read . words

solution :: String -> String
solution = show . length . filter id . map report . map parseReport . lines

main = interact solution
