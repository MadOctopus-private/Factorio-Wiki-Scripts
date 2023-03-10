File = open("DE-Template.txt","r")
Template = File.readlines()
File.close

File = open("Core.txt", "r")
Core = File.readlines()
File.close

File = open("Base.txt", "r")
Base = File.readlines()
File.close

Translation = []

for i in range(len(Template)):
    flag = 0
    if "=" in Template[i] and "{" not in Template[i]:
        CurrentLine = Template[i].split(" = ")

        for j in range(len(Core)):
            if "=" in Core[j]:
                smth = Core[j].split("=")
                if CurrentLine[0].lower().replace(" ","-") == smth[0]:
                    CurrentLine[1] = smth[1]
                    flag = 1
                    
        for k in range(len(Base)):
            if "=" in Base[k]:
                smth = Base[k].split("=")
                if CurrentLine[0].lower().replace(" ","-") == smth[0]:
                    CurrentLine[1] = smth[1]
                    flag = 1

    else: Translation.append(Template[i])
    if flag == 1:
        CurrentLine[0] = "| " + str(CurrentLine[0])
    Translation.append(" = ".join(CurrentLine))

File = open("Translated.txt", "w")
for i in Translation:
    File.write(i)
File.close