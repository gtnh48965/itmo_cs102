package rsa

import (
	"errors"
	"math"
	"math/big"
	"math/rand"
)

type Key struct {
	key int
	n   int
}

type KeyPair struct {
	Private Key
	Public  Key
}

func isPrime(n int) bool {
	//return big.NewInt(int64(n)).ProbablyPrime(0)
	for i := 2; i < int(math.Sqrt(float64(n)))+1; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func gcd(a int, b int) int {
	//return int(new(big.Int).GCD(nil, nil, big.NewInt(int64(a)), big.NewInt(int64(b))).Int64())
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func extendedEuclidGcd(a int, b int) (int, int, int) {
	s := 0
	oldS := 1
	t := 1
	oldT := 0
	r := b
	oldR := a
	for r != 0 {
		quotient := oldR / r
		oldR, r = r, oldR-quotient*r
		oldS, s = s, oldS-quotient*s
		oldT, t = t, oldT-quotient*t
	}
	return oldR, oldS, oldT
}

func multiplicativeInverse(e int, phi int) int {
	//return int(new(big.Int).ModInverse(big.NewInt(int64(e)), big.NewInt(int64(phi))).Int64())
	_, x, _ := extendedEuclidGcd(e, phi)
	if x < 0 {
		x += phi
	}
	return x
}

func GenerateKeypair(p int, q int) (KeyPair, error) {
	if !isPrime(p) || !isPrime(q) {
		return KeyPair{}, errors.New("Both numbers must be prime.")
	} else if p == q {
		return KeyPair{}, errors.New("p and q can't be equal.")
	}

	// n = pq
	n := p * q

	// phi = (p-1)(q-1)
	phi := (p - 1) * (q - 1)

	e := rand.Intn(phi-1) + 1
	g := gcd(e, phi)
	for g != 1 {
		e = rand.Intn(phi-1) + 1
		g = gcd(e, phi)
	}

	d := multiplicativeInverse(e, phi)
	return KeyPair{Key{e, n}, Key{d, n}}, nil
}

func Encrypt(pk Key, plaintext string) []int {
	cipher := []int{}
	n := new(big.Int)
	for _, ch := range plaintext {
		n = new(big.Int).Exp(
			big.NewInt(int64(ch)), big.NewInt(int64(pk.key)), nil)
		n = new(big.Int).Mod(n, big.NewInt(int64(pk.n)))
		cipher = append(cipher, int(n.Int64()))
	}
	return cipher
}

func Decrypt(pk Key, cipher []int) string {
	plaintext := ""
	n := new(big.Int)
	for _, ch := range cipher {
		n = new(big.Int).Exp(
			big.NewInt(int64(ch)), big.NewInt(int64(pk.key)), nil)
		n = new(big.Int).Mod(n, big.NewInt(int64(pk.n)))
		plaintext += string(rune(int(n.Int64())))
	}
	return plaintext
}
