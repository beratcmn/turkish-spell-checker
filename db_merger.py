import os


def merge_files():
    # get all .list files from the directory ./Turkce-Kelime-Listesi
    path = "./Turkce-Kelime-Listesi"
    files = [f for f in os.listdir(path) if f.endswith(".list")]
    print(files)

    # merge them into a single file
    with open("merged_list.txt", "w", encoding="UTF-8") as outfile:
        for fname in files:
            with open(os.path.join(path, fname), encoding="UTF-8") as infile:
                for line in infile:
                    outfile.write(line)

    # remove duplicates
    with open("merged_list.txt", "r", encoding="UTF-8") as f:
        lines = f.readlines()
    with open("merged_list.txt", "w", encoding="UTF-8") as f:
        f.writelines(sorted(set(lines)))

    # sort the words alphabetically
    with open("merged_list.txt", "r", encoding="UTF-8") as f:
        lines = f.readlines()
    with open("merged_list.txt", "w", encoding="UTF-8") as f:
        f.writelines(sorted(lines))


if __name__ == "__main__":
    merge_files()
    print("Done!")
