package collections

type Element struct {
	next, prev *Element
	// the list this element belongs
	list  *List
	Value interface{}
}

func (e *Element) Next() *Element {
	if p := e.next; e.list != nil && p != e.list.root {
		return p
	}
	return nil
}

func (e *Element) Prev() *Element {
	if p := e.prev; e.list != nil && p != e.list.root {
		return p
	}

	return nil
}

type List struct {
	root *Element
	len  int
}
