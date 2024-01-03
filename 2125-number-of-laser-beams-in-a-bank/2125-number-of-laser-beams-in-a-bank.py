class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        previous_count=0
        final_count=0
        for i in range(len(bank)):
            current_count=0
            current_count=bank[i].count('1')
            final_count+=previous_count*current_count
            if current_count==0:
                continue
            else:
                previous_count=current_count
        return final_count
                    
        