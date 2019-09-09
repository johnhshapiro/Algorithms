import java.util.*;

public class BetterQuicksort {

    final int NUMBER_OF_ELEMENTS = 500000;
    final int TIMES_TO_RUN = 500;
    final int INSERTION_SIZE = 400;
    Random randomNumbers = new Random();
    int[] array = new int[NUMBER_OF_ELEMENTS];

    public static void main(String[] args) throws Exception {
        BetterQuicksort sorter = new BetterQuicksort();

        sorter.multipleSorts("median");
        
        //sorter.sort("");


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
        
        if (option == "median") {
            medianOfThree(0, array.length / 2, array.length - 1, array);
        }

        int pivot = array.length - 1;
        int start = 0,
            sorted = array.length - 2,
            current = 0;
        
        quicksort(pivot, start, sorted, current, array, option);
        
    } // end quicksort
        // quicksort helper
        private void quicksort(int pivot, int start, int sorted, int current, int[] array, String option) {

            if (option == "insertion" && pivot - start <= INSERTION_SIZE) {
                insertionSort(start, pivot, array);
            } else {
                if (option == "median") {
                    medianOfThree(start, (start + pivot)/2, pivot, array);
                }
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
                    quicksort(sorted, start, sorted - 1, start, array, option);
                }
                if (current < pivot) {
                    quicksort(pivot, current, pivot - 1, current, array, option);
                }
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