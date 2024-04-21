class Calculator:
    def add(x: int| float, y: int| float) -> float:
        if type(x) not in (int, float) or type(y) not in (int, float):
            raise TypeError
        return x + y

    def sub(x: int| float, y: int| float) -> float:
        if type(x) not in (int, float) or type(y) not in (int, float):
            raise TypeError
        return x - y

    def mult(x: int| float, y: int| float) -> float:
        if type(x) not in (int, float) or type(y) not in (int, float):
            raise TypeError
        return x * y

    def div(x: int| float, y: int| float) -> float:
        if type(x) not in (int, float) or type(y) not in (int, float):
            raise TypeError
        return x / y

