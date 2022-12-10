import atheris
import sys
import re

with atheris.instrument_imports():
    from bs4 import BeautifulSoup as bs

@atheris.instrument_func
def TestOneInput(data):

    fdp = atheris.FuzzedDataProvider(data)
    data = fdp.ConsumeString(len(data))

    data2 = fdp.ConsumeString(len(data))

    soup = bs(data, features ="html.parser")
    return soup.find_all(string=[data, data2])
    
atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()