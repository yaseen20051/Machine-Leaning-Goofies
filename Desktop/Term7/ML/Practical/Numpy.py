import numpy as np




## checking numpy version
def numpy_version():
    print(np.__version__)





if __name__ == "__main__":
    try:
        numpy_version()

        # creating ndarray (N-dimensional object) 
        # using array([])  
        # arguments : List 
        arr = np.array([1,2,3,4,5,6])
        print(arr)
        print(type(arr))  ## ----> object of ndarray class

        ## Dimensions of arrays 

        zero_dim_arr = np.array(7)
        print(zero_dim_arr)

        one_dim_array = np.array([2005,2206,2013])
        print(one_dim_array)

        two_dim_array = np.array([[1,2,1],[3,6,9]])   ## two rows  three columns
        print(two_dim_array)


        print(zero_dim_arr.ndim)
        print(one_dim_array.ndim)
        print(two_dim_array.ndim)

        three_dim_array = np.array([[[1,2,3],[9,8,1]],[[4,5,6],[10,8,3]]],ndmin=3)
        print(three_dim_array)
        print(three_dim_array.ndim)


        ## Accessing array elements

        print(one_dim_array[0])
        # print(one_dim_array[3])  ## out of index


        print(two_dim_array[1,1])

        print(three_dim_array[1,0,-2])

        ## Slicing array [start = 0 if none : end = len(arr) if none  : step = 1 if none]

        arr = np.array([1, 2, 3, 4, 5, 6, 7])

        print(arr[1:3])

        print(arr[4:])

        print(arr[:5])

        print(arr[-6:-1:2]) ## using step argument

        print(arr[::2])


        arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

        print(arr[1,1:4])

        print(arr[0:2,2])

        print(arr[0:2,1:4])

        ## Data types
        print(arr.dtype)

        arr = np.array([1,2,3])
        print(arr.dtype)

        fruits = np.array(["apple","bananna","Melons"])
        print(fruits.dtype)
        print(fruits.ndim)

        ## Data type converting 
        
        float_nums_arr = np.array([1.23,1.5,2.5])

        int_converted_arr = float_nums_arr.astype('i')

        print(int_converted_arr)

        string_converted_array = float_nums_arr.astype('U')

        print(string_converted_array)

        arr = np.array([-1,3,0])

        boolean_array = arr.astype(bool)
        third_copy_array = arr.astype('b')

        print(boolean_array)
        print(third_copy_array)

        ## Copy vs View 

        names = np.array(["Yaseen","Yahia"])
        copy_arr = names.copy()
        view_arr = names.view()
        copy_arr[1] = "Islam" ## doesnot affect the original array
        view_arr[0] = "Dan"  ## Affect the original array 
        print(names)
        print(copy_arr)
        print(copy_arr.base)
        print(view_arr.base)

        # Iterate on Array 
        arr = np.array([1,2,3,4,5])
        for num in arr :
            print(num)
        sd_array = np.array([[2,4,1],[4,6,7]]) 
                           
        for num in sd_array:
            print(num)
        for num in np.nditer(sd_array):
            print(num)
    
        arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]],dtype='i')
        print(type(5))
        for x in np.nditer(arr):
         print(x.dtype)
        print("###############################################################################")
        arr = np.array([1,2,3,4,5])

        for num in np.nditer(arr):
            num = num.astype('U') 
            print(num.dtype)
        
        for num in np.nditer(arr,flags=['buffered'],op_dtypes='U'):
            print(num.dtype)


        # for num in np.nditer(arr,flags=['buffered'],op_dtypes=['U']):
        #     print(num)

        arr = np.array([1,2,3,4])
        for x in np.nditer(arr):
            x = x*2

        print(arr)

        # TO edit the array we must use ellipsis indexing = select everthing && op_flags = ['readwrite']
        for x in np.nditer(arr,op_flags=['readwrite']):
            x[...] = x*2 ##ellipsis indexing
        print(arr)
        arr = np.array([[1, 2, 3, 4,6,8], [5, 6, 7, 8,10,12]])

        for x in np.nditer(arr[:1,:],op_flags=['readwrite']):
            x[...] = x * 0
        
        for row in arr:
            print(row)

        ## Enumeration : Listing items giving them indecies

        arr = np.array([[[1,2,3],[4,5,6]],[[8,9,10],[12,13,14]]])

        for index,num in np.ndenumerate(arr):
            print(f"Element at {index} = {num} ")

        ## getting elements that statisfy a specific purpose 
        odd_positions = [index for index,num in np.ndenumerate(arr) if num%2 == 1]
        print(odd_positions)

        ## Numpy Joining (Concatination and Stacking)
        a = np.array([[[1,2,3]],[[4,5,6]]])
        b = np.array([[[10,12,43]],[[50,1,2]]])
        axis0 = np.concatenate([a,b],axis=0)
        axis1 = np.concatenate([a,b],axis=1)
        axis2 = np.concatenate([a,b],axis=2)
        print(f"axis zero : \n{axis0}")
        print(f"\naxis one : \n{axis1}")
        print(f"\naxis two : \n{axis2}")
        arr1 = np.array([1, 2, 3])

        arr2 = np.array([4, 5, 6])
        print("#################################### Arrays Joining ###########################################")
        concatenatedArray = np.concatenate([arr1,arr2])
        stackingArray = np.stack([arr1,arr2])
        vstack = np.vstack([arr1,arr2])
        hstack = np.hstack([arr1,arr2])
        depthStack = np.dstack([arr1,arr2])
        print(f"concatenated array : {concatenatedArray}")
        print(f"stacked array : \n{stackingArray}")
        print(f"Vertical array : \n{vstack}")
        print(f"Horizontal array : \n{hstack}")
        print(f"Depth array : \n{depthStack}")

        print("#################################### Arrays Splitting ###########################################")
        nums = np.array([1,2,3,4,5,6,7,8,9])
        slicied_array = np.array_split(nums,3)
        print(slicied_array)
        print(type(slicied_array))
        print(slicied_array[2])
        print(type(slicied_array[0]))
        arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

        newarr = np.array_split(arr, 3)

        print(newarr[0]) 

        arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

        newarr = np.array_split(arr, 3)

        print(newarr[0]) 

        arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

        newarr = np.array_split(arr, 3, axis=1)

        print(f"\n{newarr[0]}") 
        print("#################################### Arrays Searching ###########################################")
        nums = np.array([1,2,3,4,5,2,4,3,2])
        num = np.where(nums == 2)     ### O(n)
        print(num)
        num = np.where(nums == 8)
        print(num)

        nums_sorted = np.array([1,2,2,2,2,2,3,4,6,7,8])
        index = np.searchsorted(nums_sorted,2)    ### O(logn)
        print(index)
        multiple_values = np.searchsorted(nums_sorted,[1,2,4,8])
        print(multiple_values)
        numberOf2s = np.searchsorted(nums_sorted,2,side='right') - np.searchsorted(nums_sorted,2,side="left") 
        print(numberOf2s)

        print("#################################### Arrays Filtering ###########################################")

        arr = np.array([4,5,6,7,8,9,10,12,13,14,15])
        filtered_array = arr % 2 == 0    ## O(n)
        print(filtered_array)
        print("#################################### Arrays Sorting (do quick sorting algorthim) ###########################################")
        arr = np.array([10,9,8,7,6,5,4])
        sortedarray = np.sort(arr)
        print(arr)
        print(sortedarray)
        arr = np.sort(arr)
        print(arr)

        test_point = np.array([0,0.25,0.8])
        arr = np.array([[0.5,0.25,0.6],[0.5,0.25,0.05],[0,0.5,0.8],[1,0.75,0.3],[0.5,1,1],[1,0,0],[0.5,0,0],[1,0.75,0.65]])
        squareArray = np.square(arr-test_point)
        sum = 0 
        distances = np.array([])
        distancesIndexed_list = []
        for row in squareArray:
            for feature in np.nditer(row):
                sum = sum + feature 
            distances = np.append(distances,np.sqrt(sum))
            sum = 0
        

        for index,value in np.ndenumerate(distances):
            index_value = (index[0]+1,value)
            distancesIndexed_list.append(index_value)
        
        
        distancesIndexed = np.array(distancesIndexed_list)   

        print(distancesIndexed)
      
        distancesIndexed = distancesIndexed[distancesIndexed[:, 1].argsort()]
       
            
        print(distancesIndexed)
        














    except Exception as exp:
        print(f"error : {exp}")