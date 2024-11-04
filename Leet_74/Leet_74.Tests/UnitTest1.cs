namespace Leet_74.Tests;

public class Tests
{
    private readonly Solution _solution = new Solution();
    private int[][] _matrix;
    
    [SetUp]
    public void Setup()
    {
        _matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 60]
        ];
    }

    [Test]
    public void Test1_SearchMatrixShouldPass()
    {
        int target = 3;
        bool result = _solution.SearchMatrix(_matrix, target);
        Assert.That(result, Is.True);
    }
    
    [Test]
    public void Test2_SearchMatrixShouldFail()
    {
        int target = 61;
        bool result = _solution.SearchMatrix(_matrix, target);
        Assert.That(result, Is.False);
    }
    
    
    [Test]
    public void Test3_SearchMatrixShouldFail()
    {
        int target = 13;
        bool result = _solution.SearchMatrix(_matrix, target);
        Assert.That(result, Is.False);
    }
}