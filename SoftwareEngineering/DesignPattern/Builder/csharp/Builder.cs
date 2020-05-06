/// <summary>
/// Represents a product created by the builder
/// </summary>
public class Car
{
    public string Make { get; set; }
    public string Model { get; set; }
    public int NumDoors { get; set; }
    public string Colour { get; set; }

    public Car(string make, string model, string colour, int numDoors)
    {
        Make = make;
        Model = model;
        Colour = colour;
        NumDoors = numDoors;
    }
}

/// <summary>
/// The builder abstraction
/// </summary>
public interface ICarBuilder
{
    string Colour { get; set; }
    int NumDoors { get; set; }

    Car GetResult();
}

/// <summary>
/// Concrete builder implementation
/// </summary>
public class FerrariBuilder : ICarBuilder
{
    public string Colour { get; set; }
    public int NumDoors { get; set; }

    public Car GetResult()
    {
        return NumDoors == 2 ? new Car("Ferrari", "488 Spider", Colour, NumDoors) : null;        
    }
}

/// <summary>
/// The director
/// </summary>
public class SportsCarBuildDirector
{
    private ICarBuilder _builder;
    public SportsCarBuildDirector(ICarBuilder builder) 
    {
        _builder = builder;
    }

    public void Construct()
    {
        _builder.Colour = "Red";
        _builder.NumDoors = 2;
    }
}

public class Client
{
    public void DoSomethingWithCars()
    {

        var builder = new FerrariBuilder();
        var director = new SportsCarBuildDirector(builder);

        director.Construct();
        Car myRaceCar = builder.GetResult();
    }
}