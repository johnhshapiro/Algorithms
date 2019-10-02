/* 
Authors: John Shapiro with methods adapted from
https://www.geeksforgeeks.org/hoares-vs-lomuto-partition-scheme-quicksort/

This program runs quick sort on arrays, allowing for customization of
    number of elements, times to run, and the point at which to run
    insertion sort size.
    The program then prints a report of the relevant data.
*/

import java.util.*;

class GFG 
{ 
    static final int NUMBER_OF_ELEMENTS = 1000;
    static final int TIMES_TO_RUN = 1;
    static final int INSERTION_SORT_SIZE = 11;
    static Random randomNumbers = new Random();

    
    public void Swap(int[] array, int position1, int position2) {
        // Swaps elements in an array

        // Copy the first position's element
        int temp = array[position1];

        // Assign to the second element
        array[position1] = array[position2];

        // Assign to the first element
        array[position2] = temp;
    } // swap

    /*
    This function takes last element as pivot, places the pivot element
    at its correct position in sorted array, and places all smaller (smaller
    than pivot) to left of pivot and all greater elements to right of pivot
    Adapted from
    https://www.geeksforgeeks.org/hoares-vs-lomuto-partition-scheme-quicksort/
     */
    public int lomutoPartition(int[] arr, int low, int high) {
        int pivot = arr[high];

        // Index of smaller element
        int i = (low - 1);

        for (int j = low; j <= high - 1; j++) {
            // If current element is smaller
            // than or equal to pivot
            if (arr[j] <= pivot) {
                i++; // increment index of
                     // smaller element
                Swap(arr, i, j);
            }
        }
        Swap(arr, i + 1, high);
        return (i + 1);
    } // lomutoPartition

    /* Takes an array, and high and low indexes of a partition of the array
    Adapted from
    https://www.geeksforgeeks.org/hoares-vs-lomuto-partition-scheme-quicksort/
    */
    public int hoarePartition(int[] arr, int low, int high) {
        int pivot = arr[low];
        int i = low - 1, j = high + 1;

        while (true) {
            // Find leftmost element greater
            // than or equal to pivot
            do {
                i++;
            } while (arr[i] < pivot);

            // Find rightmost element smaller
            // than or equal to pivot
            do {
                j--;
            } while (arr[j] > pivot);

            // If two pointers met.
            if (i >= j)
                return j;
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            // swap(arr[i], arr[j]);
        }
    } // end hoarePartition

    /* Lomuto quicksort takes an array, the high and low indexes of a
        partition, and the optimization type */
    public void lomutoQuickSort(int[] arr, int low, int high, String optimization) {
        if (optimization == "insertion" && high - low <= INSERTION_SORT_SIZE) {
            // don't sort that part
        }
        else if (low < high) {
            /*
             * pi is partitioning index, arr[p] is now at right place
             */
            int pi = lomutoPartition(arr, low, high);

            // Separately sort elements before
            // partition and after partition
            lomutoQuickSort(arr, low, pi - 1, optimization);
            lomutoQuickSort(arr, pi + 1, high, optimization);
        }
    }

    /* Recursive hoareQuicksort, takes an array, the high and low indexes of a
        partition, and the optimization type */
    public void hoareQuickSort(int[] arr, int low, int high, String optimization) {
        if (optimization == "insertion" && high - low <= INSERTION_SORT_SIZE) {
            // don't sort that part
        }
        else if (low < high) {
            /*
             * pi is partitioning index, arr[p] is now at right place
             */
            int pi = hoarePartition(arr, low, high);

            // Separately sort elements before
            // partition and after partition
            hoareQuickSort(arr, low, pi, optimization);
            hoareQuickSort(arr, pi + 1, high, optimization);
        }
    } // hoareQuickSort

    /* Function to print an array. Takes array and size of array */
    public void printArray(int[] arr, int size) {
        int i;
        for (i = 0; i < size; i++)
            System.out.print(" " + arr[i]);
        System.out.println();
    }

