import java.util.Random;

public class Quicksort {

    public String is_sorted(int[] arrayToCheck) {
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

    public void swap(int indexA, int indexB, int[] array) {
        int swap = indexA;
        array[indexA] = array[indexB];
        array[indexB] = swap;
    }

    public void medianOfThree(int start, int mid, int end, int[] array) {
        int a = array[start], b = array[mid], c = array[end];
        if ((b <= a && a <= c) || (c <= a && a <= b)) {
            swap(a, c, array);
        } else if ((a <= b && b <= c) || (c <= b && b <= a)) {
            swap(b, c, array);
        }
    }

    public void quicksort(int[] array, String option) {
        
        int pivot = array.length - 1;

        int start = 0,
            sorted = array.length - 2,
            current = 0;
        
        quicksort(pivot, start, sorted, current, array);
        
    } // end quicksort
        // quicksort helper
        private void quicksort(int pivot, int start, int sorted, int current, int[] array) {

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
           
           // quicksort low section then high section
           if (sorted > start) {
              quicksort(sorted, start, sorted - 1, start, array);
           }
           if (current < pivot) {
              quicksort(pivot, current, pivot - 1, current, array);
           }
        } // end quicksort helper

    public static void main(String[] args) throws Exception {
        Quicksort sorter = new Quicksort();
        Random randomNumbers = new Random();
        final int NUMBER_OF_ELEMENTS = 150000;
        long timeInMillis;
        double elapsedTime;
        String sorted;


        int[] arr = new int[NUMBER_OF_ELEMENTS];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = randomNumbers.nextInt(NUMBER_OF_ELEMENTS);
        }
        timeInMillis = System.currentTimeMillis();
        sorter.quicksort(arr, "median");
        elapsedTime = ((System.currentTimeMillis() - timeInMillis)/1000.00);

        sorted = sorter.is_sorted(arr);
        System.out.println(sorted + "\n" + "Sort time: " + elapsedTime);

    }
}