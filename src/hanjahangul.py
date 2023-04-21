'''
All files in Hanja-Hangul are available under Creative Commons Zero v1.0 Universal.
Author: Masoris Karam KIM (masoris@gmail.com)
Version 1.03
'''

import unicodedata, re, csv, os, sys

def opencsv(filename):
    f = open(filename,'r',encoding='utf8')
    data = csv.reader(f)
    header = next(data)
    # print(f'Header: {header} \n')
    return list(data)

basepath = os.path.abspath(os.path.dirname(__file__))
dueumlist = opencsv(os.path.join(basepath, 'dueum.csv')) #두음법칙 목록 리->이
hanjalist = opencsv(os.path.join(basepath, 'hanja.csv')) #한자목록 家->가

def len_hangul(str):
    '''한글 갯수 세기'''
    str = unicodedata.normalize('NFC',str)
    len = 0
    for i in str:
        uname = unicodedata.name(i)
        if uname.find('HANGUL') != -1:
            len+=1
    return len

def only_hangul(str):
    '''한글만 추출'''
    str = unicodedata.normalize('NFC',str)
    len = ''
    for i in str:
        uname = unicodedata.name(i)
        if uname.find('HANGUL') != -1:
            len+=i
    return len

def len_hanja(str):
    '''한자 갯수 세기'''
    str = unicodedata.normalize('NFC',str)
    len = 0 
    for i in str:
        uname = unicodedata.name(i)
        if uname[:3]=="CJK": len+=1
        if uname[:6]=="KANGXI": len+=1
    return len

def only_hanja(str):
    '''한자만 추출'''
    str = unicodedata.normalize('NFC',str)
    len = '' 
    for i in str:
        uname = unicodedata.name(i)
        if uname[:3]=="CJK": len+=i
        if uname[:6]=="KANGXI": len+=i
    return len

def len_wanseong(str):
    '''완성형 한글 글자 세기'''
    str = unicodedata.normalize('NFC',str)
    len = 0 
    for i in str:
        uname = unicodedata.name(i)
        if uname[:15]=="HANGUL SYLLABLE": len+=1
    return len

def is_hangul(str):
    '''모든 글자가 한글인가?'''
    str = unicodedata.normalize('NFC',str)
    if str == '':return False
    return len(str)==len_hangul(str)

def is_hanja(str):
    '''모든 글자가 한자인가?'''
    str = unicodedata.normalize('NFC',str)
    if str == '':return False
    return len(str)==len_hanja(str)

def is_wanseong(str):
    '''모든 글자가 완성형 한글인가?'''
    str = unicodedata.normalize('NFC',str)
    if str == '':return False    
    return len(str)==len_wanseong(str)

def only_wanseong(str):
    '''완성형 한글만 추출'''
    str = unicodedata.normalize('NFC',str)
    result = re.compile('[가-힣]').findall(str)
    return ''.join(result)

def __make_dueum_a_char(char):
    '''한글자 두음법칙 적용하기'''
    char = unicodedata.normalize('NFC',char)
    if not is_hangul(char): return char
    for i in dueumlist:
        a, b = i[0], i[1]
        if a == char:
            return b
    return char

def __is_vowel_or_nieun(char):
    '''모음이나 니은 받침으로 끝나는가?'''
    if not is_hangul(char): return False
    n = (ord(char) - 0xAC00) % 28
    if n == 0 or n == 4: return True
    else: return False

def make_dueum(str):
    '''한글 한 단어에 두음법칙 적용하기'''
    str = unicodedata.normalize('NFC',str)
    if str=='' : return str #빈 문자인경우
    l = [char for char in str]
    l[0]=__make_dueum_a_char(l[0]) #첫번째 글자에 두음법칙 적용
    if len(l) == 1: return l[0] #한 글자일 경우
    # 모음이나 ㄴ 받침 뒤에 이어지는 '렬, 률'은 '열, 율'로 발음한다.
    previous = l[0]
    for i in range(1, len(l)):
        if l[i] == '렬' and __is_vowel_or_nieun(previous):
            l[i] = '열'
        elif l[i] == '률' and __is_vowel_or_nieun(previous):
            l[i] = '율'
        previous = l[i]
    return ''.join(l)

def hanja_to_hangul_simple(str):
    '''한자 하나하나를 두음법칙이 적용되지 않은 한글 대표음으로 변환'''
    str = unicodedata.normalize('NFC',str)
    for i in hanjalist:
        a, b = i[0], i[1]
        str=str.replace(a, b)
    return str

def make_splitted_hanja_list(str):
    '''한자어와 다른 요소를 리스트로 분해
    家那多羅락락락多羅aaa -> 
    ['家那多羅', '락락락', '多羅', 'aaa']
    '''
    str = unicodedata.normalize('NFC',str)
    is_hanja_list = list(range(len(str)))
    spliited = ['']
    previous = is_hanja(str[0])
    for i in range(len(str)):
        if is_hanja(str[i])!=previous:
            spliited.append('')
            spliited[-1]+=str[i]
            previous = is_hanja(str[i])
        else:
            spliited[-1]+=str[i]
            previous = is_hanja(str[i])
    return spliited            

def hanja_to_hangul_dueum(str):
    '''한자를 한글로 두음법칙을 적용하여 변환'''
    str = unicodedata.normalize('NFC',str)
    splitted = make_splitted_hanja_list(str)
    result = ''
    for i in range(len(splitted)):
        if is_hanja(splitted[i]):
            result+=make_dueum(hanja_to_hangul_simple(splitted[i]))
        else:
            result+=splitted[i]
    return result
        

# sample = '''歷史 圓周率 確率'''
# print(make_splitted_hanja_list(sample))
# print(hanja_to_hangul_dueum(sample))

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("Usage: %s 'Hanja for translate to Hangul'" % sys.argv[0])
        sys.exit(0)

    hangul_txt = sys.argv[1]
    print(hanja_to_hangul_dueum(hangul_txt))
