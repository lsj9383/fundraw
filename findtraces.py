import numpy as np

class Point:
    row = 0
    col = 0
    maxrow = 0
    maxcol = 0
    oplist = []
    def __init__(self, row, col, maxrow, maxcol):
        self.row = row
        self.col = col
        self.maxrow=maxrow
        self.maxcol=maxcol
        self.oplist = [[-1, -1], [-1, 0], [-1, 1], \
                            [ 0, 1], \
                  [ 1, -1], [ 1, 0], [ 1, 1],]
    def __iter__(self):
        for op in self.oplist:
            nextrow = self.row+op[0] 
            nextcol = self.col+op[1]
            if (nextrow > self.maxrow or nextrow < 0 or \
                nextcol > self.maxcol or nextcol < 0):
                continue
            yield Point(nextrow, nextcol, self.maxrow, self.maxcol)

# 查询端点, 递归
def __find_endpoint_rec__(onep, visited, deep):
    visited[onep.row][onep.col] = True
    deeps = []
    ps = []
    for nextp in onep:
        if not visited[nextp.row][nextp.col]:
            tdeep, tp = __find_endpoint_rec__(nextp, visited, deep+1)
            deeps.append(tdeep)
            ps.append(tp)
    if len(deeps) == 0:
        return deep, onep
    else:
        maxdeep = max(deeps)
        return maxdeep, ps[deeps.index(maxdeep)]

# 查询端点, 迭代
def __find_endpoint__(onep, visited, deep):
    q = []
    q.append({"pt":onep,"deep":0})
    maxdeep = -1
    endp = None
    while len(q):
        p = q.pop()                 # 出栈
        if(visited[p['pt'].row][p['pt'].col]):  # 该点已经到过
            continue
        visited[p['pt'].row][p['pt'].col]=True  # 
        if maxdeep<p['deep']:
            maxdeep = p['deep']
            endp = p['pt']
        q.extend([{"pt":pt, "deep":p['deep']+1} for pt in list(p['pt'])])           # 下一批入队
    return maxdeep, endp
        
# 通过端点查询路径
def __trance_by_endpoint__(endpoint, visited):
    bfs = 0
    dfs = -1
    use = dfs
    q = []
    trace = []
    q.append(endpoint)
    while len(q):
        p = q[use]                  # 取出栈顶或是队首元素，由use决定
        del q[use]                  # 删除栈顶或是队首元素，由use决定
        if(visited[p.row][p.col]):  # 该点已经到过
            continue
        visited[p.row][p.col]=True  # 
        trace.append(p)             # 取出放至路径的下一个点
        q.extend(list(p))           # 下一批入队
    return trace

# 搜寻
def do(img):
    visited = img.copy()            # True为已经查询过的点
    rows = img.shape[0]
    cols = img.shape[1]
    traces = []
    print("loading", end='', flush=True)
    for rown in range(0, rows):
        print(".", end='', flush=True)
        for coln in range(0, cols):
            if not visited[rown][coln] :
                _, endpoint = __find_endpoint__(Point(rown, coln, rows-1, cols-1), visited.copy(), 0)
                traces.append(__trance_by_endpoint__(endpoint, visited))
    return traces