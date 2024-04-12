```go
func TcpPortStatus(ip string, port int, timeout int) bool {
	addr := fmt.Sprintf("%s:%d", ip, port)
	conn, err := net.DialTimeout("tcp", addr, time.Duration(timeout)*time.Second)
	if err != nil {
		return false
	}
	defer conn.Close()
	return true
}
```