import pyperclip

red = 0
green = 0
blue = 0
alpha = 0
decimal = 3
rgba = True
end = "n"
copy = "y"
output = ""

def divideInt(num, outOf):
    return num / outOf

def copyToClipboard(text):
    pyperclip.copy(text)

while end == "n":
    red = int(input("\nRed: "))
    red = round(divideInt(red, 255), decimal)

    green = int(input("Green: "))
    green = round(divideInt(green, 255), decimal)

    blue = int(input("Blue: "))
    blue = round(divideInt(blue, 255), decimal)

    alpha = int(input("Alpha (256 to ignore): "))
    if alpha >= 256:
        rgba = False
    else:
        alpha = round(divideInt(alpha, 255), decimal)
        rgba = True

    if rgba == True:
        output = f"{red}, {green}, {blue}, {alpha}"
    else:
        output = f"{red}, {green}, {blue}"
    print(f"\nResult: {output}")

    print("Copy to clipboard (y/n)")
    copy = input("")
    if copy.lower() == "y":
        copyToClipboard(output)

    print("End? (y/n)")
    end = input("")
    
