import copy

listdata1 = [ 30, 50, [80,90], "python"]

listdata2 = listdata1 # 이건 주소를 복사한것, 복사된게 아님
listdata3 = copy.copy(listdata1)
listdata1[0] = 88
print(listdata2, id(listdata2))
print(listdata1, id(listdata1))
print(listdata3, id(listdata3))

listdata4 = copy.deepcopy(listdata1)
# 원본을 복사한건데 반영을 시켰는지 여부가 중요함
# 리스트 내부네 이스크를 퐇마하고 있을 경우에는 사본객체를 형성할대
# copy가 아니라 copy.decopy를 사용하자