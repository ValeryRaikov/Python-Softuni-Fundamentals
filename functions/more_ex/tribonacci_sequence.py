def tribonacci(n):
    start = 1
    result_list = [start]
    output_list = [start]
    for i in range(1, n):
        if i < 2:
            result_list.append(start)
        else:
            if i >= 4:
                result_list.remove(result_list[0])
                output_list.append(result_list[0])
                
            result_list.append(sum(result_list))
    result_list.remove(result_list[0])       
    output_list.extend(result_list)
            
    for num in output_list:
        print(num, end = " ")
    
n = int(input())
tribonacci(n)