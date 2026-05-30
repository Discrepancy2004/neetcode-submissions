class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length())
            return false;

        Map <Character,Integer> sh = new HashMap<>();
        Map <Character,Integer> th = new HashMap<>();

        for(char ch: s.toCharArray())
        {
            sh.put(ch,sh.getOrDefault(ch,0)+1);
            
        }
        for(char ch: t.toCharArray())
        {
        th.put(ch,th.getOrDefault(ch,0)+1);
        }
        if(sh.equals(th))
            return true;
        return false;

    }
}
