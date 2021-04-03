using System;
using System.IO;
using Newtonsoft.Json; 

namespace ProjectB
{
    class userReview
    {
        public string dishReview { get; set; }
    }

    class reviewPage
    {
        static void Main(string[] args)
        {
            //Introduction about page
            Console.WriteLine("***Welcome to the review page!***/n");
            Console.WriteLine("Here you can read and place reviews");
            Console.WriteLine("Enter dishnumber and amount of stars (0-5 *): ");

            userReview UserReview = new userReview
            {
                dishReview = Console.ReadLine()
            };

             
            var reviewResult = JsonConvert.SerializeObject(UserReview);
            var json = File.ReadAllText("dishRatings.json");
            //benegen is wat ik bedoelde met append
            System.IO.File.AppendAllText("dishRatings.json", reviewResult);
            // dit onder kan weg kan weg, is gw om te checken of die het wel toevoegt
            var json1 = File.ReadAllText("dishRatings.json");
            Console.WriteLine(json1);
        }
    }
}
