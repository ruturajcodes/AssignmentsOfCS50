def convert(face):
    print(face.replace(":)","🙂").replace(":(","🙁"))

def main():
    face = input("Enter your emoji: ")
    convert(face)

main()