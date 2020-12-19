//usr/local/bin/go run $0 $@ ; exit

package main

import "fmt"

func main() {

 // for i :=0.01; i <= 1; i = i + 0.01 {
 //   fmt.Printf("  %v\n", i)
 // }

  k := 0.01
  for k < 1 {
    fmt.Printf("%v, + , 0.01 , = : ", k)
    k = k + 0.01
    fmt.Printf("%v \n", k)

  }

  fmt.Println("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

  v := 0.01
  for v <= 1 {
    fmt.Printf("%v \n", v)
    v = v + 0.01
  }

}
