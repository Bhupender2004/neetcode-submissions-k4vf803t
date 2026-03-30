class Solution {
    public void setZeroes(int[][] matrix) {
        int rows = matrix.length, cols = matrix[0].length;
        int [][] mark = new int[rows][cols];
        for(int i=0; i<rows; i++){
            System.arraycopy(matrix[i], 0, mark[i], 0, cols);
        }
        for(int i=0; i<rows; i++){
            for(int j=0; j<cols; j++){
                if(matrix[i][j]==0){
                    for(int col=0; col<cols; col++){
                        mark[i][col]=0;
                    }
                    for(int row=0; row<rows; row++){
                        mark[row][j]=0;
                    }
                }
            }
        }
        for(int i=0; i<rows; i++){
            System.arraycopy(mark[i],0,matrix[i],0,cols);
        }
    }
}
