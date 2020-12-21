//usr/local/bin/go run $0 $@ ; exit

package main

import (
	"fmt"
	"reflect"
)

func main() {

 // for i :=0.01; i <= 1; i = i + 0.01 {
 //   fmt.Printf("  %v\n", i)
 // }

  a := 0.01
  fmt.Println(reflect.TypeOf(a))
  for a < 1 {
    fmt.Printf("%v + 0.01 =  ", a)
    a = a + 0.01
    fmt.Printf("%v \n", a)

  }

  fmt.Println("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

  b := 0.01
  for b <= 1 {
    fmt.Printf("%v \n", b)
    b = b + 0.01
  }

  fmt.Println("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

  /**
  	1/0.01=100
  **/
  counter := 1
  c := 0.01
  for counter <=100 {
    fmt.Printf("%v + 0.01 = ", c)
    counter++
    c = c + 0.01
    fmt.Printf("%v \n", c)
  }

}

// ref.https://text.baldanders.info/golang/loop-counter/
