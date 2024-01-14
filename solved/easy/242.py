def main(s: str, t: str) -> bool:
    if sorted(s) == sorted(t):
        return True
    return False


if __name__ == "__main__":
    r = main("anagram", "nagaram")
    print(r)
