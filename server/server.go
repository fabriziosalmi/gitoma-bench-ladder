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
// from s.users.Get(id), which returns (user, found bool).
// If the user is not found, the greeting is "Hello, stranger!".
func (s *Server) Greet(id int) string {
	user, found := s.users.Get(id)

	if !found {
		return "Hello, stranger!"
	}

	name := user
	return fmt.Sprintf("Hello, %s!", name)
}