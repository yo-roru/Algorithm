import time
def Optimal_BST(p,q,n):
  e=[[0 for a in range(0,n+1)] for b in range(0,n+2)] #儲存每個區間的最佳效率
  w=[[0 for a in range(0,n+1)] for b in range(0,n+2)] #儲存每個點的權重
  root=[[0 for a in range(0,n+1)] for b in range(0,n+1)] #儲存每個區間的最佳分割位置
  for i in range(1,n+2): #將最初開始值放入效率解及權重
    e[i][i-1]=q[i-1]
    w[i][i-1]=q[i-1]
  for l in range(1,n+1):  #由下至上計算
    for i in range(1,n-l+2):  #每行從最左邊算至最右邊
      j=i+l-1 
      e[i][j]=-1 #假設-1為無限大
      w[i][j]=w[i][j-1]+p[j]+q[j] #先計算每點權重
      #print(i,",",j,",",format(w[i][j],".2f"))
      for r in range(i,j+1): #計算找到區間的最佳子結構 最小值最有效率的解
        t=e[i][r-1]+e[r+1][j]+w[i][j]   #利用重複的特性 找最佳解
        if t<e[i][j] or e[i][j]==-1:  #比較每個子結構 找到最小值最佳解
          e[i][j]=t
          root[i][j]=r #root 儲存最小值的最佳分割位置
          #print(e[i][j])
  return e,w,root #回傳 最佳效率 權重 最佳分割位置
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
  start=time.time() #計算開始時間
  TXT=open("hw2_input_k12.txt","r") #讀取txt檔檔
  input=TXT.readlines() #以line 存取
  proDummyKey=list(map(float,input[3].split(' '))) #不存在的點計算到的機率
  proKey=list(map(float,input[1].split(' '))) #節點計算到的機率
  lenKey=len(proKey) #節點數量
  proKey.insert(0,0)
  e,w,root=Optimal_BST(proKey,proDummyKey,lenKey)
  end=time.time() #結束時間
  print("Cost of the optimal binary search tree is ",end="")
  print(round(e[1][lenKey],2))
  print("Optimal binary search tree:")
  print("以前序表示：",end="")
  printTree(root,1,lenKey,0)
  print("(大的放在父元素右邊放，小的放在父元素左邊)")
  print("執行時間：%f ms"%((end-start)*1000))
