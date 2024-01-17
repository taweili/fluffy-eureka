// write a hello world program in Go language
package main

import (
	"fmt"
	"time"
)

// write a corotuine to print out hello coroutine

func main() {
	go func() {
		for i := 0; i < 10; i++ {
			time.Sleep(time.Second)
		}
	}()
	time.Sleep(time.Second * 10)

}
