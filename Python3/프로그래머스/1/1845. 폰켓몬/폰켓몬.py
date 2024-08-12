def solution(nums):
    output = []
    
    for i in nums:
        if output.count(i) == 0:
            output.append(i)
            
    if len(output) > len(nums)/2:
        return len(nums)/2
    else:
        return len(output)
