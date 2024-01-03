class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        previous_count=0
        final_count=0
        for i in range(len(bank)):
            current_count=0
            for j in range(len(bank[i])):
                if bank[i][j]=='1':
                    current_count+=1
            final_count+=previous_count*current_count
            print(final_count)
            if current_count==0:
                continue
            else:
                previous_count=current_count
        return final_count
                    
        