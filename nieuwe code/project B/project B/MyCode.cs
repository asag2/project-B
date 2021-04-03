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
			"Or press 'v' to sort for vegetarian dishes, 'g' for glutenfree, 'h' for halal food, s for spicy and \n'0' to go back to the Main menu, " + 
			"follow that up by pressing Enter.");
		var dish = Console.ReadLine();
		var n = dish;
		List<string> list = new List<string>() { "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "0", "v", "g", "h", "b", "s" };

		if (!list.Contains(n))
		{
			Console.WriteLine("There is no such dish or command");
		}
		else if (dish == "v")
		{
			Console.WriteLine("These are the vegetarian options:\n");
			foreach (var s in stuff)
			{
				if (s.Veggie == true)
				{
					string vegdishes = s.Number + s.Dot + s.Name + s.Price;
					Console.WriteLine(vegdishes);
				}
			}
		}
		else if (dish == "s")
		{
			Console.WriteLine("These are the vegetarian options:\n");
			foreach (var s in stuff)
			{
				if (s.Spicy == true)
				{
					string spicedishes = s.Number + s.Dot + s.Name;
					Console.WriteLine(spicedishes);
				}
			}
		}
		else if (dish == "g")
		{
			Console.WriteLine("These are the glutenfree options:\n");
			foreach (var s in stuff)
			{
				if (s.GlutenFree == true)
				{
					string glfrdishes = s.Number + s.Dot + s.Name;
					Console.WriteLine(glfrdishes);
				}
			}
		}
		else if (dish == "h")
		{
			Console.WriteLine("These are the Halal options:\n");
			foreach (var s in stuff)
			{
				Console.WriteLine(s.Number + s.Dot + s.Name);
				if (s.Halal == true)
				{
					string halaldishes = s.Number + s.Dot + s.Name;
					Console.WriteLine(halaldishes);
				}
			}
		}
		else if (dish == "b")// if b is ur inpu, there will be a list of the dishes that are both vegetarian and glutenfree
		{
			Console.WriteLine("These are the vegeterian glutenfree options:\n");
			foreach (var s in stuff)
			{
				if (s.GlutenFree == true && s.Veggie == true)
				{
					string bothdish = s.Number + s.Dot + s.Name;
					Console.WriteLine(bothdish);
				}
			}
		}
		else if (dish == n)// n is the number you input, and here it will show the details for the specific dishes 
		{
			foreach (var s in stuff)
			{
				if (s.Number == n)
				{
					Console.WriteLine("\n" + s.Name + s.Dot + "\n" + s.Ingredients);
				}
			}
		}
		else if (dish == "0")
        {
		//go to MainMenu
		} 
		Console.WriteLine("Please press Enter to go back.");
		Console.ReadLine();
		MenuPage();
	}
}