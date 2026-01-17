from customtkinter import *
import pyperclip

root = CTk()
root.geometry("400x300")
root.title("RGB To Float Converter")
root.iconbitmap("icon.ico")
root.resizable(False, False)

def varSet(var, set):
    return var.set(set)

def varGet(var):
    return root.getvar(name = var)

def rgb(t, r, g, b, a = "0"):
    try:
        if t != "0":
            if a == "0":
                varSet(t, f"{r}, {g}, {b}")
            else:
                varSet(t, f"{r}, {g}, {b}, {a}")
        else:
            if a == "0":
                return f"{r}, {g}, {b}"
            else:
                return f"{r}, {g}, {b}, {a}"
    except:
        pass


def onRedChange(*args):
    global inputValLast

    try:
        if args[0] == "redIn":
            inputInt = redIn.get()
            red = "1"
            green = "0"
            blue = "0"
            alpha = "0"
            inputName = redIn
            outputName = redOut
        elif args[0] == "greenIn":
            inputInt = greenIn.get()
            red = "0"
            green = "1"
            blue = "0"
            alpha = "0"
            inputName = greenIn
            outputName = greenOut
        elif args[0] == "blueIn":
            inputInt = blueIn.get()
            red = "0"
            green = "0"
            blue = "1"
            alpha = "0"
            inputName = blueIn
            outputName = blueOut
        elif args[0] == "alphaIn":
            inputInt = alphaIn.get()
            red = "0"
            green = "0"
            blue = "0"
            alpha = "1"
            inputName = alphaIn
            outputName = alphaOut
        doAlpha = True

        if int(inputInt) > 255:
            varSet(inputName, "255")
            inputInt = redIn.get() if red == "1" else greenIn.get() if green == "1" else blueIn.get() if blue == "1" else alphaIn.get()
        elif int(inputInt) < 0 and alpha == "1":
            varSet(inputName, "-1")
            inputInt = alphaIn.get()
        elif int(inputInt) < 0 and alpha == "0":
            varSet(inputName, "0")
            inputInt = redIn.get() if red == "1" else greenIn.get() if green == "1" else blueIn.get()
        if inputInt != "":
            floatVal = round(int(inputInt) / 255, 2)
            if inputInt != "-1":
                varSet(outputName,f"{floatVal}")
                if alphaIn.get() == "-1":
                    doAlpha = False
            else:
                varSet(outputName, "")
                doAlpha = False
        else:
            varSet(outputName, "0.0")
        
        if doAlpha:
            rgb(total, redOut.get(), greenOut.get(), blueOut.get(), alphaOut.get())
        else:
            rgb(total, redOut.get(), greenOut.get(), blueOut.get())
        
    except:
        pass
    
    try:
        inputInt = int(inputInt)
    except ValueError:
        if inputInt != "":
            if inputInt != "-":
                varSet(inputName, "0")
                varSet(outputName, "0.0")
                rgb(total, redOut.get(), greenOut.get(), blueOut.get(), alphaOut.get())
        else:
            varSet(outputName, "0.0")
    
    inputValLast = inputInt

def focusOut(event):
    if redIn.get() == "":
        varSet(redIn, "0")
    if greenIn.get() == "":
        varSet(greenIn, "0")
    if blueIn.get() == "":
        varSet(blueIn, "0")
    if alphaIn.get() == "":
        varSet(alphaIn, "0")
    onRedChange

def copy():
    pyperclip.copy(total.get())
    copyText.set("Copied")
    root.after(1000, copyText.set("Copy"))

def delete(var):
    if var == "red":
        redIn.set("0")
    elif var == "green":
        greenIn.set("0")
    elif var == "blue":
        blueIn.set("0")
    elif var == "alpha":
        alphaIn.set("0")

satoshi = ("Satoshi", 20, "normal")

labelX = 125
labelW = 75

inputX = labelX
inputW = 200

# var in and out ( HEHEHE BURGER LOL)
redIn = StringVar(root, name = "redIn", value = "0")
redOut = StringVar(root, name = "redOut", value = "0.0")
greenIn = StringVar(root, name = "greenIn", value = "0")
greenOut = StringVar(root, name = "greenOut", value = "0.0")
blueIn = StringVar(root, name = "blueIn", value = "0")
blueOut = StringVar(root, name = "blueOut", value = "0.0")
alphaIn = StringVar(root, name = "alphaIn", value = "0")
alphaOut = StringVar(root, name = "alphaOut", value = "0.0")

total = StringVar(root, name = "total", value = rgb("0", redOut.get(), greenOut.get(), blueOut.get(), alphaOut.get()))

copyText = StringVar(root, name = "copyText", value = "Copy")

# on var change
redIn.trace_add("write", onRedChange)
greenIn.trace_add("write", onRedChange)
blueIn.trace_add("write", onRedChange)
alphaIn.trace_add("write", onRedChange)

# red
redLabel = CTkLabel(root, text = "Red", font = satoshi, width = labelW)
redInput = CTkEntry(root, textvariable = redIn, font = satoshi, width = inputW)

redInput.bind("<FocusOut>", focusOut)
redIn.set("0")

redLabel.place(x = labelX, y = 50, anchor = "e")
redInput.place(x = inputX, y = 50, anchor = "w")

# green
greenLabel = CTkLabel(root, text = "Green", font = satoshi, width = labelW)
greenInput = CTkEntry(root, textvariable = greenIn, font = satoshi, width = inputW)

greenInput.bind("<FocusOut>", focusOut)
greenIn.set("0")

greenLabel.place(x = labelX, y = 100, anchor = "e")
greenInput.place(x = inputX, y = 100, anchor = "w")

# blue
blueLabel = CTkLabel(root, text = "Blue", font = satoshi, width = labelW)
blueInput = CTkEntry(root, textvariable = blueIn, font = satoshi, width = inputW)

blueInput.bind("<FocusOut>", focusOut)
blueIn.set("0")

blueLabel.place(x = labelX, y = 150, anchor = "e")
blueInput.place(x = inputX, y = 150, anchor = "w")

# alpha
alphaLabel = CTkLabel(root, text = "Alpha", font = satoshi, width = labelW)
alphaInput = CTkEntry(root, textvariable = alphaIn, font = satoshi, width = inputW)

alphaInput.bind("<FocusOut>", focusOut)
alphaIn.set("0")

alphaLabel.place(x = labelX, y = 200, anchor = "e")
alphaInput.place(x = inputX, y = 200, anchor = "w")

# total
totalButton = CTkButton(root, textvariable = copyText, font = satoshi, width = labelW, command = copy)
totalOutput = CTkLabel(root, textvariable = total, font = satoshi, width = inputW)

totalButton.place(x = labelX, y = 250, anchor = "e")
totalOutput.place(x = inputX, y = 250, anchor = "w")


root.mainloop()
