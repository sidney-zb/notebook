package main

import (
	"fmt"
	"testing"
)

func TestTcpPortStatus(t *testing.T) {
	fmt.Println(TcpPortStatus("192.168.73.128",8001,5))
}
