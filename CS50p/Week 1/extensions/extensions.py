import string


def main():
    name = input("File name: ")

    name = name.lower().strip()
    # finding period
    periodLoc = name.rfind(".")

    suffix = name[periodLoc+1:]
    match suffix:
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "png" | "gif":
            print(f"image/{suffix}")
        case "pdf" | "zip":
            print(f"application/{suffix}")
        case "txt":
            print("text/plain")
        case _:
            print("application/octet-stream")


main()
