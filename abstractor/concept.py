class file(object):

    def __init__(self, FILE):
        self.file = FILE
        self.final = ""



    def readFile(self):
        try:
            self.fileText = docx.Document(self.file)
            self.read = True
        except:
            print(f"couldnt read {self.file}")
    


    def createFile(self):
        with open("abstracted.txt", "x") as f:
            f.write(self.final)



    def abstract(self):
        if self.read == True:
            for word in self.fileText.split():
                print(word)
                if self.switch(word) == False:
                    self.final += " "+word
        else:
            print("file wasnt read")
    


    def switch(self, arguement):

        print(arguement)

        switches = ["and","as","a","for","if","but","of",
                    "the","that","which","is","was", "i",
                    "in", "with", "an", "or"]
        if arguement in switches:
            return True
        else:
            return False




if __name__ == "__main__":

    try: 
        import docx
    except:
        print("python docx not installed")

    #created new file class and initialised
    try1 = file("dummy.docx")
    #read the file it was given
    try1.readFile()
    #abstracting file
    try1.abstract()
    #writing abstracted file
    try1.createFile()