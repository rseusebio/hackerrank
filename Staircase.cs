using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;

namespace HackerRank
{
    public class Staircase
    {
        public static void Main(String[] args)
        {
            int size = Convert.ToInt32(Console.ReadLine());
            staircase(size);
        }
        public static void staircase(int size)
        {
            TextWriter writer = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);
            for (int i = 0; i < size; i++)
            {
                string line = String.Empty;
                // quantity of hash characters
                int hashQnt = (i + 1);
                // quantity of white characters
                int whiteQnt = size - hashQnt;
                for (int j = 0; j < whiteQnt; j++)
                {
                    line += " ";
                }
                for (int j = 0; j < hashQnt; j++)
                {
                    line += "#";
                }
                writer.WriteLine(line);
                writer.Flush();
            }
            writer.Close();
        }
    }
}