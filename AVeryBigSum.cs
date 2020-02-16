using System;
using System.Collections;
using System.IO;
using System.Linq;
using System.Collections.Generic;

namespace HackerRank
{
    public class HackerRankMethods
    {
        public static void Main(String[] args)
        {
            aVeryBigSum();
        }

        public static void aVeryBigSum()
        {
            int qnt = Convert.ToInt32(Console.ReadLine());
            List<string> values = Console.ReadLine().Split(' ').ToList();
            long sum = 0;
            for (int i = 0; i < qnt; i++)
            {
                long v = Convert.ToInt64(values[i]);
                sum += v;
            }
            TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);
            textWriter.WriteLine(sum);
            textWriter.Flush();
            textWriter.Close();
        }
    }
}