package server

import (
	"testing"

	"gitoma-bench-rung-1/store"
)

func TestGreetKnownUser(t *testing.T) {
	us := store.NewUserStore()
	us.Put(42, "Alice")

	s := New(us)
	got := s.Greet(42)
	want := "Hello, Alice!"

	if got != want {
		t.Fatalf("Greet(42) = %q, want %q", got, want)
	}
}

func TestGreetUnknownUser(t *testing.T) {
	us := store.NewUserStore()

	s := New(us)
	got := s.Greet(99)
	want := "Hello, stranger!"

	if got != want {
		t.Fatalf("Greet(99) on empty store = %q, want %q", got, want)
	}
}
