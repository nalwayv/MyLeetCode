namespace Leet
{
    public class Solution 
    {
        public int[] DeckRevealedIncreasing(int[] deck) 
        {
            Array.Sort(deck);
            int[] index = new int[deck.Length];
            for (int j = 0; j < deck.Length; j++)
            {
                index[j] = j;
            }

            Queue<int> queue = new(index);

            int[] result = new int[deck.Length];
            for(int i = 0; i < deck.Length; i++)
            {
                result[queue.Dequeue()] = deck[i];
                if(queue.Count > 0)
                {
                    queue.Enqueue(queue.Dequeue());
                }
            }

            return result;
        }
    }

    class Program
    {

        static void PrintArray(int[] arr)
        {
            Console.Write("[");
            foreach(int num in arr)
            {
                Console.Write($" {num} ");
            }
            Console.WriteLine("]");
        }

        static void Main()
        {
            Console.WriteLine("950. Reveal Cards In Increasing Order");

            Solution solution = new();
            int[] case1 = [17,13,11,2,3,5,7];
            int[] result = solution.DeckRevealedIncreasing(case1);
            
            Console.WriteLine("Before");
            PrintArray(case1);
            Console.WriteLine("After");
            PrintArray(result);
        }    
    }
}