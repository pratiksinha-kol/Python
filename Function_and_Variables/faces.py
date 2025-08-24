def fun(text: str):
    return text.replace(":)", "🙂").replace(":(", "🙁").replace(":D","😂")

def main():
    faces = input("Enter sign you want to convert into an emoji: i.e. ':)' or ':('...:::: ")
    print(f"{fun(faces)}")

main()