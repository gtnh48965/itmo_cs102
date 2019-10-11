package vigenere

import (
	"strings"
)

func EncryptVigenere(plaintext string, keyword string) string {
	var ciphertext string

	keyword = strings.ToLower(keyword)
	for i := 0; i < len(plaintext); i++ {
		letter := plaintext[i]
		shift := int(keyword[i%len(keyword)]) - 97
		if (int('a') <= int(letter)) && (int(letter) <= int('z')) {
			ciphertext += string(rune(int(letter)-97+shift)%26 + 97)
		} else if (int('A') <= int(letter)) && (int(letter) <= int('Z')) {
			ciphertext += string(rune(int(letter)-65+shift)%26 + 65)
		} else {
			ciphertext += string(letter)
		}
	}

	return ciphertext
}

func DecryptVigenere(ciphertext string, keyword string) string {
	var plaintext string

	keyword = strings.ToLower(keyword)
	for i := 0; i < len(ciphertext); i++ {
		letter := ciphertext[i]
		shift := int(keyword[i%len(keyword)]) - 97
		if (int('a') <= int(letter)) && (int(letter) <= int('z')) {
			newLetter := int(letter) - shift
			if newLetter < 97 {
				newLetter += 26
			}
			plaintext += string(rune(newLetter))
		} else if (int('A') <= int(letter)) && (int(letter) <= int('Z')) {
			newLetter := int(letter) - shift
			if newLetter < 65 {
				newLetter += 26
			}
			plaintext += string(rune(newLetter))
		} else {
			plaintext += string(letter)
		}
	}

	return plaintext
}
