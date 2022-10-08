#Maximum-subarray
import time
#計算low至high區間中最大值
def FIND_MAX_CROSSING_SUBARRAY(A,low,mid,high):
  max_left=0
  max_right=0
  left_sum=-100000000 #左區間最大值
  sum=0
  for i in range(mid,low-1,-1):#找出從mid至low的區間最大值
    sum=sum+A[i] 
    if sum>left_sum:
      left_sum=sum
      max_left=i #最低點
  right_sum=-1000000000 #右區間最大值
  sum=0
  for j in range(mid+1,high):#找出從mid至high的區間最大值
    sum=sum+A[j]
    if sum>right_sum:
      right_sum=sum
      max_right=j #最高點
  return (max_left,max_right,left_sum+right_sum) #回傳 最低點最高點及區間最大值
def FIND_MAXIMUM_SUBARRAY(A,low,high):
  if high==low: #已經切到無法再切了
    return (low,high,A[low]) #直接回傳
  else:
    mid=int((low+high)/2)
    (left_low,left_high,left_sum)=FIND_MAXIMUM_SUBARRAY(A,low,mid) #分割成左邊子數列
    (right_low,right_high,right_sum)=FIND_MAXIMUM_SUBARRAY(A,mid+1,high) #分割成右邊子數列
    #分割至最小後開始計算開始，並回傳比較，比較完後持續結合
    (cross_low,cross_high,cross_sum)=FIND_MAX_CROSSING_SUBARRAY(A,low,mid,high) 
    if left_sum>=right_sum and left_sum>=cross_sum: #若左數列相加最大回傳最大值及最低點及最高點
      return(left_low,left_high,left_sum)
    elif right_sum>=left_sum and right_sum>=cross_sum: #若右數列相加最大回傳最大值及最低點及最高點
      return(right_low,right_high,right_sum)
    else: #若中間相加最大回傳最大值及最低點及最高點
      return(cross_low,cross_high,cross_sum)
if __name__=="__main__":
  start=time.time() #計算開始時間
  TXT=open("D:\MyData\大三上\演算法\input_96.txt","r") #讀取txt
  input=TXT.readlines() #以line 存取
  Len=int(input[0][0:len(input[0])-1]) #資料筆數
  Data=list(map(float,input[1].split(','))) #股價資料
  Interval=list() #存取兩天間差值
  for i in range(0,len(Data)-1): #計算前後兩天相對差值
    Interval.append(Data[i+1]-Data[i])
  ANS=FIND_MAXIMUM_SUBARRAY(Interval,0,len(Interval)-1) #丟入副程式計算最大子數列
  end=time.time() #結束時間
  print("共讀入",Len,"筆股價資料")
  print("第",ANS[0],"日收盤買進第",ANS[1]+1,"日收盤賣出就對了！")
  print("執行時間：%f ms"%((end-start)*1000))
