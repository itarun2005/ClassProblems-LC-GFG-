class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        rows=[""]* numRows
        currentrow=0
        goingdown=False
        for c in s:
            rows[currentrow]+= c
            if currentrow==0 or currentrow==numRows-1:
                goingdown=not goingdown
            currentrow+=1 if goingdown else -1
        return "".join(rows)
        