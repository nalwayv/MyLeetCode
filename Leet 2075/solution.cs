using System.Text;

public class Solution
{
    public string DescodeCiphertext(string encodedText, int rows, bool debug = false)
    {
        if(encodedText == "")
        {
            return "";
        }

        var cols = encodedText.Length / rows;
        char[,] matrix = new char[rows, cols];

        for(int i = 0; i < encodedText.Length; i++)
        {
            var row = i / cols;
            var col = i % cols;
            matrix[row, col] = encodedText[i];
        }

        if (debug)
        {
            for(int i = 0; i < cols; i++)
            {
                Console.Write("[ ");
                for(int j = 0; j < rows; j++)
                {
                    Console.Write($" {matrix[j, i]} ");
                }
                Console.WriteLine(" ]");
            }
        }

        StringBuilder stringBuilder = new();        
        for(int col = 0; col < cols; col++)
        {
            var k = col;
            for(int row = 0; row < rows; row++)
            {
                if (k >= cols) 
                {
                    break;
                }
                
                stringBuilder.Append(matrix[row,k]);

                k++;
            }
        }

        return stringBuilder.ToString().TrimEnd();

    }
}


class Program
{
    private static void Main()
    {
        Solution solution = new();
        var text1 = solution.DescodeCiphertext("ch   ie   pr", 3);
        Console.WriteLine($"Result: {text1} {text1.Length}");

        var text2 = solution.DescodeCiphertext("iveo    eed   l te   olc", 4);
        Console.WriteLine($"Result: {text2} {text2.Length}");
    }
}