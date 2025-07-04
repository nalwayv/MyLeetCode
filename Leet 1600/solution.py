class ThroneInheritance:
    def __init__(self, kingName: str):
        self.king: str = kingName
        self.family: dict[str, list[str]] = {kingName: []}
        self.alive: set[str] = {kingName}

    def birth(self, parentName: str, childName: str) -> None:
        if parentName not in self.family:
            self.family[parentName] = []

        self.family[parentName].append(childName)
        self.family[childName] = []

        self.alive.add(childName)

    def death(self, name: str) -> None:
        self.alive.discard(name)

    def _dfs(self, name: str, names: list[str]):
        if name in self.alive:
            names.append(name)

        for child in self.family.get(name, []):
            self._dfs(child, names)

    def getInheritanceOrder(self) -> list[str]:
        names: list[str] = []
        self._dfs(self.king, names)
        return names


def main() -> None:
    print("1600. Throne Inheritance")

    throne = ThroneInheritance("king")
    
    throne.birth("king", "andy")
    throne.birth("king", "bob")
    throne.birth("king", "catherine")
    throne.birth("andy", "matthew")
    throne.birth("bob", "alex")
    throne.birth("bob", "asha")

    print(throne.getInheritanceOrder())
    
    throne.death("bob")
    
    print(throne.getInheritanceOrder())


if __name__ == "__main__":
    main()

