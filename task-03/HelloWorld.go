//GO program to print all the prime numbers upto n

package main
import ("fmt")

func main() {
	var n int

	fmt.Println("Enter a number: ")
	fmt.Scan(&n)

	for i := 2; i <= n; i++ {
		if isPrime(i) {
			fmt.Println(i)
		}
	}
}

func isPrime(num int) bool {
	if num < 2 {
		return false
	}

	for i := 2; i*i <= num; i++ {
		if num%i == 0 {
			return false
		}
	}

	return true
}