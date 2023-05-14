파이썬으로 만든 한자를 한글로 또는 국한문혼용으로 쓰여 있는 글을 한글전용으로 변환하는 모듈입니다. 유니코드 정규화(Unicode Normalization)된 한자 또한 두음법칙이 적용된 한글로 변환 가능합니다.

# 사용법
두음법칙을 적용하여 한자를 한글로 바꾼다.
```python
>>> from hanjahangul import *
>>> hanja_to_hangul_dueum("歷史 圓周率 確率")
'역사 원주율 확률'
```
두음법칙을 무시하고 한자를 한글로 바꾼다.
```python
>>> hanja_to_hangul_simple("歷史 圓周率 確率")
'력사 원주률 확률'
```
한글만 추출한다.
```python
>>> only_hangul("역사 歷史")
'역사'
```
한자만 추출한다.
```python
>>> only_hanja("역사 歷史")
'歷史'
```
모든 글자가 한글인가?
```python
>>> is_hangul("역사")
True
```
모든 글자가 한자인가?
```python
>>> is_hanja("歷史")
True
```

# 저작권
CC0-1.0 license 라이센스로 누구나 자유롭게 이용할 수 있습니다.

Masoris Karam KIM ( masoris@gmail.com )