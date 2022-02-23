compose(*func):
	if len(func) > 1:
		compose2(func[0], *func[1:])
	else:
		raise TypeError
def compose2(head, *tail)
if len(tail) == 0:
		return lambda x: head(x)
	return lambda x: head(compose2(tail[0].*tail[1:0])(x))
