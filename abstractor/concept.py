class tesseract():

    def imageMake(self,arg,imageLocal):
        self.image = cv2.imread(imageLocal)
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        if arg == "threshold":
            self.gray = cv2.threshold(self.gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        elif arg == "blur":
            self.gray = cv2.medianBlur(self.gray, 3)

        else:
            print("incorrect parse")
            cv2.waitKey(0)

        self.filename = "{}.png".format(os.getpid())
        cv2.imwrite(self.filename, self.gray)



    def imgToString(self):
        self.final=""
        self.text = pytesseract.image_to_string(Image.open(self.filename))
        os.remove(self.filename)
        print(self.text)

        cv2.imshow("Image", self.image)
        cv2.imshow("Output", self.gray)
        self.read = True

    def createFile(self):
        with open("abstracted.txt", "x") as f:
            f.write(self.final)



    def abstract(self):
        if self.read == True:
            for word in self.text.split():
                print(word)
                if self.switch(word) == False:
                    self.final += " "+word
        else:
            print("file wasnt read")
    


    def switch(self, arguement):

        print(arguement)

        switches = ["and","as","a","for","if","but","of",
                    "the","that","which","is","was", "i",
                    "in", "with", "an", "or", "to"]
        if arguement in switches:
            return True
        else:
            return False

    

if __name__ == "__main__":

    try:
        from PIL import Image
        import pytesseract
        import imutils
        import os
        import cv2
    except:
        print("imports failed")

    tess = tesseract()
    tess.imageMake("threshold", "dummy.png")
    tess.imgToString()
    tess.abstract()
    tess.createFile()

