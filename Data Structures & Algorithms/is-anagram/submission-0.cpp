class Solution {
public:
// racecar  carrace
// chars {raecar}
// arrace
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }
        map<char, int> char_count_s;
        for (int i = 0; i < s.length(); ++i) {
            char curr_char = s[i];
            char_count_s[curr_char]++;
        }

        map<char, int> char_count_t;
        for (int i = 0; i < t.length(); ++i) {
            char curr_char = t[i];
            char_count_t[curr_char]++;
        }

        for (auto pair : char_count_s) {
            if (char_count_t[pair.first] != pair.second) {
                return false;
            }
        }
        return true;

    }
};
