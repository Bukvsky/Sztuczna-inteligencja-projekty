from FileReader import fileReader
import os



def generateListOfLanguages():
    countries = {}
    for filename in os.listdir('.\\dane\\language_texts_grouped\\'):
        fr = fileReader('.\\dane\\language_texts_grouped\\'+filename+'\\')
        fr.generatePercentDict()
        countries[filename] = fr.charsPercentDict

    return countries


def main():
    generateListOfLanguages()

if __name__ == '__main__':
    main()
