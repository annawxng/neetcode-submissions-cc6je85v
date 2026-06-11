class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
            vector<unordered_set<char>> row_set(9);
    vector<unordered_set<char>> col_set(9);
    vector<unordered_set<char>> box_set(9);

    int rows = board.size();
    int cols = board[0].size();
    
    for (int r = 0; r < rows; ++r) {
        for (int c = 0; c < cols; ++c) {
            char curr = board[r][c];
            if (curr == '.') {
                continue;
            }
            int box_row = (r / 3);
            int box_col = (c / 3);
            int box_cols = 3;
            int box_idx = box_row * box_cols + box_col;
            
            
            if (row_set[r].find(curr) != row_set[r].end() || col_set[c].find(curr) != col_set[c].end() || box_set[box_idx].find(curr) != box_set[box_idx].end()) {
                return false;
            }
            row_set[r].insert(curr);
            col_set[c].insert(curr);
            box_set[box_idx].insert(curr);
        }
    }
    return true;
    
    }
};
