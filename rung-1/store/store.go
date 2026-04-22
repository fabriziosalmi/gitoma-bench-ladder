// Package store is an in-memory user lookup.
//
// This file is rung-1's "stable" dependency — its signature was
// recently tightened from ``Get(id int) string`` to
// ``Get(id int) (string, bool)`` so callers can distinguish a
// missing user (bool=false) from an intentionally-empty name.
package store

type UserStore struct {
	data map[int]string
}

func NewUserStore() *UserStore {
	return &UserStore{data: make(map[int]string)}
}

// Get returns (name, found). A false second return means there is
// no user registered under this ID — callers should not treat the
// empty string as "user exists but has no name".
func (s *UserStore) Get(id int) (string, bool) {
	name, ok := s.data[id]
	return name, ok
}

// Put registers ``name`` under ``id``, overwriting any prior value.
func (s *UserStore) Put(id int, name string) {
	s.data[id] = name
}
