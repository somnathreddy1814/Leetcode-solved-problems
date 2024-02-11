class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        max_elements=[]
        for i in range(len(matrix[0])):
            temp=[]
            for j in range(len(matrix)):
                temp.append(matrix[j][i])
            max_elements.append(max(temp))
        
                
        for i in range(len(matrix)):
            temp=[]
            for j in range(len(matrix[0])):
                if matrix[i][j]==-1:
                    matrix[i][j]=max_elements[j]
        return matrix
        
        
        