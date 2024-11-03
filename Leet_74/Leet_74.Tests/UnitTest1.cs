namespace Leet_74.Tests;

public class Tests
{
    private readonly Solution _solution = new Solution();

    [SetUp]
    public void Setup()
    {
    }

    [Test]
    public void Test1_SearchMatrixShouldPass()
    {
        int[][] matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]];
        int target = 20;
        bool result = _solution.SearchMatrix(matrix, target);
        Assert.That(result, Is.True);
    }
    
    [Test]
    public void Test2_SearchMatrixShouldFail()
    {
        int[][] matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]];
        int target = 61;
        bool result = _solution.SearchMatrix(matrix, target);
        Assert.That(result, Is.False);
    }
}