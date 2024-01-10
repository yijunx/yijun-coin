class Stuff:
    def __init__(self, name1: str, name2: str) -> None:
        self.name1 = name1
        self.name2 = name2

    def __eq__(self, __value: "Stuff") -> bool:
        return (self.name1 + self.name2) == (__value.name1 + __value.name2)


if __name__ == "__main__":
    print(Stuff("b", "a") == Stuff("ba", ""))
