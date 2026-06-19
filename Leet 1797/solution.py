class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self._tokens: dict[str, int] = {}
        self._time_to_live: int = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self._tokens:
            return
        
        self._tokens[tokenId] = currentTime + self._time_to_live

    def renew(self, tokenId: str, currentTime: int) -> None:
        """Renew unexpired token with extra time if found
        """
        # not been added
        if tokenId not in self._tokens:
            return
        
        # is expired
        if currentTime >= self._tokens[tokenId]:
            return
        
        # update with new expiry time from current time
        self._tokens[tokenId] = currentTime + self._time_to_live
        
    def countUnexpiredTokens(self, currentTime: int) -> int:
        count: int = 0 
        for v in self._tokens.values():
            if v > currentTime:
                count += 1
        return count


def main() -> None:
    print("1797. Design Authentication Manager")
    
    manager = AuthenticationManager(5)
    manager.renew("a", 1) # does nothing
    manager.generate("a", 2) # expires at 7
    print(manager.countUnexpiredTokens(6))# 1 
    manager.generate("b", 7) # expired at 12
    manager.renew("a", 8) # expired so do nothing
    manager.renew("b", 10) # update to 15
    print(manager.countUnexpiredTokens(15)) # 0


if __name__ == "__main__":
    main()