#Ruby program to print all the prime numbers upto n

def prime(n)
    if n == 0 || n == 1
        return false 
    end
    range = (2..Math.sqrt(n)).to_a
    for i in range 
        if n % i == 0
            return false
        end
    end
    return true
end

puts "Enter a number- "
n = gets.chomp.to_i

range = (1..n)
for i in range 
    if prime(i)
        puts"#{i}"
    end
end
