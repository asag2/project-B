using System;
using System.IO;
using Newtonsoft.Json;
using System.Collections.Generic;


class Mycode
{
	static void Main(string[] args)
	{
		MenuPage();
	}
	public static void MenuPage()
    {
		var json = File.ReadAllText("details.json");
		dynamic stuff = JsonConvert.DeserializeObject(json);
		foreach (var s in stuff)
			{
            Console.WriteLine(s.Number + s.Dot + s.Name );
			}
		SortingMenu();

	}
    public static void SortingMenu()
    {
		var json = File.ReadAllText("details.json");
		dynamic stuff = JsonConvert.DeserializeObject(json);

		Console.WriteLine("\nPlease press the number of the dish you want to know more information about.\n" +
			"Or press 'v' to sort for vegetarian, 'g' for glutenfree, 'h' for halal food, follow that up by pressing Enter.");
		var dish = Console.ReadLine();


		if (dish == "v")
		{
			foreach (var s in stuff)
			{
				if (s.Veggie == true)
				{
					Console.WriteLine(s.Number + s.Name);
				}
			}
		}
		else if (dish == "g")
		{
			foreach (var s in stuff)
			{
				if (s.GlutenFree == true)
				{
					Console.WriteLine(s.Number + s.Name);
				}
			}
		}
		else if (dish == "h")
		{
			foreach (var s in stuff)
			{
				if (s.Halal == true)
				{
					Console.WriteLine(s.Number + s.Name);
				}
			}
		}
		else if (dish == "1")
		{
			foreach (var s in stuff)
			{
				if (s.Number == "1")
				{
					Console.WriteLine(s.Name + "\n" + s.Ingredients);
				}
			}
		}
		else if (dish == "2")
		{
			foreach (var s in stuff)
			{
				if (s.Number == "2")
				{
					Console.WriteLine(s.Name + "\n" + s.Ingredients);
				}
			}
		}
		else if (dish == "3")
		{
			foreach (var s in stuff)
			{
				if (s.Number == "3")
				{
					Console.WriteLine(s.Name + "\n" + s.Ingredients);
				}
			}
		}
		else if (dish == "4")
		{
			foreach (var s in stuff)
			{
				if (s.Number == "4")
				{
					Console.WriteLine(s.Name + "\n" + s.Ingredients);
				}
			}
		}
		else if (dish == "5")
		{
			foreach (var s in stuff)
			{
				if (s.Number == "5")
				{
					Console.WriteLine(s.Name + "\n" + s.Ingredients);
				}
			}
		}
		else if (dish == "6")
		{
			foreach (var s in stuff)
			{
				if (s.Number == "6")
				{
					Console.WriteLine(s.Name + "\n" + s.Ingredients);
				}
			}
		}
		else if (dish == "7")
		{
			foreach (var s in stuff)
			{
				if (s.Number == "7")
				{
					Console.WriteLine(s.Name + "\n" + s.Ingredients);
				}
			}
		}
		else if (dish == "8")
		{
			foreach (var s in stuff)
			{
				if (s.Number == "8")
				{
					Console.WriteLine(s.Name + "\n" + s.Ingredients);
				}
			}
		}
		else if (dish == "9")
		{
			foreach (var s in stuff)
			{
				if (s.Number == "9")
				{
					Console.WriteLine(s.Name + "\n" + s.Ingredients);
				}
			}
		}
		else if (dish == "10")
		{
			foreach (var s in stuff)
			{
				if (s.Number == "10")
				{
					Console.WriteLine(s.Name + "\n" + s.Ingredients);
				}
			}
		}
		else if (dish == "11")
		{
			foreach (var s in stuff)
			{
				if (s.Number == "11")
				{
					Console.WriteLine(s.Name + "\n" + s.Ingredients);
				}
			}
		}
		else if (dish == "12")
		{
			foreach (var s in stuff)
			{
				if (s.Number == "12")
				{
					Console.WriteLine(s.Name + "\n" + s.Ingredients);
				}
			}
		}
		else if (dish == "13")
		{
			foreach (var s in stuff)
			{
				if (s.Number == "13")
				{
					Console.WriteLine(s.Name + "\n" + s.Ingredients);
				}
			}
		}
		else if (dish == "14")
		{
			foreach (var s in stuff)
			{
				if (s.Number == "14")
				{
					Console.WriteLine(s.Name + "\n" + s.Ingredients);
				}
			}
		}
		else if (dish == "15")
		{
			foreach (var s in stuff)
			{
				if (s.Number == "15")
				{
					Console.WriteLine(s.Name + "\n" + s.Ingredients);
				}
			}
		}
		else if (dish == "16")
		{
			foreach (var s in stuff)
			{
				if (s.Number == "16")
				{
					Console.WriteLine(s.Name + "\n" + s.Ingredients + "\n");
				}
			}
		}
		else if (dish == "0")
        {
		//go to MainMenu
		} 
		else
		{
			Console.WriteLine("There is no such Dish.");
		}
		Console.WriteLine("Please press Enter to go back.");
		string x = Console.ReadLine();
		
		MenuPage();

	}
}
