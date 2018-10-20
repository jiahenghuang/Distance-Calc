#1、欧式距离：

import numpy as np
vec1=np.array([1,2,3])
vec2=np.array([4,5,6])
print np.sqrt((vec1-vec2)*(vec1-vec2).T)
#或者
print((vec1-vec2)*(vec1-vec2).T)**0.5

#2、哈曼顿距离：
     
import numpy as np
vec1=np.array([1,2,3])
vec2=np.array([4,5,6])
print sum(np.abs(vec1-vec2))

#3、切比雪夫距离
     
import numpy as np
vec1=np.array([1,2,3])
vec2=np.array([4,5,6])
print np.abs((vec1-vec2).max())

#4、夹角余弦

import numpy as np
vec1=np.array([1,2])
vec2=np.array([3,4])
cosv12=np.dot(vec1,vec2)/(np.linalg.norm(vec1) * (np.linalg.norm(vec2)))
print cosv12

#5、汉明距离

import numpy as np
vec1=np.mat([1,1,1,1])
vec2=np.mat([1,0,0,1])
smstr=np.nonzero(vec1-vec2)
print np.shape(smstr)[1]

#6、杰卡德相似系数

import numpy as np
import scipy.spatial.distance as dist
matv=np.mat([[1,1,0,1],[0,1,1,0]])
print "dist.jaccard",dist.pdist(matv,'jaccard')
