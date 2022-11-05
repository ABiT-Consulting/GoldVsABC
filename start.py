# write code to get value from forex.py
def onegramgoldValueInPKR():
    # current date
    import datetime
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    forxurl = "https://www.forex.pk/bullion-rates-gold-xau-pkr.php#:~:text=Today%20Gold%20Price%20for%2010,in%20every%20city%20of%20Pakistan."
    # get data from forex.pk
    import requests
    from bs4 import BeautifulSoup
    page = requests.get(forxurl)
    soup = BeautifulSoup(page.content, 'html.parser') 
    # print(soup.prettify())
    # find td with value XAU
    list = soup.find_all('td', text='XAU')
    tengramgold_value_pkr = list[0].find_next('td').text
    print(tengramgold_value_pkr.strip())
    # convert to float
    tengramgold_value_pkr = float(tengramgold_value_pkr.strip().replace(',',''))
    # get value of 1 gram gold
    onegramgold_value_pkr = tengramgold_value_pkr / 10
    return onegramgold_value_pkr
def ABCtoPKR(abc): 
    abc_constant=0.00008548031388 
    # get value of 1 gram abc
    onegramgold_value_pkr = onegramgoldValueInPKR()
    onegramabc_value_pkr = onegramgold_value_pkr * abc_constant
    # print(onegramabc_value_pkr)
    # get value of 5000 abc
    fivekabc_value_pkr = onegramabc_value_pkr * abc
    return fivekabc_value_pkr
fivekabc_value_pkr = ABCtoPKR(5000)
print("5000 abc ="+str(fivekabc_value_pkr))
def PKRtoABC(pkr):
    abc_constant=0.00008548031388
    # get value of 1 gram abc
    onegramgold_value_pkr = onegramgoldValueInPKR()
    onepkrgram=1/onegramgold_value_pkr 
    PayableGrams = pkr * onepkrgram
    abc = PayableGrams / abc_constant
    return abc
abc = PKRtoABC(5000)
print("5000 pkr ="+str(abc))
