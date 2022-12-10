import atheris
import sys

with atheris.instrument_imports():
    from bs4 import BeautifulSoup as bs

@atheris.instrument_func
def TestOneInput(data):

    fdp = atheris.FuzzedDataProvider(data)
    data = fdp.ConsumeString(len(data))

    soup = bs(data, features ="html5lib")
    return soup.find_all(data)
    
atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()
