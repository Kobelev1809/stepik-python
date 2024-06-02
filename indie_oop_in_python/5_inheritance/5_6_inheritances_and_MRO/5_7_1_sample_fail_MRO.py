# Первый вариант невозможности реализации алгоритма С3 линеаризации (МРО)
class X: ...


class Y: ...


class A(X, Y): ...


class B(Y, X): ...


class G(A, B): ...


# Второй вариант невозможности реализации алгоритма С3 линеаризации (МРО)
class X: ...


class Y(X): ...


class A(X, Y): ...
