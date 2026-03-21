class Solution {
    record Values(int value, int x, int y) {
        public Values(int value, int x, int y) {
            this.value = value;
            this.x = x;
            this.y = y;
        }
    }

    public int[][] reverseSubMatrix(int[][] grid, int x, int y, int k)
    {
        int endRow = Math.min(x + k, grid.length);
        int endCol = Math.min(y + k, grid[0].length);
        ArrayList<Values> values = new ArrayList<>();

        int row = x;
        for (int r = endRow - 1; r >= x; r--) {
            for (int c = y; c < endCol; c++) {
                values.add(new Values(grid[r][c], row, c));
            }
            row++;
        }

        for(Values pair : values) {
            grid[pair.x][pair.y] = pair.value;
        }

        return grid;
    }
}