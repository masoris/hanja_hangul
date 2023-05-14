파이썬으로 만든 한자를 한글로 또는 국한문혼용으로 쓰여 있는 글을 한글전용으로 변환하는 모듈입니다. 유니코드 정규화(Unicode Normalization)된 한자 또한 두음법칙이 적용된 한글로 변환 가능합니다.  
This is a module made in Python that converts text written in Hanja (Chinese characters) or a mixture of Hangul and Hanja into Hangul-only text. Chinese characters in Unicode normalization can also be converted into Hangul text.

## 사용법 How to use
두음법칙을 적용하여 한자를 한글로 바꾼다.  
Convert Hanja to Hangul with South Korea style.
```python
>>> from hanjahangul import *
>>> hanja_to_hangul_dueum("歷史 圓周率 確率")
'역사 원주율 확률'
>>> hanja_to_hangul_dueum("大韓民國의 主權은 國民에게 있고, 모든 權力은 國民으로부터 나온다.")
'대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다.'
```
두음법칙을 무시하고 한자를 한글로 바꾼다.  
Convert Hanja to Hangul with North Korea style.
```python
>>> hanja_to_hangul_simple("歷史 圓周率 確率")
'력사 원주률 확률'
```
한글만 추출한다.  
Extract only Hangul.
```python
>>> only_hangul("역사 歷史")
'역사'
```
한자만 추출한다.  
Extract only Hanja.
```python
>>> only_hanja("역사 歷史")
'歷史'
```
모든 글자가 한글인가?  
Are all the characters Hangul?
```python
>>> is_hangul("역사")
True
```
모든 글자가 한자인가?  
Are all the characters Hanja?
```python
>>> is_hanja("歷史")
True
```

## 저작권 License
CC0-1.0 license 라이센스로 누구나 자유롭게 이용할 수 있습니다.  
It can be freely used by anyone under the CC0-1.0 license.

Masoris Karam KIM ( masoris@gmail.com )