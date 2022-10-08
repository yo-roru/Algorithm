import time
def recu_OBST(p,i,j):
  if j==i-1:  #初始始值未開始為不存在的點
    return proDummyKey[i-1]
  min=1000000000 #假設起始值為無限大來做比較
  for a in range(i,j+1):  #計算區間i到j的最佳效率解
    time=recu_OBST(p,i,a-1)+recu_OBST(p,a+1,j)+w[i][j] #time 計算每個可能性的花費時間
    if time<min:  #並找到最小花費時間
      min=time
      root[i][j]=a  #將分割的最佳區間的點存在root
  return round(min,2)  #回傳最佳效率解

def weight(p,q,n):  #迴圈計算出每個區間的權重
  w=[[0 for a in range(0,n+1)] for b in range(0,n+2)] #儲存每個權重
  for i in range(1,n+2):
    for j in range(0,n+1):
      for l in range(i,j+1):
        w[i][j]=w[i][j]+p[l]
      for l in range(i-1,j+1):
        w[i][j]=w[i][j]+q[l]
  return w

def printTree(rootData,s,n,count): #表示二元搜尋樹
  if count!=0:
    print(",",end="")
  count=count+1
  root=rootData[s][n]
  print("k",root,end="") #輸出前序二元搜尋樹的排列
  
  if root !=0 and s+1<=n and root-1>=s:#左子樹向下執行後，沒有節點後，再依序往右子樹執行
    left=printTree(rootData,s,root-1,count)
  if root !=0 and s+1<=n and root+1<=n:
    right=printTree(rootData,root+1,n,count)
    
if __name__=='__main__':
  start=time.time()#計算開始時間
  TXT=open("hw2_input_k12.txt","r") #讀取txt
  input=TXT.readlines() #以line 存取
  proDummyKey=list(map(float,input[3].split(' ')))  #不存在的點計算到的機率
  proKey=list(map(float,input[1].split(' ')))#節點計算到的機率
  lenKey=len(proKey) #節點長度
  proKey.insert(0,0)
  root=[[0 for a in range(0,lenKey+1)]for b in range(0,lenKey+1)] #儲存最佳解分割的點
  w=weight(proKey,proDummyKey,lenKey) #計算每個區間的權重
  OBST=recu_OBST(proKey,1,lenKey) #以遞迴方式計算出最佳解
  end=time.time() #結束時間
  print("Cost of the optimal binary search tree is ",end="")
  print(OBST)
  print("Optimal binary search tree:")
  print("以前序表示：",end="")
  printTree(root,1,lenKey,0)
  print("(大的放在父元素右邊放，小的放在父元素左邊)")
  print("執行時間：%f ms"%((end-start)*1000))
