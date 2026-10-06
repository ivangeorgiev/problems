import json
import os


class FileManager:
    def id_finder(self, name: str, dir: str, ex: str, id: int):
        file = dir + "/" + name + "." + ex
        if not os.path.exists(file) or not os.path.isfile(file):
            print("File does not exist under path: " + file)
            return

        numbers: list[int] = []
        if ex == "txt":
            # read the IDs from TXT file
            with open(file, "r") as f:
                txt = f.read()
            ids = txt.split(",")
            for file_id in ids:
                numbers.append(int(file_id))

        elif ex == "json":
            # read the IDs from JSON file
            with open(file, "r") as f:
                txt = f.read()
            numbers = json.loads(txt)
        else:
            print("Unsupported file extension: " + ex)
            return

        for number in numbers:
            if number == id:
                print(f"Id {id} has been found in the file {file}.")
                return

        print(f"Id {id} has not been found in the file {file}.")


if __name__ == "__main__":
    file_manager: FileManager = FileManager()
    file_manager.id_finder("testFile", ".", "txt", 5) # found
    file_manager.id_finder("testFile", ".", "txt", 15) # not found
    file_manager.id_finder("testFile", ".", "json", 3) # found
    file_manager.id_finder("testFile", ".", "json", 20) # not found
