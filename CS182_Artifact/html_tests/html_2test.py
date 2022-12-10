import atheris
import sys

with atheris.instrument_imports():
    from bs4 import BeautifulSoup as bs

@atheris.instrument_func
def TestOneInput(data):

    fdp = atheris.FuzzedDataProvider(data)
    data = fdp.ConsumeString(len(data))

    p = fdp.ConsumeString(len(data))

    soup = bs(data, features ="html.parser")
    return soup.find_all(p, data)
    
atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()

