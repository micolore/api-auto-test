package main

import (
	"fmt"
)

// 插件的使用场景和范围还有待研究

func get_page_size() int {
	fmt.Println("get_page_size......")
	return 2
}

func GetUserAgent() string {
	return "hrp/fungo"
}
