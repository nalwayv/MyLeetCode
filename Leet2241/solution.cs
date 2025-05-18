namespace Leet2241;

public class ATM
{
    private readonly int[] _notes = [20, 50, 100, 200, 500];
    private readonly Dictionary<int, int> _banknotesCount = new()
    {
        {20, 0},
        {50, 0},
        {100, 0},
        {200, 0},
        {500, 0},
    };

    public ATM()
    {
    }

    public void Deposit(int[] banknotesCount)
    {
        for (int i = 0; i < banknotesCount.Length; i++)
        {
            if (i < _notes.Length)
            {
                _banknotesCount[_notes[i]] += banknotesCount[i];
            }
        }
    }

    public int[] Withdraw(int amount)
    {
        Dictionary<int, int> withdrawNotes = [];
        for (int i = _notes.Length - 1; i >= 0; i--)
        {
            int note = _notes[i];
            if (amount >= note && _banknotesCount.TryGetValue(note, out int count) && count > 0)
            {
                withdrawNotes[note] = Math.Min(count, amount / note);
                amount -= note * withdrawNotes[note];
            }
        }

        if (amount == 0)
        {
            foreach (var (key, value) in withdrawNotes)
            {
                _banknotesCount[key] -= value;
            }

            int[] result = new int[_notes.Length];
            for (int i = 0; i < _notes.Length; i++)
            {
                if (withdrawNotes.TryGetValue(_notes[i], out int count))
                {
                    result[i] = count;
                }
            }
            return result;
        }

        return [-1];
    }
}

class Program
{
    private static void PrintResult(int[] arr)
    {
        Console.Write("notes: [");
        foreach (var item in arr)
        {
            Console.Write($" {item} ");
        }
        Console.WriteLine("]");
    }

    static void Main(string[] args)
    {
        Console.WriteLine("2241. Design an ATM Machine");
        ATM atm = new();
        atm.Deposit([0, 0, 1, 2, 1]);
        PrintResult(atm.Withdraw(600));
        atm.Deposit([0, 1, 0, 1, 1]);
        PrintResult(atm.Withdraw(600));
        PrintResult(atm.Withdraw(550));
    }
}