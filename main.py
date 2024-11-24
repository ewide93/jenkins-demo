import os


def save_workspace() -> None:
    with open("workspace.txt", mode="w") as ostream:
        ostream.write("Workspace contents:\n")
        for file in os.listdir():
            ostream.write(file + "\n")

def main() -> None:
    save_workspace()

if __name__ == "__main__":
    main()