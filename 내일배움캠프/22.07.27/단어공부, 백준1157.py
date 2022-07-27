"""
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
"""


input = "baaa".upper()
input_list = list(set(input))

cnt = []
for i in input_list:
    count = input.count
    cnt.append(count(i))


if cnt.count(max(cnt)) > 1:
    print("?")

else:
    print(input_list[(cnt.index(max(cnt)))])

