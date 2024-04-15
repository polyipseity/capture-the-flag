from pathlib import Path

if __name__ == "__main__":
    Path("wordlist.txt").write_text("".join(f"{hex(num)}\n" for num in range(2**20)))
