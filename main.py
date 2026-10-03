def greet(name: str) -> str:
    return f"Привет, {name}!"


def farewell(name: str) -> str:
    return f"Пока, {name}!"


if __name__ == "__main__":
    print(greet("Git"))
    print(farewell("Git"))