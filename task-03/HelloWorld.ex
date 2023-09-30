defmodule Prime do
  def nth_prime(n), do: prime(n, 2)
def is_prime(x), do: (2..x |> Enum.filter(fn a -> rem(x, a) == 0 end) |> length()) == 1
def prime(n, n), do: []
def prime(n, acc) do
  case is_prime(acc) do
    true -> [acc | prime(n, acc + 1)]
    false -> prime(n, acc + 1)
  end
end 
  
  def start do
    {n, _} = IO.gets("") |> Integer.parse

    i = nth_prime(n)
    IO.inspect i
  end
  
end

Prime.start()