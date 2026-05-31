public class Solution
{
    public bool AsteroidsDestroyed(int mass, int[] asteroids)
    {
        Array.Sort(asteroids);

        int count = 0;
        long lMass = mass;

        foreach (var asteroid in asteroids)
        {
            if (asteroid > lMass)
            {
                break;
            }

            lMass += asteroid;

            count++;
        }

        return count == asteroids.Length;
    }
}