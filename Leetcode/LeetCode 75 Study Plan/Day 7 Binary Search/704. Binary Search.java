class Solution {
    public int search(int[] nums, int target) {
        int n=nums.length-1;
        return binarySearch(nums,0,n,target);
    }
    public static int binarySearch(int arr[], int l, int r, int x)
    {
        if (l<=r) {
            int mid = l + (r - l) / 2;
            if (arr[mid] == x)
                return mid;
            if (arr[mid] > x)
                return binarySearch(arr, l, mid - 1, x);
            return binarySearch(arr, mid + 1, r, x);
        }
 
        return -1;
    }
}