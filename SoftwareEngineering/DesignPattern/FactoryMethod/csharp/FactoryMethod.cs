//Empty vocabulary of actual object
public interface IPerson
{
    string GetName();
}

public class Villager : IPerson
{
    public string GetName()
    {
        return "Village Person";
    }
}

public class CityPerson : IPerson
{
    public string GetName()
    {
        return "City Person";
    }
}

public enum PersonType
{
    Rural,
    Urban
}

/// <summary>
/// Implementation of Factory - Used to create objects
/// </summary>
public class Factory
{
    public IPerson GetPerson(PersonType type)
    {
        switch (type)
        {
            case PersonType.Rural:
                return new Villager();
            case PersonType.Urban:
                return new CityPerson();
            default:
                throw new NotSupportedException();
        }
    }
}

/**
 * In the above code you can see the creation of one interface called IPerson and two implementations called Villager and CityPerson. Based on the type passed into the Factory object, we are returning the original concrete object as the interface IPerson.
 * A factory method is just an addition to Factory class. It creates the object of the class through interfaces but on the other hand, it also lets the subclass decide which class is instantiated.
*/

public interface IProduct
{
    string GetName();
    string SetPrice(double price);
}

public class Phone : IProduct 
{
    private double _price;

    public string GetName()
    {
        return "Apple TouchPad";
    }

    public string SetPrice(double price)
    {
        this._price = price;
        return "success";
    }
}

/* Almost same as Factory, just an additional exposure to do something with the created method */
public abstract class ProductAbstractFactory
{
    protected abstract IProduct MakeProduct();

    public IProduct GetObject() // Implementation of Factory Method.
    {
        return this.MakeProduct();
    }
}

public class PhoneConcreteFactory : ProductAbstractFactory
{
    protected override IProduct MakeProduct()
    {
        IProduct product = new Phone();
        //Do something with the object after you get the object. 
        product.SetPrice(20.30);
        return product;
    }
}
