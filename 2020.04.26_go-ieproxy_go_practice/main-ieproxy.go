package main

import (
  "fmt"
  "io"
  "net/http"
  "os"

  _ "github.com/mattn/go-ieproxy/global"
)

func main() {
  res, err := http.Get("https://api.ipify.org?format=json")
  if err != nil {
    fmt.Fprintln(os.Stderr, err)
    os.Exit(1)
  }
  defer res.Body.Close()
  io.Copy(os.Stdout, res.Body)
}
