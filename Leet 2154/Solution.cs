Console.WriteLine("2154. Keep Multiplying Found Values by Two");


int FindFinalValue(int[] nums, int original)
{
    var set = new HashSet<int>(nums);

    while (set.Contains(original))
    {
        original *= 2;
    }

    return original;
}


int[] nums = [1,3,5,6,12];
int original = 3;
Console.WriteLine(FindFinalValue(nums, original));
