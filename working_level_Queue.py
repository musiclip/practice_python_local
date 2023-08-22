## 함수
def isQueueFull():
    global SIZE, queue, front, rear
    #if rear >= SIZE -1 :
        #return True
    #else:
        #return False
    if rear != SIZE -1 :
        return False
    elif rear == SIZE-1 and front == -1:
        return True
    elif rear == SIZE -1 and front != -1:
        for i in range(front+1, SIZE, 1):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False
    
def enQueue(data):
    global SIZE, queue, front, rear
    if isQueueFull():
        print('큐가 꽉 찼다.')
        return
    rear += 1
    queue[rear] = data

def isQueueEmpty():
    global SIZE, queue, front, rear
    if front == rear :
        return True
    else:
        return False
    
def deQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('큐가 텅 비었다.')
        return
    front += 1
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('큐가 텅 비었다.')
        return
    return queue[front + 1]    

## 변수
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear= -1

## 메인
enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
enQueue('선미')

#print('출구 <--', queue, '<-- 입구')

#nQueue('원더걸스')

retData = deQueue()
print('손님 이리로 ==>', retData)
print('준비하세요 :', peek())
retData = deQueue()
print('손님 이리로 ==>', retData)
#print('준비하세요 :', peek())
#retData = deQueue()
#print('손님 이리로 ==>', retData)

enQueue('재남')
enQueue('정국')
print('출구 <--',queue, '<-- 입구')
enQueue('길동')
print('출구 <--',queue, '<-- 입구')
retData = deQueue()
print('손님 이리로 ==>', retData)
enQueue('길동')
print('출구 <--',queue, '<-- 입구')