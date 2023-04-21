파이썬으로 만든 국한문혼용으로 쓰여 있는 글을 한글전용으로 또는 한자를 한글로 변환하는 소프트웨어입니다.

```
>> import hanjahangul
>>> text = "歷史 圓周率 確率"
>>> hanjahangul.hanja_to_hangul_dueum(text) #두음법칙을 적용하여 한자를 한글로 바꾼다.
'역사 원주율 확률'
>>> hanjahangul.hanja_to_hangul_simple(text) #두음법칙을 무시하고 한자를 한글로 바꾼다.
'력사 원주률 확률'
```
