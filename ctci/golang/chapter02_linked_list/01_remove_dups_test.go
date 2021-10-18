package chapter02_linked_list

import (
	"container/list"
	"testing"
)

func TestIsUnique(t *testing.T) {
	l := list.New()
	l.PushBack(4)
	l.PushBack(3)
	l.PushBack(2)
	l.PushBack(2)
	l.PushBack(4)
	t.Run("delete_dups", func(t *testing.T) {
		deleteDups(l)
		if l.Len() != 3 {
			t.Logf("List length is %d", l.Len())
			t.Errorf("Expected list length %d", 3)
		}
	})
}

func deleteDups(l *list.List) {
	set := make(map[interface{}]struct{})

	n := l.Front()

	for n != nil {
		if _, ok := set[n.Value]; ok {
			l.Remove(n)
			deleteDups(l)
		} else {
			set[n.Value] = struct{}{}
		}
		n = n.Next()
	}
}
