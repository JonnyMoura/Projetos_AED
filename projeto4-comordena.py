# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 14:42:22 2022

@author: joanm


"""

from sys import stdin,stdout
import math,random,time


def readln():
    return stdin.readline().rstrip().split(" ")


'''def insertionSort(arr,low,high):
  
    # Traverse through 1 to len(arr)
    for i in range(low, high+1):
  
        key = arr[i]
  
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key                    
def swap(arr,index1,index2):
    tmp= arr[index1]
    arr[index1]=arr[index2]
    arr[index2]=tmp
    
def quicksort(raster_arr, low, high):
    cutoof=30
    if low+cutoof>high:
        insertionSort(raster_arr,low,high)
    else:
        med = (low+high)//2
        if raster_arr[med] < raster_arr[low]:
            swap(raster_arr, low, med )
        if raster_arr[high] < raster_arr[low]:
            swap(raster_arr, low, high )
        if raster_arr[high] < raster_arr[med]:
            swap(raster_arr, med, high )

        swap(raster_arr, med, high-1)
        pivot= raster_arr[high-1]
        i = low
        j = high - 1
        while (1):
            i+=1
            while (raster_arr[i] < pivot):
                i+=1
            j-=1
            while (pivot < raster_arr[j]):
                j-=1
            if (i < j):
                swap(raster_arr, i, j)
            else:
                break

        swap(raster_arr, i, high - 1)
        quicksort(raster_arr, low, i - 1)
        quicksort(raster_arr, i + 1, high)'''c
        
def count_sort(arr):
    max_element = int(max(arr))
    min_element = int(min(arr))
    range_of_elements = max_element - min_element + 1
    # Create a count array to store count of individual
    # elements and initialize count array as 0
    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(arr))]
 
    # Store count of each character
    for i in range(0, len(arr)):
        count_arr[arr[i]-min_element] += 1
 
    # Change count_arr[i] so that count_arr[i] now contains actual
    # position of this element in output array
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]
 
    # Build the output character array
    for i in range(len(arr)-1, -1, -1):
        output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
        count_arr[arr[i] - min_element] -= 1
 
    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(0, len(arr)):
        arr[i] = output_arr[i]
 
    return arr
        
def raster(n,m,array):
    for i in range(n):
        aux=readln()
        for i in aux:
            array+=[int(i)]
    stdout.write("RASTER GUARDADO\n")
    
def amp(array):
    print(str(array[len(array)-1]-array[0]))

def percentil(array,N):
    aux=readln()
    count=0
    for i in range(N):
        soma=0
        for k in array:
                if(k>=int(aux[count])):
                    break
                soma+=1
        stdout.write(str(math.floor((soma/len(array))*100)))
        if i !=N-1:
            stdout.write(" ")
        count+=1
    stdout.write("\n")
def mediana(array):
    if(len(array)%2!=0):
        print(array[math.floor(len(array)/2)])
    else:
        valorm=int(len(array)/2)
        print(int((array[valorm-1]+array[valorm])/2))
        
        
def main():
    user_in = [""]
    array=[]
    try:
            while(user_in[0] != "TCHAU"):
                user_in = readln()
                if user_in[0] == "RASTER":
                      raster(int(user_in[1]), int(user_in[2]),array)
                      count_sort(array)
                      
                if user_in[0] == "PERCENTIL":
                    percentil(array,int(user_in[1]))
                if user_in[0] == "AMPLITUDE":
                    amp(array)
                if user_in[0]=="MEDIANA":
                    mediana(array)
    
                  
    except EOFError:
        pass   

# Python program to
# count smaller or equal
# elements in sorted array.

# A binary search function.
# It returns
# number of elements
# less than of equal
# to given key
def binarySearchCount(arr, n, key):

	left = 0
	right = n

	mid = 0
	while (left < right):
	
		mid = (right + left)//2

		# Check if key is present in array
		if (arr[mid] == key):
		
			# If duplicates are
			# present it returns
			# the position of last element
			while (mid + 1<n and arr[mid + 1] == key):
				mid+= 1
			break
		

		# If key is smaller,
		# ignore right half
		elif (arr[mid] > key):
			right = mid

		# If key is greater,
		# ignore left half
		else:
			left = mid + 1
	

	# If key is not found in
	# array then it will be
	# before mid
	while (mid > -1 and arr[mid] > key):
		mid-= 1

	# Return mid + 1 because
	# of 0-based indexing
	# of array
	return mid + 1

# Driver code





lista = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]
for NUM in lista:
    print("--- Valores pra %d ---" % NUM)
    raster1 = [random.randrange(0, 10000) for _ in range(NUM)]
    perc = [random.randrange(0, 10000) for _ in range(NUM)]
    tic = time.perf_counter()
    count_sort(raster1)
    for i in range(NUM):
            math.floor((binarySearchCount(raster1,len(raster1),i)/len(raster1))*100)
    toc = time.perf_counter()
    print("--- %f seg ---" % (toc - tic))
print()
