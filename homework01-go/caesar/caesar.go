package caesar

func EncryptCaesar(plaintext string, shift int) string {
	var ciphertext string

	for i := 0; i < len(plaintext); i++ {
		letter := plaintext[i]
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

func DecryptCaesar(ciphertext string, shift int) string {
	var plaintext string

	for i := 0; i < len(ciphertext); i++ {
		letter := ciphertext[i]
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