    /* Function checks if an array is sorted. Takes an array */
    public Boolean isSorted(int[] arrayToCheck) {
        Boolean sorted = true;
        int i = 0;
        while (true && i < arrayToCheck.length - 1) {
            if (arrayToCheck[i] > arrayToCheck[i + 1]) {
                sorted = false;
            }
            i++;
        }
        return sorted;
    } // isSorted

    /* Find the median of three values. takes the starting, middle, and
        final index of an array partion, and the array. */
    public void medianOfThree(int start, int mid, int end, int[] array) {
        int a = array[start], b = array[mid], c = array[end];
        if ((b <= a && a <= c) || (c <= a && a <= b)) {
            swap(start, end, array);
        } else if ((a <= b && b <= c) || (c <= b && b <= a)) {
            swap(mid, end, array);
        }
    } // medianOfThree

    /* Swaps two values of an array given their indicies. Takes the indicies
        and the array. */
    public void swap(int indexA, int indexB, int[] array) {
        int swap = array[indexA];
        array[indexA] = array[indexB];
        array[indexB] = swap;
    }

    /* Creates an array of random values, calls a sort, and returns
        the sort time (long). Takes the partition type and optimization type
        */
    public long sort(String partition , String optimization) {
        long timeInMillis;
        long elapsedTime;
        int n = NUMBER_OF_ELEMENTS;
        int array[] = new int[NUMBER_OF_ELEMENTS];
        fillRandomArray(array);

        timeInMillis = System.currentTimeMillis();
        if (optimization == "median") {
            medianOfThree(0, n/2, n - 1, array);
        }
        if (partition == "lomuto") {
            lomutoQuickSort(array, 0, n - 1, optimization);
        }
        if (partition == "hoare") {
            hoareQuickSort(array, 0, n - 1, optimization);
        }
        if (optimization == "insertion") {
            insertionSort(0, n - 1, array);
        }
        elapsedTime = System.currentTimeMillis() - timeInMillis;
        isSorted(array);
        if (!isSorted(array)) {
            System.out.println("you've brought shame upon your family");
        }
        return elapsedTime;
    } // sort

    /* Calls sort multiple times and prints average time, partition,
        and optimizatinon type of sort */
    public void multipleSorts(String partition, String optimization) {
        long totalTime = 0;
        double averageTime = 0;

        for (int i = 0; i < TIMES_TO_RUN; i++) {
            totalTime += sort(partition, optimization);
        }
        averageTime = (totalTime/TIMES_TO_RUN)/1000.000;
        System.out.println("Partition Type: " + partition);
        System.out.println("  Optimization: " + optimization);
        if (optimization == "insertion") {
            System.out.println("Insertion At <= " + INSERTION_SORT_SIZE);
        }
        System.out.println("          # Elements: " + NUMBER_OF_ELEMENTS);
        System.out.println("         # Times ran: " + TIMES_TO_RUN);
        System.out.println("        Average Time: " + averageTime);
    } // multiple sorts

    /* Fill an array with random integers */
    public void fillRandomArray(int[] array) {
        for (int i = 0; i < NUMBER_OF_ELEMENTS; i++) {
            array[i] = i;
        }
    }  // fillRandomArray

    /* adapted from
    https://rosettacode.org/wiki/Sorting_algorithms/Insertion_sort#Java */
    public void insertionSort(int start, int end, int[] array){
        for(int i = start + 1; i <= end; i++){
            int value = array[i];
            int j = i - 1;
            while(j >= 0 && array[j] > value){
                array[j + 1] = array[j];
                j = j - 1;
            }
            array[j + 1] = value;
        }
    }

    // Driver Code
    static public void main(String[] args) {

        GFG sorter = new GFG();
        sorter.multipleSorts("hoare", "none");
        // sorter.multipleSorts("hoare", "median");
        // sorter.multipleSorts("hoare", "insertion");
        // sorter.multipleSorts("lomuto", "none");
        // sorter.multipleSorts("lomuto", "median");
        // sorter.multipleSorts("lomuto", "insertion");
    }
} 