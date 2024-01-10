def main():
    x  = input()
    print(convert(x))

def convert(to):
    to = to.replace(":)", "🙂")
    to = to.replace(":(", "🙁")
    return to

main()
