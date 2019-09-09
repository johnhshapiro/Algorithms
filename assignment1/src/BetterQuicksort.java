import java.util.*;

public class BetterQuicksort {

    final int NUMBER_OF_ELEMENTS = 500000;
    final int TIMES_TO_RUN = 500;
    final int INSERTION_SIZE = 400;
    Random randomNumbers = new Random();
    int[] array = new int[NUMBER_OF_ELEMENTS];

    public static void main(String[] args) throws Exception {
        BetterQuicksort sorter = new BetterQuicksort();

        sorter.multipleSorts("");
        
    }

    public void printArray(int[] array) {
        System.out.print("[ ");
        for (int i = 0; i < array.length - 1; i++) {
            System.out.print(array[i] + ", ");
        }
        System.out.println(array[array.length - 1] + " ]");
    }

    public long sort(String option) {
        long timeInMillis;
        long elapsedTime;
        String sorted;

        for (int i = 0; i < NUMBER_OF_ELEMENTS; i++) {
            array[i] = randomNumbers.nextInt(NUMBER_OF_ELEMENTS);
        }

        timeInMillis = System.currentTimeMillis();
        quicksort(array, option);
        elapsedTime = System.currentTimeMillis() - timeInMillis;
        sorted = isSorted(array);        
        if (sorted != "Sort Successful") {
            System.out.println("you're dead to me");
        }
        return elapsedTime;
    }
    public Double multipleSorts(String option) {
        long totalTime = 0;
        double averageTime = 0;
        for (int i = 0; i < TIMES_TO_RUN; i++) {
            totalTime += sort(option);
        }
        averageTime = (totalTime/TIMES_TO_RUN)/1000.000;
        System.out.println("Optimization: " + option);
        System.out.println("     # Times ran: " + TIMES_TO_RUN);
        System.out.println("    Average Time: " + averageTime);
        return averageTime;
    }

    public void swap(int indexA, int indexB, int[] array) {
        int swap = array[indexA];
        array[indexA] = array[indexB];
        array[indexB] = swap;
    }

    public void medianOfThree(int start, int mid, int end, int[] array) {
        int a = array[start], b = array[mid], c = array[end];
        if ((b <= a && a <= c) || (c <= a && a <= b)) {
            swap(start, end, array);
        } else if ((a <= b && b <= c) || (c <= b && b <= a)) {
            swap(mid, end, array);
        }
    }

    public String isSorted(int[] arrayToCheck) {
        String sorted = "Sort Successful";
        int i = 0;
            while (sorted == "Sort Successful" && i < arrayToCheck.length - 1) {
                if (arrayToCheck[ i ] > arrayToCheck[ i + 1 ]) {
                    sorted = "Sort failed";
                }
                i++;
            }
        return sorted;
    }

    public void quicksort(int[] array, String option) {
        
        int pivot, start, sorted, current, left, swap, index, right;
        pivot = start = sorted = current = left = swap = index = right = 0;

        if (option == "lomuto") {
            left = pivot = swap = 0; pivot = 0;
            index = 1;
            right = array.length - 1;
            quicksortLomuto(left, pivot, swap, index, right, array);
        }
        else {
            pivot = array.length -1;
            start = current = 0;
            sorted = array.length -2;

            if (option == "median") {
                medianOfThree(0, array.length / 2, array.length - 1, array);
                quicksortMedian(pivot, start, sorted, current, array);
            } else if (option == "insertion") {
                quicksortInsertion(pivot, start, sorted, current, array);
            } else {
                quicksortClassic(pivot, start, sorted, current, array);
            }
        }
        
    }
        private void quicksortClassic(int pivot, int start, int sorted, int current, int[] array) {

            while (current < sorted) {
                if (array[sorted] <= array[pivot] && array[pivot] <= array[current]) {
                    swap(current, sorted, array);
                    current++;
                    sorted--;
                } else if (array[sorted] <= array[pivot] && array[current] <= array[pivot]) {
                    current++;
                } else if (array[pivot] <= array[sorted] && array[pivot] <= array[current]) {
                    sorted--;
                } else {
                    current++;
                    sorted--;
                }
            }
            if (sorted < current || (sorted == current && array[pivot] < array[current])) {
                swap(current, pivot, array);
                current++;
            } else if (array[pivot] >= array[current]) {
                swap(current + 1, pivot, array);
                current++;
            } 
            if (sorted > start) {
                quicksortClassic(sorted, start, sorted - 1, start, array);
            }
            if (current < pivot) {
                quicksortClassic(pivot, current, pivot - 1, current, array);
            }
        }
    
        private void quicksortInsertion(int pivot, int start, int sorted, int current, int[] array) {

            if (pivot - start <= INSERTION_SIZE) {
                insertionSort(start, pivot, array);
            } else {
                while (current != sorted && current < sorted) {
                    if (array[sorted] <= array[pivot] && array[pivot] <= array[current]) {
                        swap(current, sorted, array);
                        current++;
                        sorted--;
                    } else if (array[sorted] <= array[pivot] && array[current] <= array[pivot]) {
                        current++;
                    } else if (array[pivot] <= array[sorted] && array[pivot] <= array[current]) {
                        sorted--;
                    } else {
                        current++;
                        sorted--;
                    }
                }
                if (sorted < current || (sorted == current && array[pivot] < array[current])) {
                    swap(current, pivot, array);
                    current++;
                } else if (array[pivot] >= array[current]) {
                    swap(current + 1, pivot, array);
                    current++;
                } 
                if (sorted > start) {
                    quicksortInsertion(sorted, start, sorted - 1, start, array);
                }
                if (current < pivot) {
                    quicksortInsertion(pivot, current, pivot - 1, current, array);
                }
            }
        }

        private void quicksortMedian(int pivot, int start, int sorted, int current, int[] array) {

            medianOfThree(start, (start + pivot)/2, pivot, array);
            while (current != sorted && current < sorted) {
                if (array[sorted] <= array[pivot] && array[pivot] <= array[current]) {
                    swap(current, sorted, array);
                    current++;
                    sorted--;
                } else if (array[sorted] <= array[pivot] && array[current] <= array[pivot]) {
                    current++;
                } else if (array[pivot] <= array[sorted] && array[pivot] <= array[current]) {
                    sorted--;
                } else {
                    current++;
                    sorted--;
                }
            }
            if (sorted < current || (sorted == current && array[pivot] < array[current])) {
                swap(current, pivot, array);
                current++;
            } else if (array[pivot] >= array[current]) {
                swap(current + 1, pivot, array);
                current++;
            } 
            if (sorted > start) {
                quicksortMedian(sorted, start, sorted - 1, start, array);
            }
            if (current < pivot) {
                quicksortMedian(pivot, current, pivot - 1, current, array);
            }

        }

        private void quicksortLomuto(int left, int pivot, int swap, int index, int right, int[] array) {

            while (index <= right) {
                if (array[pivot] <= array[index]) {
                    index++;
                } else if (array[pivot] > array[index]) {
                    swap++;
                    swap(swap, index, array);
                    index++;
                }
            }
            swap(swap, pivot, array);

            if (swap > left) {
                quicksortLomuto(left, left, left, left + 1, swap - 1, array);
            }
            if (swap + 1 < right) {
                quicksortLomuto(swap + 1, swap + 1, swap + 1, swap + 2, right, array);
            }


        } // end quicksort helper
    
        // adapted from https://rosettacode.org/wiki/Sorting_algorithms/Insertion_sort#Java
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

}