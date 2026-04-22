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
// NOTE (reader): this function now correctly handles the two return values
// from store.UserStore.Get, which returns (user, error).
// If the user is not found (error is present), the greeting is "Hello, stranger!".
func (s *Server) Greet(id int) string {
	user, err := s.users.Get(id)

	if err != nil {
		// User not found or error occurred
		return "Hello, stranger!"
	}

	name := user
	return fmt.Sprintf("Hello, %s!", name)
}