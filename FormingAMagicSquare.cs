using System;
using System.Collections;
using System.Collections.Generic;



namespace HackerRank
{
    public class MatrixUtils
    {

        public static dynamic SumAColumn(List<List<dynamic>> matrix, int colIndex)
        {
            dynamic sum = 0;
            matrix.ForEach((List<dynamic> row) =>
            {
                if (colIndex < 0 || colIndex >= row.Count)
                {
                    throw new Exception("column index out of range.");
                }
                sum += row[colIndex];
            });
            return sum;
        }

        public static dynamic SumARow(List<List<dynamic>> matrix, int rowIndex)
        {
            dynamic sum = 0;
            if (rowIndex < 0 || rowIndex >= matrix.Count)
            {
                throw new Exception("row index out of range.");
            }
            matrix[rowIndex].ForEach((dynamic value) =>
            {
                sum += value;
            });
            return sum;
        }

        public static dynamic SumADiagonal(List<List<dynamic>> matrix, bool isMain)
        {
            // Checking if matrix is an square matrix
            int rowsQnt = matrix.Count;
            matrix.ForEach((List<dynamic> col) =>
            {
                if (col.Count != rowsQnt)
                {
                    throw new Exception("matrix must be an square matrix.");
                }
            });

            int index = isMain ? 0 : rowsQnt - 1;

            dynamic sum = 0;
            matrix.ForEach((List<dynamic> col) =>
            {
                sum += col[index];
                if (isMain)
                {
                    index++;
                }
                else
                {
                    index--;
                }
            });
            return sum;
        }

        public static void Main(String[] args)
        {
            List<List<dynamic>> matrix = new List<List<dynamic>>{
                new List<dynamic>{5, 3, 4},
                new List<dynamic>{1, 5, 8},
                new List<dynamic>{6, 4, 2}
            };
            Console.WriteLine(SumAColumn(matrix, 0));
            Console.WriteLine(SumAColumn(matrix, 1));
            Console.WriteLine(SumAColumn(matrix, 2));
            Console.WriteLine(SumARow(matrix, 0));
            Console.WriteLine(SumARow(matrix, 1));
            Console.WriteLine(SumARow(matrix, 2));
            Console.WriteLine(SumADiagonal(matrix, true));
            Console.WriteLine(SumADiagonal(matrix, false));
        }
    }
}