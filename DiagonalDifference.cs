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
            int qnt = Convert.ToInt32(Console.ReadLine());
            List<List<int>> matrix = new List<List<int>>();
            for (int i = 0; i < qnt; i++)
            {
                var list = Array.ConvertAll(Console.ReadLine().Trim().Split(' '), value => Convert.ToInt32(value)).ToList();
                matrix.Add(list);
            }
            TextWriter writer = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

            writer.WriteLine(diagonalDifference(matrix));
            writer.Flush();
            writer.Close();
        }

        public static int diagonalDifference(List<List<int>> matrix)
        {
            int mainDiagonal = 0;
            int secondaryDiagonal = 0;
            int mainIndex = 0;
            int secondaryIndex = matrix.Count - 1;
            matrix.ForEach((List<int> row) =>
            {
                mainDiagonal += row[mainIndex++];
                secondaryDiagonal += row[secondaryIndex--];
            });
            int result = Math.Abs(mainDiagonal - secondaryDiagonal);
            return result;
        }
    }
}