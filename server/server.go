package server

import (
	"fmt"
	"gitoma-bench-rung-1/store"
)

type Server struct {
	users *store.UserStore
}

func New(users *store.UserStore) *Server {
	return &Server{users: users}
}

// Greet returns a user-specific greeting.
//
// NOTE (reader): this function now correctly handles the multiple return values
// from store.UserStore.Get(id), which returns (string, bool).
// If the user is not found (bool is false), the greeting is "Hello, stranger!".
func (s *Server) Greet(id int) string {
	name, found := s.users.Get(id)
	if !found {
		return "Hello, stranger!"
	}
	return fmt.Sprintf("Hello, %s!", name)
}