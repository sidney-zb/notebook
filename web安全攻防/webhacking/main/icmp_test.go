package main

import (
	"log"
	"testing"
)

func TestPingHost(t *testing.T) {
	log.Println(PingHost("192.168.73.1"))
}
