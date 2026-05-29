import numpy as np # as : numpy를 np로 사용하겠다 라는 별칭 부여 문법

# 1, 2, 3, 다차원 배열 형태의 데이터를 생성하고 연산할 필요가 있다
# 리스트의 단점, 스칼라랑 더하기 연산하면 안된다 등, 브로드캐스팅을 사용해서 넘파이를 사용한다?
# 넘파이 배열을 생성
# arr1 = np.array([ [5, 6, 7, 8], [5, 6, 7, 8] ]) # 리스트를 이용해서 넘파이 배열 객체를 생성
# arr2 = np.array( [ [5], [6] ,[7], [8] ])
# arr3 = np.array([ [ [5], [6] ,[7], [8] ],[ [5], [6] ,[7], [8] ] ] )
# print(arr1) # , 가 없다는 것이 리스트와의 차이점
# print(arr2)
# print(arr3)
# print( arr1.ndim ) # 배열의 차원수를 반환
# print( arr1.shape ) # 배열의 형태를 반환 (행, 렬) 1차원은 (4, ) 로 표현함
# # (4, ) 는 1차
# # (4, 1)은 4행 1열 2차를 의미함[[5] [6] [7] [8]]
# # (4, 1, 1)는 4묶음 1행 1열

# 범위데이터를 이용해서 넘파이 배열을 생성
arr2 = np.arange(1,21).reshape((4, 5)) # 3, 4 그대로 줘도 되는데 정확하게 하려면 shape을 튜플로 제공
print(arr2)
# 넘파이 배열 select 문법
print( arr2[1][2])
print( arr2[3][3])
subset =  arr2[1:3,1:3 ] # arr[ 행슬라이싱, 열슬라이싱] 이걸 쓰도록 하자
print(subset)
print( arr2[1:3][1:3]) # 모양이 틀려서 안되는 것, shape이 틀려서 안된다고 함 1차원일땐 돌아감 될떄 안될때가 있으니 참고
print(arr2[1:4, 3:5]) # 1: 걍 끝까지니까 밀자
print(arr2[:3, :3])

# #  임의의 난수 넘파이 배열 생성
# arr3 = np.random.randint(1, 100, (4,5))
# print(arr3)

arr_zero = np.zeros((24, 24)) # 배열의 내용을 0으로 채워서 배열을 생성해줌
print(arr_zero)

arr_one = np.ones((4, 4))
print(arr_one)