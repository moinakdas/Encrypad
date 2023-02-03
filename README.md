# Encrypad

Encrypad is an application featuring its own encryption algorithm. At it's core, it is a substitution cipher based on a configurable dictionary located at the beginning of the script. Additional random characters are then added onto the existing text during encryption to mask the length of the original string. Furthermore, the substitution cipher runs through itself a random number of times, resulting in up to 10 different possible substitutions. For example, given the following dictionary:

```python
  encrypt={'`':'<','1':'N','2':'C','3':'E','4':'.','5':'_','6':'#','7':'I','8':'b','9':'V','0':'W','-':'1','=':'B','q':'s','w':'G','e':'T','r':'|','t':'$','y':'&','u':'-','i':'J','o':'i','p':'A','[':'9',']':'y','a':'p','s':'w','d':'h','f':'H','g':'!','h':'n','j':'P','k':'x','l':'{',';':'}',"'":'D','z':'=','x':'5','c':'/','v':'4','b':'j','n':'K','m':'~',',':'>','.':'Y','/':'m','~':'X','!':'q','@':'*','#':'l','$':'U','%':'F','^':'%','&':';','*':'r','(':'e',')':'L','_':':','+':'+','Q':'7','W':'t','E':'v','R':'2','T':'u','Y':'3','U':'M','I':']','O':'g','P':'S','{':'z','}':'o','|':'?','A':'`','S':'R','D':'[','F':'Q','G':'a','H':')','J':',','K':'6','L':'@',':':'O','Z':'\n','X':'d','C':'0','V':"'",'B':'f','N':'8','M':'(','':'k','>':'^','?':'\t','<':'','"':"Z",'\n':'c',"\t":'"'}
```

If there is one substitution, a "D" becomes a "[". If there are two substitutions, a "D" becomes a "[" and then ultimately becomes a "9". This continues for a maximum of ten possible substitutions as key value pairs are substituted back into the dictionary. Any one of ten possible substitutions are possible upon encryption, with a different substitution happening each time. 

Considering these factors, the algorithm generates a new encrypted string every time. While the possibility of the same input string yielding the same output string is highly unlikely, it is theoretically possible should the randomly chosen letters at the end of the input string match in two cases. In order to make this algorithm more secure, a more cryptographically sound random function should be utilized.

## Getting Started

These instructions will help you get a copy of Encrypad's source code up and running on your local machine for development and testing purposes.

### Installing

```
git clone https://github.com/Sadkoi/Encrypad.git
```

2. In the same directory to where you downloaded the repository, create a directory named "Encryption.io"

3. Open the project in any python editor and run

## Usage

The Encrypad window contains two panels. The top panel is the input window, which is where you type the string to be encrypted. The bottom panel is the encryption window, which shows the encrypted output. At any point, the current encrypted output can be saved by entering a filename at the bottomost input field, and clicking on save. The resulting .txt file will be located in the "Encryption.io" directory and can only be decrypted by the Encrypad program loaded with the same dictionary used to encrypt it. There is also an option to view the current .txt files in the "Enctyption.io" directory. To open any one of these files, type out the file name in the bottommost text input field and click on the open button.

## Built With

- python 
- tkinter


## Contributing

If you would like to contribute to the development of Encrypad, please reach out to Moinak.Das@stonybrook.edu.

## License

EmerGo is released under the [MIT License](https://opensource.org/licenses/MIT).
