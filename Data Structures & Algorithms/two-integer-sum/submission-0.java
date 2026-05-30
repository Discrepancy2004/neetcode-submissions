class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap <Integer,Integer> seen = new HashMap<>();
        int[] sum = new int[2];
        for(int i = 0;i<nums.length;i++)
        {   
            
            if(seen.containsKey(target - nums[i]))
            {
                sum[0] = seen.get(target-nums[i]);
                sum[1] = i;
                return sum;
            }
            
            seen.put(nums[i],i);
            
        }
        return sum;
    }
}
