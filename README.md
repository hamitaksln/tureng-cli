# `tureng-cli` - Tureng CLI
## Tureng CLI is a very basic command line tool for tureng.com

## Install
```
pip install tureng-cli
```

## Usage
```python
Usage:
tureng.py tr <word>
tureng.py en <word>

-h --help help
```
## Example
### tr-en
```
$ tureng tr bilgisayar
https://tureng.com/en/turkish-english/bilgisayar
Word: bilgisayar Language: tr
----------------------------------------
computer
hardware system
machine
data computer
computing device
computing machine
thinking-machine
machine
computer
computer
```
### en-tr
```
$ tureng en computer
https://tureng.com/en/turkish-english/computer
Word: computer Language: en
----------------------------------------
bilgisayar
kompüter
elektronik beyin
bilgisayar
kompüter
bilgisayar
kompütör
bilgi sayar
bilgisayarı kapatmak
bilgisayarı çökmek
```
## Requirements
```
requests==2.25.1
docopt==0.6.2
selectolax==0.2.11
```