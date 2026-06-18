package main

import (
	"fmt"
	"slices"
)

func processStr(s string) string {
	// '*' removes the last character from result, if it exists.
	// '#' duplicates the current result and appends it to itself.
	// '%' reverses the current result.

	var characters []rune

	for _, ch := range s {
		if ch >= 'a' && ch <= 'z' {
			characters = append(characters, ch)
		}

		if ch == '*' {
			if len(characters) > 0 {
				characters = characters[:len(characters)-1]
			}
		}

		if ch == '#' {
			characters = append(characters, characters...)
		}

		if ch == '%' {
			slices.Reverse(characters)
		}
	}

	return string(characters)
}

func main() {
	fmt.Println("3612. Process String with Special Operations I")

	fmt.Printf("ztv#*l = %s\n", processStr("ztv#*l"))
	fmt.Printf("a#b%%* = %s\n", processStr("a#b%*"))
}
