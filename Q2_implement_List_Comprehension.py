
#['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
input_str='ACADGILD'
result_str=[i for i in input_str]

print(result_str)


#['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
input_str=list('XYZ')
result_str=[i*j for i in input_str for j in [1,2,3]]
result_str

#['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
input_str=list('XYZ')
result_str=[i*j for i in range(1,5) for j in input_str]
result_str

#[[2], [3], [4], [3], [4], [5], [4], [5], [6]]
num = [1,2,3]
numlist=[[i+j] for i in num for j in [1,2,3]]
numlist

#[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
num = [2,3,4,5]
numlist=[[i+j for i in num] for j in [1,2,3]]
numlist


#[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
nums=[1,2,3]
numlist=[(b,a) for b in nums for a in nums]
numlist