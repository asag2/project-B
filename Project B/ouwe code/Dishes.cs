using System;
using System.Collections.Generic;
					
public class Program
{
	public static void Main()
	{
Console.WriteLine("         Voorgerechten:");
string[] VGDishes = { "Sashimi tonijn ", "Carpaccio ", "Huzarensalade", "Soep " };  
List<string> VGDishList = new List<string>();  
VGDishList.AddRange(VGDishes);  
foreach (string a in VGDishList)  
Console.WriteLine(a);  

Console.WriteLine("         Tussengerechten:");
string[] TGDishes = { "Pasta", "Eendenborst "};  
List<string> TGDishList = new List<string>();  
TGDishList.AddRange(TGDishes);  
foreach (string a in TGDishList)  
Console.WriteLine(a);  

Console.WriteLine("         Hoofdgerechten:");
string[] HGDishes = { "Biefstuk met knoflookaardappeltjes", "Vis van de dag ", "Kibbeling", "Lasagne" };  
List<string> HGDishList = new List<string>();  
HGDishList.AddRange(HGDishes);  
foreach (string a in HGDishList)  
Console.WriteLine(a);  

Console.WriteLine("         Nagerechten:");
string[] NGDishes = { "Panna Cotta", "Bitterkoekjes", "Kaasplateau"};  
List<string> NGDishList = new List<string>();  
NGDishList.AddRange(NGDishes);  
foreach (string a in NGDishList)  
Console.WriteLine(a);  
		
Console.WriteLine("         Drinken:");
string[] Drinken = { "Frisdrank/Soda", "Wijn", "Beer"};  
List<string> DrankList = new List<string>();  
DrankList.AddRange(Drinken);  
foreach (string a in DrankList)  
Console.WriteLine(a);  
	}
}
