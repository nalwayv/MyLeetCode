class Solutuion
{
    bool Equals(int[][] a, int[][] b)
    {
        if (a.Length != b.Length)
        {
            return false;
        }

        for (int i = 0; i < a.Length; i++)
        {
            if (a[i].Length != b[i].Length)
            {
                return false;
            }

            for (int j = 0; j < a[i].Length; j++)
            {
                if (a[i][j] != b[i][j])
                {
                    return false;
                }
            }
        }

        return true;
    }

    int[][] Rotate(int[][] mat)
    {
        int rows = mat.Length;
        int cols = mat[0].Length;

        int[][] rotated = new int[cols][];
        for (int i = 0; i < cols; i++)
        {
            rotated[i] = new int[rows];
        }

        for (int r = 0; r < rows; r++)
        {
            for (int c = 0; c < cols; c++)
            {
                rotated[c][rows - r - 1] = mat[r][c];
            }
        }

        return rotated;
    }

    public bool FindRotation(int[][] mat, int[][] target)
    {
        for (int i = 0; i < 4; i++)
        {
            mat = Rotate(mat);
            if (Equals(mat, target))
            {
                return true;
            }
        }

        return false;
    }
}