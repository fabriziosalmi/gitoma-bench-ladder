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
// NOTE (reader): this function still uses the OLD 1-return-value call
// style for store.UserStore.Get. That API now returns (string, bool);
// the compiler flags this file as a result. Fixing requires:
//  1. Reading store/store.go to learn the new signature + the meaning
//     of the bool.
//  2. Updating this function to handle both return values. When the
//     user is not found, the greeting is "Hello, stranger!".
func (s *Server) Greet(id int) string {
	name, ok := s.users.Get(id)
	if !ok {
		return "Hello, stranger!"
	}
	return fmt.Sprintf("Hello, %s!", name)
}