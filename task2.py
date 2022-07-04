str = 'Happy new year'
def first_last(letter, st):
    _first = st.find(letter)
    _last = st.rfind(letter)
    return (None, None) if _last == -1 else (_first, _last)
print(first_last('a', str))