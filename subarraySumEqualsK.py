def subarraySum(nums,k):
    count = 0
    prefix_sum = 0

    #crítico: inicializar com {0:1}
    #inicializar com o zero.
    sum_freq = {0:1}

    for num in nums:

        prefix_sum += num
        print(prefix_sum)


        #checa se existe um subarray com soma = k:
        #prefix_sum - k  significa o quanto falta

        #depois - antes = k
        #depois - k = antes?

        if prefix_sum - k in sum_freq:
            count += sum_freq[prefix_sum-k]

        
        # Eu aumento sempre que sei fazer o "left"
        sum_freq[prefix_sum] = sum_freq.get(prefix_sum,0)+1
        print(sum_freq)
        print("count = ",count)

    return count
#para cada elemento calcula o prefix
#se existir um prefix - valor, então existe o subarray

nums = [1,2,3,4,5]
k = 5
print(subarraySum(nums,k))