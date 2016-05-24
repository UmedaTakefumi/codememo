using System;
using System.Threading.Tasks;

namespace MyProject.ParallelFor
{
    class Program
    {
        static void Main(string[] args)
        {
            // ParallelOptionsで2スレッドまでに制限
            ParallelOptions option = new ParallelOptions();
            option.MaxDegreeOfParallelism = 2;

            Parallel.For(0, 100, option, i =>
            {
                Console.Write(i + ",");
            });

            Console.ReadKey();
        }
    }
}
