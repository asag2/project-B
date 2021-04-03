using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace opdrachten{
    class Program{
        static void Main(){
				Console.WriteLine("         Voorgerechten:");
				string[] VGDishes = { "1.Sashimi tonijn ", "2.Carpaccio ", "3.Huzarensalade", "4.Soep " };
				List<string> VGDishList = new List<string>();
				VGDishList.AddRange(VGDishes);
				foreach (string a in VGDishList)
				Console.WriteLine(a);

				Console.WriteLine("\n         Tussengerechten:");
				string[] TGDishes = { "5.Pasta", "6.Eendenborst " };
				List<string> TGDishList = new List<string>();
				TGDishList.AddRange(TGDishes);
				foreach (string a in TGDishList)
					Console.WriteLine(a);

				Console.WriteLine("\n         Hoofdgerechten:");
				string[] HGDishes = { "7.Biefstuk met knoflookaardappeltjes", "8.Vis van de dag ", "9.Kibbeling", "10.Lasagne" };
				List<string> HGDishList = new List<string>();
				HGDishList.AddRange(HGDishes);
				foreach (string a in HGDishList)
					Console.WriteLine(a);

				Console.WriteLine("\n         Nagerechten:");
				string[] NGDishes = { "11.Panna Cotta", "12.Bitterkoekjes", "13.Kaasplateau" };
				List<string> NGDishList = new List<string>();
				NGDishList.AddRange(NGDishes);
				foreach (string a in NGDishList)
					Console.WriteLine(a);

				Console.WriteLine("\n         Drinken:");
				string[] Drinken = { "14.Frisdrank/Soda", "15.Wijn", "17.Beer" };
				List<string> DrankList = new List<string>();
				DrankList.AddRange(Drinken);
				foreach (string a in DrankList)
					Console.WriteLine(a);
				//choose number
				Console.WriteLine("\nPlease click the number before the dish to get more details\n");
				string Dish2 = Console.ReadLine();
				int dish = Int32.Parse(Dish2);

				if (dish == 1)
				{
					Console.WriteLine("sambai vinaigrette, sojaboontjes, sesam mayonaise, gepofte wilde rijst \n" +
						"€ 12,50");
				}
				else if (dish == 2)
				{
					Console.WriteLine("Hollands rund-truffel vinaigrette, oude kaas, rucola\n" +
						"(€12,50)");
				}
				else if (dish == 3)
				{
					Console.WriteLine("U get whatever u want!!!!!3");
				}
				else if (dish == 4)
				{
					Console.WriteLine("U get whatever u want!!!!!4");
				}
				else if (dish == 5)
				{
					Console.WriteLine("U get whatever u want!!!!!5");
				}
				else if (dish == 6)
				{
					Console.WriteLine("U get whatever u want!!!!!6");
				}
				else if (dish == 7)
				{
					Console.WriteLine("U get whatever u want!!!!!7");
				}
				else if (dish == 8)
				{
					Console.WriteLine("U get whatever u want!!!!!8");
				}
				else if (dish == 9)
				{
					Console.WriteLine("U get whatever u want!!!!!9");
				}
				else if (dish == 10)
				{
					Console.WriteLine("U get whatever u want!!!!!10");
				}
				else if (dish == 11)
				{
					Console.WriteLine("U get whatever u want!!!!!11");
				}
				else if (dish == 12)
				{
					Console.WriteLine("U get whatever u want!!!!!12");
				}
				else if (dish == 13)
				{
					Console.WriteLine("U get whatever u want!!!!!13");
				}
				else if (dish == 14)
				{
					Console.WriteLine("U get whatever u want!!!!!14");
				}
				else if (dish == 15)
				{
					Console.WriteLine("U get whatever u want!!!!!15");
				}
				else if (dish == 16)
				{
					Console.WriteLine("U get whatever u want!!!!!16");
				}
				else if (dish == 17)
				{
					Console.WriteLine("U get whatever u want!!!!!17");
				}
				else{
					Console.WriteLine("The is no such dish, please choose another dish!!!");
				}
			}

		}
	}

