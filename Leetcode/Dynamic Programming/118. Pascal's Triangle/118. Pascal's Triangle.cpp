class Solution {
public:
    vector<vector<int>> generate(int numRows) {
            vector<vector<int>> vec(numRows,vector<int>(numRows));
            for(int i=0;i<numRows;i++){
                vec[i][0]=1;
             }
            for(int i=0;i<numRows;i++){
                    vec[i][i]=1;
            }
            
            for(int i=2;i<numRows;i++){
                for(int j=1;j<i;j++){
                    vec[i][j]=vec[i-1][j-1]+vec[i-1][j];
                }
            }
            // Remove initial zero values from the vector
            for (int i = 0; i < vec.size(); i++) {
                vec[i].erase(std::remove(vec[i].begin(), vec[i].end(), 0), vec[i].end());
            }
            return vec;
    }
};