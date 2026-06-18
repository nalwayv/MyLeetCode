public class Solution
{
    private static double MapRange(double value, double inMin, double inMax, double outMin, double outMax)
    {
        return (value - inMin) / (inMax - inMin) * (outMax - outMin) + outMin;
    }

    public float AngleClock(int hour, int minutes)
    {
        // convert hour on clock to the minute's it points to
        // 12 -> 0, 1 -> 5
        double hourToClockMinutes = hour % 12 * 5.0;

        double bigHand = minutes;
        double littleHand = hourToClockMinutes + (bigHand / 12.0);

        // map clock face to angle
        double angle = MapRange(Math.Abs(bigHand - littleHand), 0.0, 60.0, 0.0, 360.0);

        // choose smallest angle
        return (float)Math.Min(angle, 360f - angle);
    }
}

class Program
{
    private static void TestCase(Solution sol, int hour, int minutes)
    {
        float angle = sol.AngleClock(hour, minutes);
        Console.WriteLine($"Hour: {hour}, Minutes: {minutes} equals Min Angle: {angle}");
    }

    private static void Main()
    {
        Console.WriteLine("1344. Angle Between Hands of a Clock");
        
        Solution solution = new();
        
        TestCase(solution, 12, 30);
        TestCase(solution, 3, 30);
        TestCase(solution, 3, 15);
        TestCase(solution, 1, 57);
        TestCase(solution, 2, 35);
    }
}