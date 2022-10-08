#暴力解
import time

#計算每一天間的差值後，做比較，找出最大值
def everyDiff(Adjacent): #Adjacent為兩天間相鄰的差值
  everyAdj=list() #存取每一天間的差值
  #計算每一天間的差值
  for i in range(len(Adjacent)): #由第i天開始
    thisline=list() #存取第i天到其他天差值
    sum=0 #初始值設定回0
    for j in range(i,len(Adjacent)):#第i天到第某j天的差值，全部存入thisline
      sum=sum+Adjacent[j]
      thisline.append(sum)
    everyAdj.append(thisline) #第i天計算完存入
  MAX=0 #設定最大差值初始值
  for i in range(len(everyAdj)):#找最大差值
    LineMax=max(everyAdj[i])#第i天到第某天的最大值  
    if(LineMax>MAX): #LineMax跟MAX做比較 ，若大於則更新最大值
      MAX=LineMax 
      low=i  #第i天買進
      high=everyAdj[i].index(MAX)+i+1 #第某天賣出
  return (low,high,MAX) #回傳最大獲利區間及買進日即賣出日

if __name__=="__main__":
  start=time.time() #計算開始時間
  TXT=open("D:\MyData\大三上\演算法\input_96.txt","r") #讀取txt
  input=TXT.readlines() #以line 存取
  #print(input)
  Len=int(input[0][0:len(input[0])-1]) #資料筆數
  Data=list(map(float,input[1].split(','))) #股價資料

  Interval=list() #存取兩天間差值
  for i in range(0,len(Data)-1): #計算前後兩天相對差值
    Interval.append(Data[i+1]-Data[i])
  ANS=everyDiff(Interval)#給Interval兩天間相鄰差值，並計算每一天間的差值後，做比較，找出最大值
 
  end=time.time() #結束時間
  print("共讀入",Len,"筆股價資料")
  print("第",ANS[0],"日收盤買進第",ANS[1],"日收盤賣出就對了！")
  print("執行時間：%f ms"%((end-start)*1000))
