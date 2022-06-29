# Ethereum-Signature-Parser



## 🚩 ABSTRACT

This script helps in parsing and extracting functions calls in the Ethereum Virtual Machine from the [Ethereum Signature Database](https://www.4byte.directory/). 

## 💁 Method Employed

It accomplishes the above task by simply running the fetching and processing for each page as a seperate thread and parallelly saving their results. Each page is processed 
using the BeautifulSoup library, to parse for table entities in the given page. The parsed data are then concurrently stored in the common [CSV](https://github.com/Neelaksh-Singh/Ethereum-Signature-Parser/blob/main/Parsed.csv) file.

## 💻 Get Started

`!!! Ensure that you have the required Libraries. !!!` <br>
Replace with the current page range of the site in [here](https://github.com/Neelaksh-Singh/Ethereum-Signature-Parser/blob/f29f3571c47b3c92df1561f957ecbefb4580435d/Eth_Sig_Parser.py#L35) in place of 42325.
```console
$ git clone https://github.com/Neelaksh-Singh/Ethereum-Signature-Parser.git
$ cd Ethereum-Signature-Parser/
$ python Eth_Sig_Parser.py
```


