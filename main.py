import os


def main() -> None:
    print("Workspace contents:")
    for file in os.listdir():
        print(file)


if __name__ == "__main__":
    main()