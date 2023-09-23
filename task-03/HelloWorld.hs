isPrime :: Integer -> Bool
isPrime n
  | n < 2     = False
  | n == 2    = True
  | even n    = False
  | otherwise = not $ any (\x -> n `mod` x == 0) [3,5..isqrt n]
  where
    isqrt = floor . sqrt . fromIntegral

primesUpToN :: Integer -> [Integer]
primesUpToN n = filter isPrime [2..n]

main :: IO ()
main = do
  putStrLn "Enter a positive integer (n): "
  userInput <- getLine
  let n = read userInput :: Integer
  if n >= 2
    then putStrLn $ "Prime numbers up to " ++ show n ++ ": " ++ show (primesUpToN n)
    else putStrLn "Please enter a positive integer greater than or equal to 2."
